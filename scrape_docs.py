import requests
from bs4 import BeautifulSoup

URLS = [
    "https://cloud.google.com/run/docs/troubleshooting",
    "https://cloud.google.com/run/docs/container-contract",
    "https://cloud.google.com/run/docs/configuring/services/containers"
]


def scrape():

    all_text = []

    for url in URLS:

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = "\n".join([p.get_text() for p in paragraphs])

        all_text.append(text)

    final_text = "\n".join(all_text)

    with open("docs/gcp_docs.txt", "w", encoding="utf-8") as f:
        f.write(final_text)

    print("Docs scraped successfully")


if __name__ == "__main__":
    scrape()