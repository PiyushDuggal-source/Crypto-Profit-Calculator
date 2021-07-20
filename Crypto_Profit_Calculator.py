def profit(crypto_price, investment,increment):
	fees = investment *1.004
	crypto_count =  investment/crypto_price
	if crypto_count in range(0,100):
		print("Good you are investing in {} crypto".format(investment/crypto_price))
	print("You are investing {:.2f} rupees on {:.2f} cryptocurrencies ".format(fees,crypto_count))
	selling_price = crypto_price + increment
	selling_fees = selling_price*crypto_count
	selling_price_without_fee = selling_fees-(selling_price*(0.4/100))
	
	profit_price = selling_price_without_fee - fees
	
	
	print("If you sell {:.2f} cryptocurrencies at {}rs\nthen you will get {:.2f} in return and {:.2f} profit.".format(crypto_count,selling_price,selling_price_without_fee,profit_price))
	if profit_price < 0:
		print("you should buy an another crypto or increase the amount of investment ")
	
price = float(input("Enter the Crypto price: "))
invest = float(input("Enter the amount you want to invest: "))
incre = float(input("Enter the increment: "))
profit(price,invest,incre)