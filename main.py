import requests
from bs4 import BeautifulSoup
headers = {
    "Accept-Language":"en-US,en;q=0.5",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
}
parameters ={
    "keywords":"earbuds",
    "qid":1675350202,
    "sprefix":"ear%2Caps%2C223",
    "sr":"8-2-spons",
    "sp_csd":"d2lkZ2V0TmFtZT1zcF9hdGY&th=1",

}
link = "https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/ref=sr_1_2_sspa"
response = requests.get(url=link,params=parameters,headers=headers).text
soup = BeautifulSoup(response,"html.parser")
price = soup.find(name="input",id="twister-plus-price-data-price").get("value")
product = soup.find(name="title").getText().split(" ")
product_name = product[0]+" "+product[1]

import smtplib
my_email = "SENDER_MAIL_ID"
password = "PASSWORD"

if (int(price)<900):
    with smtplib.SMTP("smtp.gmail.com") as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(from_addr=my_email,to_addrs="RECEIVER_MAIL_ID",
                           msg=f"Subject:Price Drop Alert!!\n\nYour wait is over. {product_name}'s price has finally dropped.\nNow you can purchase it for Rs {price}.\nGo to {link} right now and catch the deal!")
