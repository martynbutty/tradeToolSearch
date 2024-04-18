import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup


def searchFFX(search_term):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    encoded_string = urllib.parse.quote(search_term)
    url = f"https://ffx.co.uk/search/{encoded_string}"
    driver.get(url)

    # Search page loads results async, so wait a short while for results to come in
    elem = WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "ais-Hits-list"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find the first <li> element in <ol class="ais-Hits-list">
    first_li = soup.find("ol", class_="ais-Hits-list").find("li")

    # Read the value of <div class="pt-2">
    if first_li:
        price_div_element = first_li.find("div", class_="pt-2")

        # Find the <a> element within the <div> element
        url_element = first_li.find('div', class_='mx-auto hit-imageURL').find('a')

        if price_div_element:
            span_element = price_div_element.find('span')
            if span_element:
                span_element.extract()  # Remove the span element

        if url_element:
            url = "https://ffx.co.uk" + url_element.get('href')

        desc_element = soup.find('span', class_='ais-Highlight-nonHighlighted')

        # Get the text value of the <span> element
        if desc_element:
            description = desc_element.get_text(strip=True).replace('<em>', '').replace('</em>', '')
        else:
            description = search_term

        price = price_div_element.get_text(strip=True).replace('£', '')
    else:
        price = 0
        print("No <li> elements found.")

    json_object = {
        "name": description,
        "Merchant": "FFX",
        "description": description,
        "url": url,
        "price": price,
        "currency": "GBP"
    }

    driver.quit()
    return json_object
