# BinanceData
To make the BinanceData.py function:
Change the 'publicKey' and 'privateKey' in Client on line 8 to your Binance API keys. 

Note:
Currently only gets the 4h candles, later on I will add more functionality. It returns a pandas DataFrame of the OHCLV in chronological order (latest to newest).

# BinanceAlert and run.py
To make BinanceAlertV3.py function:
Change the 'publicKey' and 'privateKey' in Client and altClient on lines 19, 22, 593 and 594 to your Binance API keys.
altClient might not be necessary if you change some settings, but I use it to make sure it won't stop because it is exceeding the max requests.
run.py is necessary if you want to run it on Linux, which is what I am currently doing. 

# BinanceAlert use cases
BinanceAlert provides alerts on the USDT pairs. These alerts are based on multiple factors, such as technical analysis, new listings on Binance and changes in your stop-loss.

Note:
Currently BinanceAlert only support the USDT pairs, adding BTC pairs might be done later.
