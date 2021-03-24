# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionWeather(Action):

	def name(self) -> Text:
		return "action_weather"

	def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		api_key = "f17d4608e53f78034c591d1c799b9523"
		base_url = "https://api.openweathermap.org/data/2.5/weather?"
		location = str(tracker.get_slot('location'))
		final_url = base_url + "q=" + location + "&units=metric&APPID=" + api_key
		weather_data = requests.get(final_url).json()
	
		if(len(weather_data)>2):
			current_temperature = weather_data["main"]["temp"]
			atm_pressure = weather_data["main"]["pressure"]
			humidity = weather_data["main"]["humidity"]
			wind_speed = weather_data["wind"]["speed"]
	    
			response = """It is {} degrees Celcius at {} right now. Besides the humidity is {}%, atmospheric pressure {}hPa and wind speed is {}m/s.""".format(current_temperature, location, humidity, atm_pressure, wind_speed)
			dispatcher.utter_message(response)


		else:
			dispatcher.utter_message("Are you sure that's the correct name of the city?")
	    

		return [SlotSet("location")]


