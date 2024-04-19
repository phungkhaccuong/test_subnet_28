import numpy as np
import yfinance as yf


def predict() -> float:
    """
    Predicting the next 6 candles using the last close
    """
    last_close = yf.Ticker('^GSPC').history(period='1s')['Close'].iloc[-1]
    df = yf.download('^GSPC', period='10m', interval='5m')
    diff = -(last_close - df.iloc[-1]['Close']) * 0.1
    diff_array = np.array([diff, -diff, diff, -diff, diff, -diff])
    pred_array = np.array([last_close for i in range(6)]) + diff_array
    return np.array([pred_array])


if __name__ == "__main__":
    print(f'prediction: {predict()}')