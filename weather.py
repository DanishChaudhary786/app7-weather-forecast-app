import requests
from CONSTANT import WEATHER_API_KEY


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data = filtered_data[:8 * forecast_days]
    return filtered_data

if __name__ == "__main__":
    print(get_data( place='Mundra',forecast_days=2))