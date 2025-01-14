def process_weather_data(weather_data):
    # Exemple de traitement des données météorologiques
    processed_data = {
        "temperature": weather_data.get("temp"),
        "humidity": weather_data.get("humidity"),
        "pressure": weather_data.get("pressure"),
    }
    return processed_data


if __name__ == "__main__":
    sample_data = {
        "main": {"temp": 15.5, "humidity": 80, "pressure": 1012},
        "name": "Paris",
    }
    print(process_weather_data(sample_data))
