import streamlit as st

import datetime
import plotly.offline as py
import plotly.graph_objs as go
import pandas_datareader as web
import data_file
import parsing 


st.title('Crypto Tracker')
st.markdown("""---""")
col1,col2=st.columns(2)

#crypto_result = st.radio("Coins", ("Bitcoin","Ethereum","Dogecoin","Tether"))
col1, col2, col3,col4,col5= st.columns(5)
with col1:
    bitcoin_true = st.button("Bitcoin", "0")
with col2:
    ethereum_true = st.button("Ethereum", "0")
with col3:
    dogecoin_true = st.button("Dogecoin", "0")
with col4:
    tether_true = st.button("Tether", "0")


#testing=st.markdown("""<button type="button" value="123">Click Me!</button>""",unsafe_allow_html=True)
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #22333b;
    transition: 0.2s;
    padding: 15px 28px;
    border-radius: 24px;
    
}
div.stButton button:hover {
    background-color: #314b57;
    color: #00000
    border-color:#00000
}
div.stButton button:active {
    background-color: #22333b;
    color: #00000
    border-color:#00000
}
</style>""", unsafe_allow_html=True)





#st.write(crypto_result)

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2025, 1, 1)

BTC = web.DataReader('BTC-USD', 'yahoo', start, end)
ETH = web.DataReader('ETH-USD', 'yahoo', start, end)
DOGE = web.DataReader('DOGE-USD', 'yahoo', start, end)
TETHER = web.DataReader('USDT-USD', 'yahoo', start, end)





trace = go.Ohlc(
    x=BTC.index[:],
    open=BTC['Open'],
    high=BTC['High'],
    low=BTC['Low'],
    close=BTC['Close'],
    name='BTC',
    increasing=dict(line=dict(color='green')),
    decreasing=dict(line=dict(color='red')),
)

trace2 = go.Ohlc(
    x=ETH.index[:],
    open=ETH['Open'],
    high=ETH['High'],
    low=ETH['Low'],
    close=ETH['Close'],
    name='ETH',
    increasing=dict(line=dict(color='black')),
    decreasing=dict(line=dict(color='red')),
)

trace3 = go.Ohlc(
    x=DOGE.index[:],
    open=DOGE['Open'],
    high=DOGE['High'],
    low=DOGE['Low'],
    close=DOGE['Close'],
    name='DOGE',
    increasing=dict(line=dict(color='purple')),
    decreasing=dict(line=dict(color='pink')),
)

trace4 = go.Ohlc(
    x=TETHER.index[:],
    open=TETHER['Open'],
    high=TETHER['High'],
    low=TETHER['Low'],
    close=TETHER['Close'],
    name='TETHER',
    increasing=dict(line=dict(color='blue')),
    decreasing=dict(line=dict(color='yellow')),
)

data = [trace]
layout = {
    'title': 'BTC - Bitcoin',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

data2 = [trace2]
layout2 = {
    'title': 'ETH - ETHEREUM',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

data3 = [trace3]
layout3 = {
    'title': 'DOGE - DOGECOIN',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

data4 = [trace4]
layout4 = {
    'title': 'USDT - TETHER',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

fig = dict(data=data, layout=layout)

col_1,col_2,col_3,col_4,col_5=st.columns(5)
crypto_result='bitcoin'
with col_2:
    if bitcoin_true:
        fig = dict(data=data, layout=layout)
        crypto_result='bitcoin'
    elif ethereum_true:
        fig = dict(data=data2, layout=layout2)
        crypto_result='ethereum'
    elif dogecoin_true:
        fig = dict(data=data3, layout=layout3)
        crypto_result='dogecoin'
    elif tether_true:
        fig = dict(data=data4, layout=layout4)
        crypto_result='tether'
    st.plotly_chart(fig)
    with col_1:
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        data_file.coinInfo(crypto_result)




m = st.markdown("""<style>
.stTextInput>div>div>input {
    background-color: #22333b;
    transition: 0.2s;  
}
.stTextInput>div>div>input:hover{
    background-color: #314b57;
     
}
</style>""", unsafe_allow_html=True)

command = st.text_input('Search') 
parsing.getCommand(command)
st.write()