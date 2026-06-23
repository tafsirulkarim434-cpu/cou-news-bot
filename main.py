import requests
from bs4 import BeautifulSoup

import os

BOT_TOKEN = os.environ["8919943087:AAF1fOdVGvchW5mgAwDDNGQawEPTrMn71uY"]
CHAT_ID = os.environ["7106520212"]

KEYWORDS = ["কুমিল্লা বিশ্ববিদ্যালয়", "কুবি", "Comilla University"]

SITES = [
    "https://dailygonokantho.com",
    "https://newsvision.com.bd",
    "https://bdtelegraph24.com"
]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_site(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text()

        for k in KEYWORDS:
            if k in text:
                send_telegram(f"📰 কুবি নিউজ পাওয়া গেছে!\n\n{url}")
                break
    except:
        pass

for site in SITES:
    check_site(site)
