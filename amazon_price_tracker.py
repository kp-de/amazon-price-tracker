import requests
from bs4 import BeautifulSoup

#### Function to convert the scraped price value into an integer value
def int_converter(original):
	#print original
	new = original.split(',')
	#print new
	pre_int = ''
	for val in new:
		pre_int = pre_int + val
	#print pre_int
	return int(pre_int)	

## Future enhancement: move this to a file based configuration where user can add URL to be tracked
url = 'https://www.amazon.in/Apple-MacBook-13-inch-Display-Dual-core/dp/B07KJQFNDQ'

my_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

headers = {"User-Agent": my_user_agent}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
price = soup.find(id="priceblock_ourprice").get_text()    ## Do inspect element for this
title = soup.find(id="productTitle").get_text()			  ## Do inspect element for this
#print("reached here")
print("Item name: " + title.strip())

trunc_price = price[2:len(price)-3]                       ## Trunc logic for Amazon.in 
#print trunc_price
converted_price = int_converter(trunc_price)
print ('price of the item is: ' + str(converted_price))
#print(converted_price)


## File operations now
readfile = open("price_log.txt","r")
old_price = readfile.readlines()
print ("old price was: " + str(old_price[0]))
readfile.close()

#overwrite with the latest price
filename = open("price_log.txt","w")
filename.write(str(converted_price))
filename.close()

## compare the old and new price 
## Future enhancement: can add actions like sending email alert here
if converted_price < int(old_price[0]):
	print("Hurry! Prices dropped!!")
elif converted_price > int(old_price[0]):
	print("Oops, price has increased")
else:
	print("Same price")