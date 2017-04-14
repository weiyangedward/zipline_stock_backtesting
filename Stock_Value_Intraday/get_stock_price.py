from rtstock.stock import Stock
import time, sys
from time import gmtime, strftime


def get_stock_price(stock_name):
	try:
		stock = Stock(stock_name)
		return stock.get_latest_price()		
	except:
		print "Error!"

def main():
	if len(sys.argv) < 2:
		print "Usage: python get_stock_price.py stock_name"
		exit(1)

	stock_name = sys.argv[1]
	for i in range(10):
		print get_stock_price(stock_name), strftime("%Y-%m-%d %H:%M:%S", gmtime())
		time.sleep(5)
	

if __name__ == '__main__':
	main()
