

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
        #print(page)

    def search_activities(self, page):
        tree = bs4.BeautifulSoup(page, "lxml")
        activities = tree.find_all("li")

        for activity in activities:
            if activity.has_attr("data-product-id"):
                title = activity.find("span", "title").find("a")
                print(title.text, "[" + title["href"] + "]")
                print()


if __name__ == "__main__":
    c = WebClientBanggood()
    c.run()
