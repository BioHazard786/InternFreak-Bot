from .__init__ import *
from ..Helpers.FetchInfo import fetch_info


def fetch_posts():
    response = requests.get("https://internfreak.co/")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        post_info = dict()
        posts = soup.select("div.post-entry.d-block.small-post-entry-v")
        for post in posts:
            try:
                title = post.find("h2", class_="heading").getText()
            except:
                title = "N/A"
            try:
                date = post.find("span", class_="date").getText()
            except:
                date = "N/A"
            try:
                link = "https://internfreak.co/" + \
                    post.find("h2", class_="heading").findChildren()[0]["href"]
            except:
                link = "https://internfreak.co/"

            info = fetch_info(link, date)
            if info:
                post_info[title] = info
            else:
                continue

        return post_info
    else:
        return False
