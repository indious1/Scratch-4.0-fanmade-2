import urllib.request
import requests

def get_profile_information(username):
  api_url = f"https://erichsu903.pythonanywhere.com/api?get=https://api.scratch.mit.edu/users/{username}"
  size = "90x90"
  try:
    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()
    #print(data)
    pfp_url = data['profile']['images'][size]

    urllib.request.urlretrieve(pfp_url, f"PFP_s{username}.png")
  except requests.exceptions.RequestException as e:
    print("Error, user may not exist or rate limits :/")
    return "User not found"

get_profile_information("scratchthecoder12345")
