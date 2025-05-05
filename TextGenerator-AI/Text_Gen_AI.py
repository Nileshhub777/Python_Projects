import requests
def fetch_quote():
    try:
        response=requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data=response.json()[0]
            quote=data['q']
            author=data['a']
            print(f"{quote} - {author}")
        else:
            print("Failed to fetch")
            print(response.status_code)
    except requests.exceptions.RequestException as e:(
                print("Network Error :", e))
fetch_quote()