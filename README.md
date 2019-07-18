# amazon-price-tracker
A simple web crawler to track the price of an item on Amazon. Coded in Python. Currently, works for a single product URL hard coded in the code. Can be enhanced to multiple items being read from config files in future.  
  
Stores the last price on Amazon to a file and compares the current price with that price. Currently, only one past price is stored to make a decision (up/ down/ same). Can be enhanced to track historical prices.

# Prerequisites
You will need to install a couple of python packages   

> pip install requests   
> pip install bs4   

# How to run  
> python2.7 amazon_price_tacker.py

