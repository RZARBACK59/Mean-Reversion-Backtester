# what it does:

import pandas as pd

def backtest_rsi(data):
    
    # create a new column in data (Position) to represent if I am holding the asset (=1), or not (=0)
    data['Position'] = 0

    # Goes through data and says we would have bought when RSI < 30, and sold when RSI > 70.
    for i in range(len(data)):
        # Need to deal with the NaN's at the start, assume position is 0
        if pd.isna(data['RSI'].iloc[i]):
            data.loc[data.index[i], 'Position'] = 0
            continue

        if data['RSI'].iloc[i] < 30:
            # Buy
            data.loc[data.index[i], 'Position'] = 1
        elif data['RSI'].iloc[i] > 70:
            # Sell
            data.loc[data.index[i], 'Position'] = 0
        else:
            # Hold position
            data.loc[data.index[i], 'Position'] = data['Position'].iloc[i-1]

    # Add column for daily returns to data
    data['Return'] = data['Close'].pct_change()
    data['StrategyReturns'] = data['Position'] * data['Return']

    return data
