

from urllib.request import urlopen
import bs4

class WebClientBanggood(object):
    """WebClientBanggood class"""
    def __init__(self):
        super(WebClientBanggood, self).__init__()

    def download_page(arg):
        #connect to the web site
        f = urlopen("https://www.banggood.com/es/Flashdeals.html")
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
        for activity in data:
            print(activity)

    def search_activities(self, page):
        tree = bs4.BeautifulSoup(page, "lxml")
        activities = tree.find_all("li")

        for activity in activities:
            if activity.has_attr("data-product-id"):
                title = activity.find("span", "title").find("a")
                price = activity.find("span", {"class" : "price"})
                link = title["href"]

                yield title.text + "\n" + link + "\n" + price.text + "\n"


if __name__ == "__main__":
    c = WebClientBanggood()
    c.run()
