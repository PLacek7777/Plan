import requests
from bs4 import BeautifulSoup as bs

path = "plan.html"
planPath = "plan.xlsx"
version = "version.txt"
url = "https://www.ur.edu.pl/pl/collegium-medicum/wydzial-nauk-o-zdrowiu-i-psychologii/student/kierunki-studiow-programy-rozklady-sylabusy/ratownictwo-medyczne/rozklady-zajec"

def getHTML(url):
    with open(path, "wb") as f:
        print("INFO >> getting html from web")
        site = requests.get(url).content
        f.write(site)
        return site

def getXLSX(url):
    try:
        with open(version, 'r+') as f:
            check = f.read()
            # print(f"DEBUG >> checking {check} with {url}")
            if check == url:
                print("INFO >> No update \nINFO >> exiting")
                return 0
            else:
                f.truncate(0)
                f.write(url)

    except FileNotFoundError:
        with open(version, 'w') as f:
            f.write(url)

    print(f"\nINFO >> Geting plan file from {url}\n")

    plan = requests.get(url)

    if plan.status_code == 200:
        with open(planPath, "wb") as f:
            f.write(plan.content)
            print("INFO >> Plan file dowland succesfull")
    else:
        print(f"ERROR >> Plan dowland code {plan.status_code}")

html = getHTML(url)
soup = bs(html, 'html.parser')
planURL = "https://www.ur.edu.pl" + soup.select_one('#article-1672598 > div.content-text > div > table:nth-child(5) > tbody > tr:nth-child(2) > td:nth-child(1) > p:nth-child(1) > a')['href']

getXLSX(planURL)
