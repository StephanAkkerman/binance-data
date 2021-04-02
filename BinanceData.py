import numpy as np
import pandas as pd
import math
from datetime import datetime
from binance.client import Client

# Change these values to your Binance API keys, keep it as a string
client = Client(api_key = 'publicKey', api_secret = 'privateKey')

# For instance:
# Symbol = 'BTCUSDT'    (string)
# Days = 1000           (int)
def fetch4Hour(symbol, days):
    # https://python-binance.readthedocs.io/en/latest/binance.html#binance.client.Client.get_klines

    candleList = []
    hrs = 4

    # Time Now
    end = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_4HOUR)[-1][0]

    # Time is in ms
    diff = hrs * 3600000 
    
    # Specify how long the loop should last
    maxDays = days
    # Round up
    daysPerLoop = math.ceil(maxDays / (hrs * 500 / 24))
    #print(daysPerLoop)

    # Get as much data as possible
    for x in range(daysPerLoop):
        # Make the list from oldest to newest
        candleList = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_4HOUR, endTime = end) + candleList
        end =  end - diff * 500

    #print(candleList)
    #print("Done")
    df = pd.DataFrame(candleList)

    # Keep OHLCV data
    df.drop(columns = [6,7,8,9,10,11],axis=1,inplace=True)
    df.columns = ["date", "open", "high", "low", "close", "volume"]  

    # Conver time in ms to datetime
    df['date'] = pd.to_datetime(df['date'], unit='ms')

    df['open'] = pd.to_numeric(df['open'])
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])
    df['volume'] = pd.to_numeric(df['volume'])

    # Volume in USDT
    df['volume'] = df.volume * df.close

    return df

    #Convert to csv file
    #df.to_csv(r' FILE LOCATION ',index=False)
