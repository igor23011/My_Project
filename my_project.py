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
        return result_product
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
                    True
            return resultat.text
    except(requests.RequestException, ValueError):
        return "Сетевая ошибка"

def info_product():
    text_product = product_number()
    soup_info = BeautifulSoup(text_product, "html.parser")
    all_info_product = soup_info.find_all("div", class_= "msg_title width100")
    all_info_prod = soup_info.find_all("div", class_= "msg_data_info")
    all_info_price = soup_info.find_all("div", class_= "msg_price width100")
    all_address_product = soup_info.find_all("div", class_= "msg_info width100 margin_bottom_50")
    all_text_product = soup_info.find_all("div", class_= "msg_text width100 box-sizing margin_bottom_50")
    all_product = []
    for product_list_info in all_info_product:
        title_product = product_list_info.find("h1").text
        all_product.append({
            "title":title_product
            })  
    for prod_list_info in all_info_prod:
        __product = prod_list_info.text.strip(' \n\t')
        sale = __product.split(",")[0]
        sale_info = __product.split(",")[1].replace('\t',"").replace( "\n", " ")
        all_product.append({
            "№ sale":sale
            })
        all_product.append({
            "sale_info":sale_info
        })             
    for product_price_info in all_info_price:
        price_product = product_price_info.text
        all_product.append({
            "price":price_product
            })  
    for product_address_info in all_address_product:
        address_product = product_address_info.select("p")[1].text.replace('\t',"")
        all_product.append({
            "Address":address_product
            })  
    for product_text_info in all_text_product:
        text_product = product_text_info.find("p").text
        all_product.append({
            "text_sale":text_product
            })          
    return all_product
     
             
if __name__ =="__main__":
    print(product_number())
 