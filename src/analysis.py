# Analyse the strategy and plot it
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def compute_stats(data):
    strat_returns = data['StrategyReturns']

    # Calculate the sharp ratio (risk-adjusted return) for the 252 trading days in a year
    sharpe = np.sqrt(252) * strat_returns.mean() / strat_returns.std()
    # Calculate cumulative returns
    cum_return = (1 + strat_returns).prod() - 1
    # Calculate rolling maximum cumulative return (i.e. the best its been up until that date)
    roll_max = (1 + strat_returns).cumprod().cummax()
    # Calculate how far the price has fallen since its most recent peak
    drawdown = (1 + strat_returns).cumprod() / roll_max - 1
    # Find the maximum drawdown (the lowest its fallen ever)
    max_dd = drawdown.min()

    return {
        "Sharpe": sharpe,
        "Total Return": cum_return,
        "Max Drawdown": max_dd
    }

def plot_equity_curve(data, ticker):
    # Calculates equity (the value of our holdings)
    equity = (1 + data['StrategyReturns']).cumprod()

    # fetches the company's name (for the graph)
    ticker_obj = yf.Ticker(ticker)
    name = ticker_obj.info['longName']  # or 'shortName'

    # plot graph
    plt.figure(figsize=(10,5))
    plt.plot(equity)
    plt.title(f"RSI Strategy Equity Curve [{name}]")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.show()
