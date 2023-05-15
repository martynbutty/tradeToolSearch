import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def searchToolstation(search_term):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    encoded_string = urllib.parse.quote(search_term)

    url = f"https://www.toolstation.com/search?q={encoded_string}"

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    prodDescEl = soup.find("p", string=lambda text: text and search_term in text)
    description = prodDescEl.text.replace('\n', '').strip()
    prodCodeEl = prodDescEl.parent.parent
    prodUrl = prodCodeEl.findNext('a').get('href')

    priceEl = prodCodeEl.findNext('div')
    price = priceEl.findNext('span').text.replace('£', '')

    json_object = {
      "name": description,
      "Merchant": "Toolstation",
      "description": description,
      "url": prodUrl,
      "price": price,
      "currency": "GBP"
    }

    driver.quit()
    return json_object


# Format of HTML is a DIV containing sub-divs with no meaingful id's to search. So we search for the original search term
# occuring in a <p>. If found, it's probably the main product description which is wrapped inside a <a>, and has a parent
# <p> which contains the (toolstation) product code. This <p> with product code has a parent <div>. This div's next
# sibling should be another <div> which contains <p> -> <span> with value being price