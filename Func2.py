import requests
from pyfiglet import Figlet
import os, time
def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

def weird_weather_bot():
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))
    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    name = input("May I take your first name please? ")
    gender_result = guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")
weird_weather_bot()

def postcode(): 
    postcode_raw = input("\nSo, what's your postcode? ")
    if postcode_raw == '':
        print("Please enter a postcode")
        postcode() 
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")
    return area, longitude, latitude
postcode()

def ellipsis():
    a = "" 
    for i in range(3):
        time.sleep(1)
        a = a + ("...\n") 
    return a
ellipsis()

def CatFact(): 
    spaces = ellipsis()
    print(spaces)
    UI = input("\nWould you like a cat fact while you wait? ")
    if UI.casefold() in ['n', 'no', 'nah']:
        print("Everyone likes cat facts now come on")
    else: 
        print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")
    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")
    print(spaces)
CatFact()

def GetWeather():
    x = postcode()
    area = x[0]
    longitude = x[1]
    latitude = x[2]
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    weather_kelvin = weather_resp["main"]["temp"]
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")
GetWeather() 
