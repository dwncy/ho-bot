## bye
* bye
  - utter_bye

## straight ask my horoscope
* ask_horoscope
  - utter_ask_horoscope_sign
* ask_horoscope{"horoscope_sign": "leo"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "leo"}

## straight ask my horoscope with out of scope
* ask_horoscope
  - utter_ask_horoscope_sign
* out_of_scope
  - utter_default
* ask_horoscope{"horoscope_sign": "leo"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "leo"}

## straight ask my horoscope with many out of scope
* ask_horoscope
  - utter_ask_horoscope_sign
* out_of_scope
  - utter_default
* ask_horoscope{"horoscope_sign": "leo"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "leo"}
* out_of_scope
  - utter_default

## straight ask another horoscope
* ask_horoscope{"horoscope_sign": "taurus"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "taurus"}

## dont know the horoscope
* greeting
  - utter_greet
* ask_horoscope
  - utter_ask_horoscope_sign
* ask_horoscope{"horoscope_sign": "leo"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "leo"}

## my horoscope again and again
* greeting
  - utter_greet
* ask_horoscope
  - utter_ask_horoscope_sign
* ask_horoscope{"horoscope_sign": "leo"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "leo"}
* ask_horoscope{"horoscope_sign": "leo"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "leo"}

## ask another horoscope
* greeting
  - utter_greet
* ask_horoscope{"horoscope_sign": "sagittarius"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "sagittarius"}

## ask another another horoscope
* greeting
  - utter_greet
* ask_horoscope{"horoscope_sign": "sagittarius"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "sagittarius"}
* ask_horoscope{"horoscope_sign": "gemini"}
  - action_get_today_horoscope
  - slot{"horoscope_sign": "gemini"}

## Generated Story -328971043333018329
* greeting
    - utter_greet
* ask_horoscope
    - utter_ask_horoscope_sign
* ask_horoscope{"horoscope_sign": "leo"}
    - slot{"horoscope_sign": "leo"}
    - action_get_today_horoscope
* ask_horoscope{"horoscope_sign": "gemini"}
    - slot{"horoscope_sign": "gemini"}
    - action_get_today_horoscope
* bye
    - utter_bye
* greeting
    - utter_greet
* ask_horoscope{"horoscope_sign": "pisces"}
    - slot{"horoscope_sign": "pisces"}
    - action_get_today_horoscope
* ask_horoscope{"horoscope_sign": "aquarius"}
    - slot{"horoscope_sign": "aquarius"}
    - action_get_today_horoscope

## Generated Story -8989125444275848818
* out_of_scope
    - utter_default


