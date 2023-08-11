import requests

def GetLocation():
    """
    :return String of City:
    """
    return input("City: ")

def GetData(location):
    """
    :param location (string):
    :return json file with Weather data :
    """
    params = {"access_key": "d866e816bf5ae317478c15d2d405e915", "query": location}
    api_url = "http://api.weatherstack.com/current"

    return requests.get(api_url, params).json()

def makeStrFromList(List):
    newStr = ""
    for element in List:
        if len(List) > 1:
            newStr += element + ", "
        else:
            newStr += element

    return newStr

def PrintWeatherData():
    """
    Prints Weather Information in given Location
    """
    Loc = GetLocation()
    Data = GetData(Loc)

    Weather_des = Data["current"]["weather_descriptions"]
    UV_Index = Data["current"]["uv_index"]
    print("Local time:", Data["location"]["localtime"])
    print("Location: ", Data["location"]["name"] + ", ", Data["location"]["country"])
    print("Temperature:", str(Data["current"]["temperature"])+"°C" + " Feels like:", str(Data["current"]["feelslike"])+"°C")
    print("Weather description: ", makeStrFromList(Data["current"]["weather_descriptions"]))
    print("UV-Index: ", str(UV_Index))
    if UV_Index >= 3:
        print("SUN PROTECTION RECOMMENDED")
