# BinanceData
**To make the BinanceData.py function:** \
Change the 'publicKey' and 'privateKey' in Client on line 8 to your Binance API keys. 

How to use:
- Add the BinanceData.py to same directory you're working in.
- Write: from BinanceData import fetchData
- To get the latest daily data on the BTCUSDT pair, write: fetchData(symbol="BTCUSDT", amount=1, timeframe='1d')

**Note: The volume is converted to USDT in this example, volume will always be converted to the second coin in a pair.**

# BinanceAlert and run.py
**To make BinanceAlertV3.py function:** \
- Change the 'publicKey' and 'privateKey' in Client and altClient on lines 19, 22, 593 and 594 to your Binance API keys.
- altClient might not be necessary if you change some settings, but I use it to make sure it won't stop because it is exceeding the max requests.
- run.py is necessary if you want to run it on Linux, which is what I am currently doing. 

# BinanceAlert use cases
BinanceAlert provides alerts on the USDT pairs. These alerts are based on multiple factors, such as technical analysis, new listings on Binance and changes in your stop-loss.

**Note: Currently BinanceAlert only support the USDT pairs, adding BTC pairs might be done later.**
