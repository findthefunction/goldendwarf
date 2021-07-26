## Scraper

### Binance API
Scraper pulls binance minute signals with 'open_time','open', 'high', 'low', 'close', 'volume', 'close_time', 'quote average volume', 'num_trades',
'taker_base_vol', 'taker_quote_vol', 'ignore' data cloumns.
This file will be exprted as a script and run at a specific interval to update dataset
These datasets will then have their features reduced prior to loading in RRN model for analysis.
