import requests
from bs4 import BeautifulSoup

def search_avito():
    params = {"page" : "2" }
    avito_url = "https://bel.kupiprodai.ru/auto/"
    try:   
        result = requests.get(avito_url, params = params)
        result.raise_for_status()
        stat_code = result.status_code
        for i in range(200, 206):
            if i == stat_code:
                return result.text   
    except(requests.RequestException, ValueError):
        return "Сетевая ошибка"

def get_product():
    html = search_avito()
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_product = soup.find_all("div", class_= "list_info_top")
        result_product = []
        for all_product_list in all_product:
            url = all_product_list.find("a")["href"]
            result_product.append(url)
        return print(result_product)
    return False    
        
def product_number():
    prod_list = get_product()
    n=-1
    try:
        for list_1 in prod_list:
            product_url = prod_list[n+1]
            resultat = requests.get(product_url)
            resultat.raise_for_status()
            stat_code = resultat.status_code
            for i in range(200, 206):
                if i == stat_code:
                    print (resultat.text)
    except(requests.RequestException, ValueError):
        return "Сетевая ошибка"
             
             
if __name__ =="__main__":
    print(get_product())
 