import requests
from bs4 import *
import smtplib

EMAIL = "harishchaudhary0129@gmail.com"
PASSWORD = "fqccdufsdzdcqemv"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
    "Accept-Language": "en-US;q=0.7"
}

URL = "https://www.flipkart.com/mi-xxq01hm-runtime-90-min-trimmer-men/p/itmd59b4b567329e?" \
      "pid=TMRFJPH3DBURGEZR&lid=LSTTMRFJPH3DBURGEZRM906O8&marketplace=FLIPKART&" \
      "q=mi+trimmer&store=zlw%2F79s%2Fby3&srno=s_1_2&otracker=search&otracker1=search&fm=Search" \
      "&iid=85661007-9edf-4b09-ba24-7167021541c2.TMRFJPH3DBURGEZR.SEARCH" \
      "&ppt=sp&ppn=sp&ssid=l78q7qvws00000001655395789190&qH=4396d4b75863e9a9"

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text.encode('ascii', 'ignore').decode('ascii'), "html.parser")
price = float(soup.find(name="div", class_="_30jeq3").getText().replace(",", ""))
item_name = soup.find(name="span", class_="B_NuCI").getText()

content = f"{item_name}\n{price}\n{URL}"

if price <= 1000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="kaushikji1211@gmail.com",
                            msg=f"{price}\n{item_name}\n{URL}"
                            )
