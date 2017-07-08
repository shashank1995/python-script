import requests
import json
import smtplib   

stock_list = []
stock_info = {}

def stock(stock_name):
		link = 'http://finance.google.com/finance/info?client=ig&q=NSE:' + stock_name
		response = requests.get(link)
		a = response.content
		a = a.translate(None, '/')
		a = json.loads(a)
		stock_closing_price = float(a[0]['l'])
		stock_price_change = float(a[0]['c'])
		stock_percentage_change = float(a[0]['cp'])
		stock_info['stock name'] = stock_name
		stock_info['stock closing price'] = stock_closing_price
		stock_info['stock price change'] = stock_price_change
		stock_info['stock percentage change'] = stock_percentage_change
		stock_list.append(stock_info.copy())
				

def sending_email():
	to = ['shashank_adityasingh@yahoo.com']
	gmail_user = 'shashank.adityasingh@gmail.com'
	gmail_pwd = 'tqbckcoswingeasp'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	for recipients in to:
		header = 'To:' + recipients + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Your latest stock prices \n'
		msg = '\n' + 'Stock detail:\n\n'
		for stocks in stock_list:
			msg += 'Stock name: ' + stocks['stock name'] + '\n' + 'Stock closing price: ' + str(stocks['stock closing price']) + '\n' + 'Stock absolute price change in Rupees: ' + str(stocks['stock price change']) + '\n' + 'Stock change in percentage: ' + str(stocks['stock percentage change']) + '%\n\n'
		message = header + msg
		smtpserver.sendmail(gmail_user, recipients, message)
	smtpserver.close()

stock('SBIN')
stock('ANANTRAJ')
sending_email()