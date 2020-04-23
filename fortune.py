import random
import json
from colorama import Fore

def fortune():
    try:
        json_file = open('fortunes.json')
    except:
        print(Fore.RED, "File not found!")
        return
    json_data = json.load(json_file)
    fortunes = json_data['data']
    x = random.randrange(2335)
    print("\"", fortunes[x]['quote'],"\"")
    print(" - ",fortunes[x]['author'])
    