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
    import matplotlib.pyplot as plt
    import yfinance as yf

    # Calculate equity curve
    equity = (1 + data['StrategyReturns']).cumprod()

    # Fetch company name
    ticker_obj = yf.Ticker(ticker)
    name = ticker_obj.info.get('longName', ticker)  # fallback to ticker

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # --- Subplot 1: Close Price ---
    ax1.plot(data.index, data['Close'])
    ax1.set_title(f"{name} — Close Price")
    ax1.set_ylabel("Price")

    # --- Subplot 2: Equity Curve ---
    ax2.plot(data.index, equity)
    ax2.set_title(f"{name} — RSI Strategy Equity Curve")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Equity")

    plt.tight_layout()
    plt.show()
