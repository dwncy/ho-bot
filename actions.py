# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetTodayHoroscope(Action):
    def name(self) -> Text:
        return "action_get_today_horoscope"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_horoscope_sign = tracker.get_slot('horoscope_sign')

        if (user_horoscope_sign == "sagitarius"):
            user_horoscope_sign = "sagittarius"

        base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
        url = base_url.format(**{ 'day': "today", 'sign': user_horoscope_sign })
        # http://horoscope-api.herokuapp.com/horoscope/today/capricorn
        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = "Today's horoscope:\n{}".format(todays_horoscope)
        dispatcher.utter_message(response)
        return [SlotSet("horoscope_sign", user_horoscope_sign)]
