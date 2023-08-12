import requests

class Weather:
    def __init__(self):
        self.Data = None
        self.dataState = False

    def GetData(self,location):
        """
        :param location (string):
        :return .json with Weather data :
        """
        params = {"access_key": "d866e816bf5ae317478c15d2d405e915", "query": location}
        api_url = "http://api.weatherstack.com/current"

        self.Data = requests.get(api_url, params).json()

    def makeStrFromList(self,List):
        """
        :param List:
        :return string:
        """
        newStr = ""
        for element in List:
            if len(List) > 1:
                newStr += element + ", "
            else:
                newStr += element

        return newStr

