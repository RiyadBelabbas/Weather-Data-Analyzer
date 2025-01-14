import requests

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    with open("api_key.txt", "r") as file:
        api_key = file.read().strip()
    city = input("Entrez le nom de la ville : ")
    print(get_weather_data(city, api_key))

