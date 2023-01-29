import httpx
from pprint import pprint

#nejak udelat vemv
url = ("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=CDD965808FFAC8AEB077638397FDBD6D?date=23.01.2023")

res = httpx.get(url)
rows = res.text.split("\n")

a = dict()
for r in rows[2:-1]:
    r =r.split("|")
    a[r[3]] = float(r[4].replace(',','.')) * int(r[2])
    


rec = input("zadejte mněnu: ")

num =int(input("zadejte castku v Kč: "))


print(round(num/a.get(rec),2) ,rec)



#peso
#pprint(a)
