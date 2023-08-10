# Binance Data

> **note**
> I have made an improved version that supports more exchanges (including Binance), you can find that repository [here](https://github.com/StephanAkkerman/crypto-ohlcv).

binance-data is a simple Python script that lets you fetch data using their API. You don't need to have an account to make this work.
Using `fetchData(symbol, amount, timeframe, as_csv, file_name)` returns a Pandas DataFrame readible by TensorTrade consisting of the most up to date data of Binance.

## How to use
- Add the `data.py` to same directory you're working in.
- Write: `from data import fetchData`.
- To get the latest 500 daily data points of OHLCV on the BTCUSDT pair, write: `fetchData(symbol="BTCUSDT", amount=1, timeframe='1d')`
- To save the data as a .csv file you can write: `fetchData(symbol="BTCUSDT", amount=1, timeframe='1d', as_csv=True)` this will save the DataFrame as BTCUSDT_1d.csv, if you would like a different name you can use the `file_name` parameter.

## Arguments
### Symbol
Symbol can be any pair availble on Binance. 

### Amount
Amount is the amount of rows you would like to have returned times 500, so amount=2 will return 1000 rows. 

### Timeframe
Supported time frames are: '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'.

## Note
The volume is converted to USDT in this example, volume will always be converted to the second coin in a pair.

## Different exchange?
If you need another exchange for some reason, check out: https://github.com/StephanAkkerman/Crypto_OHLCV. It functions the same as this script, but there are more exchanges available.
