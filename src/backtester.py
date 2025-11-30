# what it does:

import pandas as pd

def backtest_rsi(data):
    
    # create a new column in data (Position) to represent if I am holding the asset (=1), or not (=0)
    data['Position'] = 0

    # Goes through data and says we would have bought when RSI < 30, and sold when RSI > 70.
    for i in range(len(data)):
        if data['RSI'].iloc[i] < 30:
            # buy
            data['Position'].iloc[i] = 1
        elif data['RSI'].iloc[i] > 70:
            # sell
            data['Position'].iloc[i] = 0
        else:
            # keep previous position
            data['Position'].iloc[i] = data['Position'].iloc[i-1]

    # Add column for Daily returns to data
    data['Return'] = data['Close'].pct_change()
    data['StrategyReturns'] = data['Position'] * data['Return']

    return data
