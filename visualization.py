import matplotlib.pyplot as plt

def plot_temperature(data):
    days = [item["day"] for item in data]
    temperatures = [item["temperature"] for item in data]

    plt.figure(figsize=(10, 6))
    plt.plot(days, temperatures, marker="o", color="blue", label="Température (°C)")
    plt.title("Évolution des températures")
    plt.xlabel("Jour")
    plt.ylabel("Température (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    sample_data = [
        {"day": "Lundi", "temperature": 12},
        {"day": "Mardi", "temperature": 14},
        {"day": "Mercredi", "temperature": 15},
    ]
    plot_temperature(sample_data)
