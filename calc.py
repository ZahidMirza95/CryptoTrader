import datetime
import json
import requests
import os
import streamlit as st
import variables

class Client(object):

    token = os.environ.get('SOR_TOKEN',"6c634e1eacecc4801b000249287fbf923d5c8824") # coinroutes portal API token

    url = 'https://staging.coinroutes.com/api/cost_calculator/'

    def __init__(self):

        self.session = requests.Session()
        self.session.headers = self.get_headers()
        #print(self.session.headers)

    def get_headers(self):
        return {'Authorization': 'Token {}'.format(self.token)}


    def run(self):
        global pair
        req = {
        "currency_pair": pair,  # currency pair to get prices for
        "exchanges": variables.exchangesList,  # exchanges to include in the cost calculation
        "side": side,  # "asks" is for the buy price, "bids" is for the sell price
        "quantity": variables.pairQuantity,  # quantity of the target currency to get the price for
        "levels": 1000,  # number of price levels to consider.  Defaults to 1000 which is sufficient for most use cases

        # This is the name of the strategy to use for calculating available balances
        # Must be specified if use_balances = True.
        #  Strategies can be found at https://portal.coinroutes.com/api/strategies/
        "strategy": None,
        # Should available Balances be used to calculate the effective price?
        #  This will limit exchange selection to exchanges with balances on the specified strategy
        "use_balances": False,
        'order_type': 'ioc',
        'use_funding_currency': False

        }

        # "asks" is to get the buy price
        req['side'] = "asks"

        asks_response = requests.post(self.url, json=req, headers=self.get_headers())
        asks_data = asks_response.json()

        # "bids" is to get the sell price
        req['side'] = 'bids'
        bids_response =  requests.post(self.url, json=req, headers=self.get_headers())

        bids_data = bids_response.json()

        buy_avg_price = asks_data.get('best_average_price')  # This is the effective price per coin without fees
        buy_first_price = asks_data.get('first_price') # this is the first price in the consolidated order book
        buy_cost = buy_avg_price - buy_first_price


        sell_avg_price = bids_data.get('best_average_price')
        sell_first_price = bids_data.get('first_price')
        sell_cost = sell_first_price - sell_avg_price

        st.write("Buy Cost: {} Sell Cost: {}".format(buy_cost, sell_cost))
        st.write("Exchanges: {}".format(variables.exchangesList))
        st.write("Quantity: {}".format(variables.pairQuantity))
        st.write("Side: {}".format(side))

side='asks'
pair = 'BTC-USD'
def initRun():
    c = Client()
    c.run()