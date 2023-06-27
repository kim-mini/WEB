import requests
import json

url = "http://192.168.50.102:8080"
# url 에 https 가 아닌 http 사용할 것

temp = {
	"LOT" : "123",
	"DBLINK" : "123"
}


#data = requests.get(url).json()

response = requests.get(url, params=temp).json()

print(response)
