import bs4
import urllib.request
import smtplib
import time
#to store the price of the item at different days
price_list = []

def check_price():
    #The item I have chosen is M1 Macbook Air
    url = 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_3?crid=3D1OMQQAFOOM9&keywords=macbook+air&qid=1658172499&sprefix=macbook+ai%2Caps%2C373&sr=8-3'
    
    #Extracting the webpage as HTML using BeautifulSoup
    url_read = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(url_read, "html.parser")
    
    #Extracting the price and converting it to float 
    prices = soup.find(id="a-price-whole").get_text()
    prices = float(prices.replace(",", "").replace("₹", ""))
    price_list.append(prices)
    return prices

#To send email to the user
def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()

#To check if the price has decreased or not 
def price_decrease_check(price_list):
    if price_list[-1] < price_list[-2]:
        return True
    else:
        return False

count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(prices_list)
        if flag:
            decrease = prices_list[-1] - prices_list[-2]
            message = f"The price is decreased by {decrease} rupees. Please check the item"
            send_email(message,"evildoctor596@gmail.com","abcd1234","progamers0419@gmail.com")
    #Since we are checking the difference in prize on a daily basis I have given 86400 to thread.sleep
    time.sleep(86400)
    count += 1
