import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


def searchScrewfix(search_term):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    encoded_string = urllib.parse.quote(search_term)
    url = f"https://www.screwfix.com/search?search={encoded_string}"
    driver.get(url)

    html = driver.page_source
    jsonLDSearchString = "<script type=\"application/ld+json\" data-qaid=\"seo-properties\">"
    start_index = html.index(jsonLDSearchString) + len(jsonLDSearchString)
    end_index = html.index("</script>", start_index)
    json_ld_data = json.loads(html[start_index:end_index].strip())

    name = json_ld_data['name']
    description = json_ld_data['description']
    url = json_ld_data['offers'][0]['url']
    price = json_ld_data['offers'][0]['price']
    cur = json_ld_data['offers'][0]['priceCurrency']

    json_object = {
        "name": name,
        "Merchant": "Screwfix",
        "description": description,
        "url": url,
        "price": price,
        "currency": cur
    }

    driver.quit()
    return json_object
