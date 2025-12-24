import requests

steam_id = "YOUR_STEAM_USER_ID"
steam_api_key = "YOUR_STEAM_WEB_API_KEY"
deal_api_key = "YOUR_ISTHEREANYDEAL_API_KEY"

# Get list of the games currently in my Steam wishlist
wishlist_response = requests.get("https://api.steampowered.com/IWishlistService/GetWishlist/v1/", 
                        params={
                            "steamid": steam_id,
                            "key": steam_api_key
                        })

# Parse the json response into a list of Steam game ID's
game_data = wishlist_response.json()["response"]["items"]

# Initiate empty lists and dicts
game_list = []
payload = []
lowest_price_games = {}

# Create a list of Steam game ID's formatted for the IsThereADeal API
for game in game_data:
    game_list.append(f"app/{game['appid']}")

# Get the IsThereADeal game ID for each Steam game ID
get_itad_game_id = requests.post(f"https://api.isthereanydeal.com/lookup/id/shop/{61}/v1",
                                 json=game_list,
                                 params={
                                     "key": deal_api_key
                                 })

# Append the IsThereADeal game ID to the payload variable
for value in get_itad_game_id.json().values():
    payload.append(value)

# Make a POST request to the IsThereADeal API to get the current prices for each game in the Steam UK Store
game_price_response = requests.post("https://api.isthereanydeal.com/games/prices/v3",
                                   json=payload, 
                                   params={
                                       "key": deal_api_key,
                                       "country": "GB",
                                       "shops": 61,
                                   })

# Parse the json reponse to access the current game price and historic lowest price, compare prices,
# add to the lowest_price_games dictionary if price is at or equal to lowest
for item in game_price_response.json():
    current_price = item["deals"][0]["price"]["amount"]
    history_low = item.get("historyLow")
    if history_low and history_low.get("all"):
        historic_lowest_price = history_low["all"]["amount"]
        if current_price <= historic_lowest_price:
            lowest_price_games[item["id"]] = current_price
    else:
        historic_lowest_price = None

print("\nHere are the games in your Steam Wishlist with historically low prices:\n")

# Get the game title from the IsThereADeal API and print title and price
for key in lowest_price_games:
    game_title_response = requests.get("https://api.isthereanydeal.com/games/info/v2",
                                       params={
                                           "key": deal_api_key,
                                           "id": key
                                       })
    print(f"{game_title_response.json()["title"]} - £{lowest_price_games[key]}")

print("\n")
