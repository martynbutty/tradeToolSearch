from screwfixSearch import *
from toolstationSearch import *
from ffxSearch import *

searchString = "DeWalt DCG405N-XJ"

# Print the prices
print("Screwfix: £", searchScrewfix(searchString))
print("Toolstation: £", searchToolstation(searchString))
print("DIY: £", "NOT IMPLEMENTED")
print("Wickes: £", "NOT IMPLEMENTED")
print("FFX: £", searchFFX(searchString))
