import pandas as pd
from binance import Client
from datetime import datetime as dt
import pandas_ta as ta


client =Client(None,None)

def calculate_time(number):
    return dt.fromtimestamp(open_time.iloc[number] / 1000)

titles=["Open Time","Open","High","Low","Close","Volume","Close Time","QAV","NAT","TBBAV","TBQAV","ignore"]

df = pd.read_csv("NEARUSDT5MIN.csv", names=titles)

open_level = df["Open"]
close_level = df["Close"]
high_level = df["High"]
low_level = df["Low"]
open_time = df["Open Time"]

rsi = ta.rsi(close=close_level,length=14)

def fibo():
    max_value= 0
    min_value = 1000000
    for i in range(len(close_level)-500,len(close_level)):
        if max_value < close_level[i]:
            max_value=close_level[i]

        if min_value > close_level[i]:
            min_value = close_level[i]


    first = (max_value-min_value)*0.236 + min_value
    second = (max_value-min_value)*0.382 + min_value
    third= (max_value-min_value)*0.5 + min_value
    forth= (max_value-min_value)*0.618 + min_value
    fifth =(max_value-min_value)*0.786 + min_value

    values = list()

    values.append(first)
    values.append(second)
    values.append(third)
    values.append(forth)
    values.append(fifth)

    return values
fibo()

def pivot():
    max_value = 0
    min_value = 10000
    close_value = 0

    day_number = 0
    for i in range(len(close_level)-30,len(close_level)):
        if calculate_time(i).hour == 3 :
            day_number = i

    for j in range(1, 25):
        if max_value < high_level[day_number-j]:
            max_value = high_level[day_number-j]
        if min_value > low_level[day_number-j]:
            min_value = low_level[day_number-j]
        if j == 1:
            close_value = close_level[day_number - j]

    High = max_value
    Low = min_value
    Close=close_value


    PP = (High + Low + Close) / 3
    R1 = 2 * PP - Low
    S1 = 2 * PP - High
    R2 = PP + (High - Low)
    S2 = PP - (High - Low)
    R3 = 2*PP +  (High - 2*Low)
    S3 = 2*PP - (2*High - Low)
    R4 = 3*PP + (High-3*Low)
    S4 =3*PP -(3*High-Low)
    R5 = 4*PP + (High-4*Low)
    S5 = 4 * PP - (4 * High - Low)

    values = list()
    values.append(PP)
    values.append(R1)
    values.append(R2)
    values.append(R3)
    values.append(R4)
    values.append(R5)
    values.append(S1)
    values.append(S2)
    values.append(S3)
    values.append(S4)
    values.append(S5)


    return values

pivot()