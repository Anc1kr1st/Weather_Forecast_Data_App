import requests

API_KEY = "4873e6eeced11b43bfb23ae28e1e1bd3"


def get_data(place, forecast_days=None, kind_of_weather=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind_of_weather == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind_of_weather == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo"))