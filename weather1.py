#whether api
import requests
import pyttsx3
import speak as s


def get_weather(api_key, city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Unable to connect to the weather service: {e}"}

# Main weather function
def weather1():
    api_key = '6e2f46defd9f9da17719fc0438ad94e4'  # Replace with your actual API key
    speak("Enter your city name")
    city = input("Enter your city name: ")

    weather_data = get_weather(api_key, city)

    if 'error' in weather_data:
        error_message = weather_data['error']
        s.speak(error_message)
        print(error_message)
    elif weather_data['cod'] == 200:
        # Display and speak the weather details
        details = [
            f"Weather in {city}:",
            f"Temperature: {weather_data['main']['temp']}°C",
            f"Humidity: {weather_data['main']['humidity']}%",
            f"Description: {weather_data['weather'][0]['description']}",
            f"Wind Speed: {weather_data['wind']['speed']} m/s",
        ]
        for detail in details:
            speak(detail)
            print(detail)
    else:
        error_message = "City not found. Please try again."
        s.speak(error_message)
        print(error_message)

# Run the script
if __name__ == "__main__":
    weather1()




