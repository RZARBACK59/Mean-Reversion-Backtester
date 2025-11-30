# run all the functions

from src.data_loader import get_data
from src.indicators import compute_rsi
from src.backtester import backtest_rsi
from src.analysis import compute_stats, plot_equity_curve

data = get_data("SPY")
data = compute_rsi(data)
data = backtest_rsi(data)

stats = compute_stats(data)
print(stats)

plot_equity_curve(data)