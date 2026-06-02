import requests


BASE_URL = "http://127.0.0.1:8000/api/parking-spots/"


valid_data = {
    "number": "A-01",
    "zone": "Центральная зона",
    "address": "ул. Ленина, 10",
    "latitude": "55.755800",
    "longitude": "37.617300",
    "spot_type": "regular",
    "status": "free"
}


data = {
    "number": "A-03",
    "zone": "Центральная зона",
    "address": "ул. Ленина, 12",
    "latitude": "155.855800",
    "longitude": "37.717300",
    "spot_type": "regular",
    "status": "free"
}

data2 = {
    "status": "occupied"
}



def print_response(response):
    print("Статус:", response.status_code)

    try:
        print(response.json())
    except Exception:
        print(response.text)


print("Создание корректного парковочного места:")
'''response = requests.post(BASE_URL, json=valid_data)
print_response(response)'''

print("\nОтправка некорректной широты:")
response = requests.post(BASE_URL, json=invalid_data)
print_response(response)