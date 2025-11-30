# what it does: calculates RSI and adds it to data

import pandas as pd

def compute_rsi(data, period=14):
    # price changes from one day to the next
    delta = data['Close'].diff()

    # positive gains (up days)
    up = delta.clip(lower=0)

    # negative losses (down days turned positive)
    down = -1 * delta.clip(upper=0)

    # calculates the rolling averages of gains/losses (from past two weeks)
    ma_up = up.rolling(period).mean()
    ma_down = down.rolling(period).mean()

    # Calculate RSI = 100 - (100/(1 + RS)), where RS = avg-up / avg-down
    rsi = 100 - (100 / (1 + ma_up / ma_down))

    # add RSI column to the dataframe
    data['RSI'] = rsi

    return data
