""" Just a simple example of using the web scrapping method in order to get
    data from banggood's web.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

class WebClientBanggood(object):
    """ A class used to scrape data from banggood.
    """
    def __init__(self):
        """ Initializes the class with the banggood's url.
        """
        self.url = "https://www.banggood.com/Flashdeals.html"

    def download_page(self):
        """ Get the string of the html web page from the url.
        """
        # connect to the web site
        fd_web = urlopen(self.url)
        # get the download_page
        page = fd_web.read()
        # close the connection
        fd_web.close()
        return page


    def run(self):
        """ The starter method for the web scrapping action.
        """
        # download a web page
        page = self.download_page()
        # search activities in web page
        data = WebClientBanggood.search_activities(page)
        # print the items found in the page
        for item in data:
            print(item)

    @staticmethod
    def search_activities(page):
        """ Using BeatifulSoup, get the information about deal offers
            and yields the data as a dictionary type with title, price and price_old
            keys.
        """
        tree = BeautifulSoup(page, "lxml")
        activities = tree.find_all("li")

        for activity in activities:
            if activity.has_attr("data-product-id"):
                title = activity.find("span", "title").find("a").text
                price = activity.find("span", {"class" : "price"}).text
                price_old_span = activity.find("span", {"class" : "price_old"})
                #If there isn't any old_price, old_price = price
                price_old = price_old_span.text if not price_old_span is None else price

                yield {"title": title, "price": price, "price_old": price_old}

if __name__ == "__main__":
    WebClientBanggood().run()
