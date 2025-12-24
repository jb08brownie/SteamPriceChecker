# Steam Wishlist Historical Low Price Checker

A Python script that checks your **Steam wishlist** and identifies which games are currently selling at their **historically lowest recorded price** on Steam, using price data from IsThereAnyDeal.

This helps during the many Steam seasonal sales to get the *best price for your most wanted games.*

---

## 🚀 What This Project Does

1. Fetches your Steam wishlist using the **Steam Web API**
2. Converts Steam App IDs to IsThereAnyDeal game IDs
3. Retrieves current prices from the Steam store (set to UK but can be changed using the ISO 3166-1 alpha-2 for your country)
4. Compares current prices with historical lowest prices
5. Prints only the games that are **at or below their all-time low**

---

## 🔌 APIs Used

- **Steam Web API** – Accesses your Steam wishlist
  API Key can obtained here: https://steamcommunity.com/dev/apikey
- **IsThereAnyDeal API** – Provides price history and current pricing data
  API Key can be obatined by creating an account here: https://isthereanydeal.com/

---

## 💻 How To Use

- Obtain your Steam User ID No. by following:
  1. In the Steam Desktop App click the Steam button (top left)
  2. Click Settings
  3. Go to Account Details in the Account tab
  4. Your Steam ID will be shown in grey underneath account header at the top
- Fill in your Steam ID, Steam Web API Key, IsThereAnyDeal API Key for the variables at the top of the script
- Run the script in the terminal, for example in Windows, use the following command:
```bash
python steam_price_checker.py
```
- Output Example
```
Here are the games in your Steam Wishlist with historically low prices:

Tex Murphy: Under a Killing Moon - £1.04
Pony Island - £0.64
Sam & Max Beyond Time and Space - £7.74
```
