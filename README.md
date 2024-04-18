# tradeToolSearch
Search for trade (power) tools and gear from multiple suppliers to find the best deal

## Prerequisites
The project has a pipenv that contains all the dependencies, so all you'll need to get going is python3 with pip and 
pipenv installed.

Once you have python3 and pip available, you can install pipenv with 
`sudo pip install pipenv`

Then install the dependancies by pointing your IDE to the pipenv, or in a terminal run
`pipenv install`

The project uses selenium with chromedriver to control chrome/chromium to visit some suppliers websites. You may find 
that just installing the pipenv will be all you need, however if you get strange errors about webdriver shutting down 
etc, you could try [https://chromedriver.chromium.org/getting-started](https://chromedriver.chromium.org/getting-started)
