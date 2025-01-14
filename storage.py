import csv

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def load_from_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == "__main__":
    data = [
        {"day": "Lundi", "temperature": 12, "humidity": 80},
        {"day": "Mardi", "temperature": 14, "humidity": 75},
    ]
    save_to_csv(data, "weather_data/weather_data.csv")
    print(load_from_csv("weather_data/weather_data.csv"))
