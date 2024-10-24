import requests

def get_pos():
    base_url = "http://192.168.100.11:2011"
    response = requests.get(f"{base_url}/pos")
    x = response.json()["pos"]["x"]
    y = response.json()["pos"]["y"]
    return f"x: {x}, y: {y}"
