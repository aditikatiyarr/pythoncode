import validators
import json
import urllib3.request
from urllib.request import urlopen
  
f=open("input.txt",'r')
urls=f.readlines()
fit=open("output.txt","w")
for x in urls:
    valid=validators.url(x)
    if valid==True:
        try:
            response = urlopen(x)
            data_json = json.loads(response.read())
            for i in data_json:
                for j in i:
                    print(j+', '+i[j]['grade'],file=fit)
        except ValueError as err:
            print('file is not a JSON file')     
    else:
        print("URL is incorrect")

open("output.txt","a")
fit.close()
f.close()


