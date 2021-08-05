#!/usr/bin/env python3
import requests
api = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
def main():
    character = input ("What pokemon are you looking for? <input bulbasaur>").lower
    resp = requests.get(api)
    poke = resp.json()
    print(poke)
    #print(poke.keys())
if __name__ == "__main__":
    main()

