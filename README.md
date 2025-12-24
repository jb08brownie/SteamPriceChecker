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

## Us
