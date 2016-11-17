import numpy as np
import pandas as pd

def main():
    do_exercise()

def do_exercise():
    # 1
    aapl_bars = pd.read_csv("./AAPL.csv")
    
    # 2
    date_index = aapl_bars["Date"]
    
    # 3
    aapl_bars.index = pd.to_datetime(date_index)
    
    # 4
    open_column = aapl_bars["Open"]
    close_column = aapl_bars["Close"]
    volume_column = aapl_bars["Volume"]
    
    #5
    df_dict = {"Open": open_column, "Close": close_column, "Volume": volume_column}
    df = pd.DataFrame(df_dict)[:]["1989": "2003-04"]
    
    return df

if __name__ == "__main__":
    main()
