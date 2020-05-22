import requests
from lxml import etree

response = requests.get("https://lenta.ru/rss/news", )

with open("data.xml", "w") as f:
    f.write(response.text)
    f.close()

links_list = []

tree = etree.parse('data.xml')

nodes = tree.xpath('/rss/channel/item/guid')

with open("links.csv", "w") as f:
    for node in nodes:
        f.write(f'{node.text} \n')
    f.close()
