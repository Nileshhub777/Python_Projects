import requests
def fetch_quote():
    response=requests.get("https://zenquotes.io/api/random")

    if response.status_code == 200:

        #print(response.json())
        data=response.json()[0]
        #print(data)
        quote=data['q']
        author=data['a']
        print(f"{quote} - {author}")
    else:
        print("Failed to fetch")
        print(response.status_code)
fetch_quote()