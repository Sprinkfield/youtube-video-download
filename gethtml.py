import requests


class HtmlPageManip:
    def __init__(self) -> None:
        pass

    def get_html_of_page(self, url_of_the_page) -> str:
        try:
            url = requests.get(url_of_the_page)
            htmltext = url.text
        except:
            exit("Error getting HTML code of the page!")

        return htmltext
