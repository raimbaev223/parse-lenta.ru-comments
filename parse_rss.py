import lxml
from lxml import etree, html
import requests


def get_xml():
    response = requests.get("https://lenta.ru/rss/news")
    with open("data.xml", "w") as f:
        f.write(response.text)
        f.close()


def parse_xml(xmlfile):
    with open("data.xml") as file:
        xml = file.read()

    root = etree.fromstring(xml, parser=lxml.html.HTMLParser(encoding='utf-8'))

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = 'None'
            else:
                text = elem.text

            print(elem.tag + " => " + text)


def main():
    get_xml()
    parse_xml("data.xml")


if __name__ == "__main__":
    main()