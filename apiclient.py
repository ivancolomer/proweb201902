

from urllib.request import urlopen
import json
import pprint

class ApiClient(object):
    """ApiWeather class"""
    def __init__(self):
        super(ApiClient, self).__init__()

    def download_page(arg):
        #connect to the web site
        f = urlopen("https://api.openweathermap.org/data/2.5/weather?q=Lleida,es&appid=fce9a295cc0f29f3b41bf0505cca3783")
        #get the download_page
        page = f.read()
        #close the connection
        f.close()
        return page


    def run(self):
        # download a web page
        page = self.download_page()
        # search activities in web page
        data = self.search_activities(page)
        # print the activities
        print(data)

    def search_activities(self, page):
        dict = json.loads(page)
        pprint.pprint(dict)
        temp = dict['main']['temp']
        weather = dict['weather'][0]['description']
        return str(temp) + " and " + weather

if __name__ == "__main__":
    c = ApiClient()
    c.run()
