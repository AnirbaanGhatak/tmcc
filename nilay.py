from urllib.request import Request,urlopen
import time
#Change the url adress in urllib.request.urlopen



def cc_links(url):
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req)

    hrefs=[]
    doc=page.read()
    for i in range(0, len(doc)):
        if doc[i:i+8]==b"<a href=":
            a=0
            for n in range(i+8, len(doc)):
                if chr(doc[n])=="\"":
                    a+=1
                    if a==2:
                        hrefs+=[str(doc[i+9:n])]
                        break

    [print(href) for href in hrefs]


banks= ['hdfc-bank', 'sbi-card', 'yes-bank', 'idfc-first-bank', 'au-small-finance-bank', 'indusind-bank', 'axis-bank', 'kotak', 'icici-bank', 'american-express']
for b in banks:
    bank_url="https://cardinsider.com/"+b
    cc_links(bank_url)