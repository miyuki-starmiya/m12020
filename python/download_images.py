
import requests
import random
import shutil
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def image(data,num):
    res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    html = res.text
    soup = bs4.BeautifulSoup(html,'lxml')
    # get all img tag
    links = soup.find_all("img")
    # print(links)]
    link = links[num].get("src")
    return link

def download(url,file_name):
    req = requests.get(url, stream=True)
    #req = requests.get(url)
    if req.status_code == 200:
        with open(file_name + ".png", 'wb') as f:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, f)

name = input("Who is you search for ?:")
for i in range(1,20):
    link = image(name,i)
    download(link,name + str(i))
    print(link)
    i += 1

