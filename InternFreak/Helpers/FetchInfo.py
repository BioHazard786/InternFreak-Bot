from .__init__ import *


def fetch_info(url, date) -> dict:
    post_info = dict()
    response = requests.get(url)
    if response.status_code == 200 and url != "https://internfreak.co/":
        soup = BeautifulSoup(response.text, "html.parser")
        info = soup.select_one("div.col-lg-8")

        thumbnail = "https://internfreak.co/" + \
                    info.find("img")["src"]
        post_info["Thumbnail"] = thumbnail
        post_info["Date"] = date

        description = info.select_one("p")
        description.extract()

        designation_key = info.select_one("h5")
        designation = info.select_one("div.col-lg-8 div p")
        post_info[designation_key.text.split(
            ":")[0].strip()] = designation.text.strip()
        designation.extract()
        designation_key.extract()

        batch_key = info.select_one("h5")
        batch = info.select_one("p")
        post_info[batch_key.text.split(
            ":")[0].strip()] = batch.text.strip()
        batch.extract()
        batch_key.extract()

        salary_key = info.select_one("h5")
        salary = info.select_one("p")
        post_info[salary_key.text.split(
            ":")[0].strip()] = salary.text.strip()
        salary.extract()
        salary_key.extract()

        important_key = info.select_one("strong")
        important_key.extract()
        important = info.select_one("p")
        important.extract()

        location_key = info.select_one("h5")
        location = info.select_one("p")
        post_info[location_key.text.split(
            ":")[0].strip()] = location.text.strip()
        location.extract()
        location_key.extract()

        apply_link = info.select_one("a#applylink").get("href")
        post_info["Apply"] = apply_link

        post_info["Link"] = url

        return post_info

    else:
        return dict()
