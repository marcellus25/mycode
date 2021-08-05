
API = "http://api.open-notify.org/astros.json"

import requests

def main():
    resp = requests.get(API)
    spacedata = resp.json()
    print(spacedata)
    print(f"There are currently {spacedata.get('number')} people in space.")
if __name__ == "__main__":
    main()
