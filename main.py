from api import get_weather_data
from data_processing import process_weather_data
from visualization import plot_temperature
from storage import save_to_csv, load_from_csv

def main():
    city = input("Entrez le nom de la ville : ")
    with open("api_key.txt", "r") as file:
        api_key = file.read().strip()
    
    weather_data = get_weather_data(city, api_key)
    processed_data = process_weather_data(weather_data)
    
    print("Données traitées :", processed_data)
    save_to_csv([processed_data], "weather_data/weather_data.csv")
    loaded_data = load_from_csv("weather_data/weather_data.csv")
    
    plot_temperature([{"day": city, "temperature": processed_data["temperature"]}])

if __name__ == "__main__":
    main()
