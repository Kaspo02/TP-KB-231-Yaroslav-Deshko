import requests


BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode="


while True:
    cc = input("Введіть код валюти (USD, EUR, JPY або інший): ")

    r = requests.get(BASE_URL + cc + "&json")

    if r.json() == []:
        print("Неправильний код валюти!")
    else:
        m = float(input("Введіть суму для конвертації: "))
        print(f"Валюта: {r.json()[0]["txt"]}. Курс: {r.json()[0]["rate"]} UAH")
        print(cc.upper() + " -> " + "UAH: " + f"{(m * float(r.json()[0]['rate'])):.2f}")