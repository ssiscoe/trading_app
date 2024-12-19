import pandas as pd
import numpy as np

def moving_average(data, window):
    """
    Calculate Simple Moving Average (SMA) for a given window period.
    
    Args:
        data (pd.DataFrame): DataFrame with 'price' column
        window (int): Number of periods for the moving average
        
    Returns:
        pd.Series: Moving average values
    """
    if not isinstance(data, pd.DataFrame) or 'price' not in data.columns:
        raise ValueError("Data must be a DataFrame with a 'price' column")
    
    return data['price'].rolling(window=window, min_periods=1).mean()

def rsi(data, window):
    """
    Calculate Relative Strength Index (RSI) for a given window period.
    
    Args:
        data (pd.DataFrame): DataFrame with 'price' column
        window (int): Number of periods for RSI calculation
        
    Returns:
        pd.Series: RSI values
    """
    if not isinstance(data, pd.DataFrame) or 'price' not in data.columns:
        raise ValueError("Data must be a DataFrame with a 'price' column")
    
    # Calculate price changes
    delta = data['price'].diff()
    
    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    # Calculate average gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    
    # Calculate RS and RSI
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    # Handle division by zero
    rsi = rsi.replace([np.inf, -np.inf], np.nan)
    
    return rsi

def bollinger_bands(data, window=20, num_std=2):
    """
    Calculate Bollinger Bands.
    
    Args:
        data (pd.DataFrame): DataFrame with 'price' column
        window (int): Window period for moving average (default: 20)
        num_std (int): Number of standard deviations (default: 2)
        
    Returns:
        tuple: (middle band, upper band, lower band)
    """
    if not isinstance(data, pd.DataFrame) or 'price' not in data.columns:
        raise ValueError("Data must be a DataFrame with a 'price' column")
    
    middle_band = moving_average(data, window)
    std = data['price'].rolling(window=window, min_periods=1).std()
    
    upper_band = middle_band + (std * num_std)
    lower_band = middle_band - (std * num_std)
    
    return middle_band, upper_band, lower_band

if __name__ == "__main__":
    # Sample data for testing
    data = pd.DataFrame({
        "price": [100, 102, 101, 105, 110, 108, 107, 111, 115, 120]
    })
    
    # Test moving average
    print("Moving Average:")
    print(moving_average(data, window=3))
    print("\nRSI:")
    print(rsi(data, window=3))
    print("\nBollinger Bands:")
    middle, upper, lower = bollinger_bands(data, window=3)
    print("Middle Band:", middle)
    print("Upper Band:", upper)
    print("Lower Band:", lower)