import requests # will need
import os
import threading
import pycoingecko as pcg
from datetime import datetime # might need
from pandas import DataFrame as df # will need
import streamlit as st
import calc
import variables

#coinRoute = requests.post('https://portal.coinroutes.com/api/cost_calculator/', headers={'Authorization':'TOKEN 6c634e1eacecc4801b000249287fbf923d5c8824'})
gecko = pcg.CoinGeckoAPI()


#View all coins
#print(gecko.get_coins_list())
def checkPair(pairs):
    for pair in pairs:
        calc.pair = pair
        calc.initRun()

def watch(id):
    threading.Timer(3, watch, [id]).start()
    cls = lambda: os.system('cls')
    cls()
    coinInfo(id)

def searchCoin(coins, currency):
    variables.activeCoins=[]
    for id in coins:
        coin = gecko.get_coin_by_id(id)
        price = gecko.get_price(ids=id, vs_currencies=currency)
        st.write(id.capitalize())
        st.write('$' + str(price[id][currency]))
        st.write('------------')

def coinInfo(id):
    coin = gecko.get_coin_by_id(id)
    st.write('Market Cap Rank:', coin['market_cap_rank'])
    st.write('Symbol:', coin['symbol'])
    st.write('Current Value:', '$' + str(coin['market_data']['current_price']['usd']))

#View fields of coin
#coin = gecko.get_coin_by_id('bitcoin')
#for field in coin:
#    print(field)

#print(coin['market_data'])
#print(coin['tickers'])
#for field in coin['tickers']:
#    print(field)