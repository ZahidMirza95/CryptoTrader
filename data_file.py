import requests # will need
import os
import threading
import pycoingecko as pcg
from datetime import datetime # might need
from pandas import DataFrame as df # will need
import streamlit as st

#coinRoute = requests.post('https://portal.coinroutes.com/api/cost_calculator/', headers={'Authorization':'TOKEN 6c634e1eacecc4801b000249287fbf923d5c8824'})
gecko = pcg.CoinGeckoAPI()

#View all coins
#print(gecko.get_coins_list())

def watch(id):
    threading.Timer(3, watch, [id]).start()
    cls = lambda: os.system('cls')
    cls()
    coinInfo(id)

def searchCoin(coins, currency):
    coin = ""
    for id in coins:
        coin = gecko.get_coin_by_id(id)
        price = gecko.get_price(ids=id, vs_currencies=currency)
    return coin

def coinInfo(id):
    coin = gecko.get_coin_by_id(id)
    st.write('id:', coin['id'])
    st.write('Market Cap Rank:', coin['market_cap_rank'])
    st.write('Symbol:', coin['symbol'])
    st.write('Current Value:', '$' + str(coin['market_data']['current_price']["usd"])) #main.currency
