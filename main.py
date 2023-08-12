import WeatherData as WD
import tkinter as tk
from PIL import ImageTk
from urllib.request import urlopen
import webbrowser

weather = WD.Weather()

class myGIU:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('WeatherApp')
        self.root.geometry('300x400')
        self.root.resizable(width='False', height='False')
        self.root.configure(background="#96B4E4")
        self.root.iconbitmap("icon_sun.ico")
        self.InputVar = tk.StringVar()
        self.Entry = tk.Entry(self.root, textvariable=self.InputVar)
        self.Entry.pack(pady=20)

        self.Button = tk.Button(self.root, text='Find', command=self.ButtonFind)
        self.Button.pack()

        self.ImageRawData = None
        self.WeatherIcon = None
        self.IconLabel = None

        self.textLabelLocation = None
        self.textLabelTemperature = None
        self.textLabelFeelsLike= None
        self.textLabelWeatherDescription = None
        self.textLabelUvIndex = None
        self.textLabelCurrentTime = None

        self.linkLabel = tk.Label(self.root, text='Weather info provided by weatherstack.com', fg="blue", bg="#96B4E4", font=("Platino", 8))
        self.linkLabel.place(x="40", y="380")
        self.linkLabel.bind("<Button-1>", lambda e: self.OpenWebPage('https://weatherstack.com'))


    def OpenWebPage(self, URL):
        """
        Opens Website from Given URL
        :param URL:
        """
        webbrowser.open(URL)

    def ButtonFind(self):
        if self.IconLabel:
            self.IconLabel.destroy()

        Location = self.InputVar.get()
        weather.GetData(Location)
        self.SetWeatherIcon()
        self.RefreshWeatherData(weather.Data)
        weather.dataState = True

    def SetImageRawData(self, URL):
        link = urlopen(URL)
        self.ImageRawData = link.read()
        link.close()

    def SetWeatherIcon(self):
        self.SetImageRawData(weather.Data['current']['weather_icons'][0])
        self.WeatherIcon = ImageTk.PhotoImage(data=self.ImageRawData)
        self.IconLabel = tk.Label(self.root, image=self.WeatherIcon,bg='#96B4E4')
        self.IconLabel.image = self.WeatherIcon
        self.IconLabel.place(x="115", y="130")

    def RefreshTextLabel(self, label_var, text, x, y, fontSize = 11):
        """
        Creates or changes (if existing) a TextLabel at location(x,y) with Platino font
        :param label_var:
        :String text:
        :int x:
        :int y:
        :int fontSize - Default value is 11:
        :returns Text label
        """
        if label_var:
            label_var.config(text=text)
        else:
            label_var = tk.Label(self.root, text=text, bg='#96B4E4', font=("Platino", fontSize))
            label_var.place(x=str(x), y=str(y))
        return label_var

    def RefreshWeatherData(self, Data):
        locationstr = Data['location']['name'] + ',' + Data['location']['country']
        self.textLabelLocation = self.RefreshTextLabel(self.textLabelLocation, locationstr, 30, 100, 11)

        tempstr = str(Data['current']['temperature']) + "°C"
        self.textLabelTemperature = self.RefreshTextLabel(self.textLabelTemperature, tempstr,132,200)

        feelslikestr = 'Feels like: ' + str(Data['current']['feelslike']) + '°C'
        self.textLabelFeelsLike = self.RefreshTextLabel(self.textLabelFeelsLike, feelslikestr, 50, 240)

        weatherdescstr = 'Weather description: ' + weather.makeStrFromList(Data["current"]["weather_descriptions"])
        self.textLabelWeatherDescription = self.RefreshTextLabel(self.textLabelWeatherDescription,weatherdescstr, 50,270)

        uvindexstr = 'UV-Index: ' + str(Data['current']['uv_index'])
        self.textLabelUvIndex = self.RefreshTextLabel(self.textLabelUvIndex, uvindexstr, 50, 300)

        localtimestr = 'Local time: ' + str(Data['location']['localtime'])
        self.textLabelCurrentTime = self.RefreshTextLabel(self.textLabelCurrentTime, localtimestr, 50, 330)

myGUI = myGIU()
myGUI.root.mainloop()

