# Mean-Reversion-Backtester

## What it does
This is a (very) simple script that tries to implement a trading strategy over the past 10 years of data (start of 2015 until now). This strategy uses an indicator called RSI (relative strength index), which is a momentum indicator used to detect if a stock is overbought or oversold. It is calculated by the following equation:

RSI = 100 - (100 / (1 + RS))

where

RS = avg-gain / avg-loss

As you will see in main.py (and the other python files), we first download the data for a specified stock from yahoo finance using get_data(ticker).
We then calculate the RSI over a moving 14 (default) day window, looking at the average gain and losses from the previous 14 days to determine the relative strength for a given day.
We then implement our strategy, looking at the RSI for each day from 01/01/2015 until now, starting from a non-holding position (we don't own any stock) and use the following rule to determine if we should buy, sell, or hold our position:

If RSI < 30 : Buy
If RSI > 70 : Sell
If 30 < RSI < 70: Hold Position 

After stating whether we'd buy or sell (or do nothing) on any given day, we calculate the compounded returns of this strategy.
We then calculate:
Total Returns (the total % gain after 10 years of using this strategy)
Max Drawdown (the most (%) the equity curve fell from it's most recent peak)
Annualised Sharpe Ratio (a metric for risk-adjusted returns, which accounts for its volatility, or, standard deviation) (SQRT(252) * returns / std-deviation)
We then plot two graphs, one showing the returns of our trading strategy over time, and one showing the returns of a 'Buy & Hold' strategy, where you just buy the stock and never sell, and hope it grows.

## Required Packages
Here is a list of the required python packages needed to run this code:
numpy
matplotlib
yfinance
pandas

## Limitations

Simply relying on RSI alone does not work favourably against even a 'Buy & Hold' strategy, as RSI assumes that a stock has an intrinsic value, and deviations from that value are bound to come back. e.g. if a stock was overbought, that would increase share price. RSI believes that people are going to sell this stock due to its increased value, and therefore the stock price will fall back to its intrinsic value. Therefore, the strategy tells us to sell our stock when its being overbought so we don't have to deal with the inevitable decrease in value back to "normal". Similarly, if a stock is oversold, we should buy because the price is lower than it 'should be' therefore we make gains when it inevitably rises again.

This all makes sense in theory, however the assumption that a stock always has an 'intrinsic value' is flawed. As companies grow or decline, the value of said company is also bound to change. Therefore, a share price increasing quickly may not always be an indicator of people overbuying the stock, but just that the company is growing quickly. (e.g. if Nvidia announce a new cutting-edge processor and people buy the stock after seeing the company's growth and future success, that's not an indicator that the price will fall again back to where it was. The company is just becoming more valuable).

An ideal hypothetical example for where this strategy would work would be a stock that had 0% change over the last 10 years, but had a good amount of daily/weekly/monthly volatility. RSI would pick up on when the stock is 'cheap' and when its overvalued, and buy and sell accordingly to make profit. However, no company in the real world is like this, therefore to make our trading strategy more sofisticated, we must consider other metrics in tandem.