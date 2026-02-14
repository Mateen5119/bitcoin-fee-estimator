import requests
import time

def get_bitcoin_price():
    # Fetch current Bitcoin price in USD
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url).json()
    return response['bitcoin']['usd']

def get_fees():
    # Fetch recommended fees from mempool.space (Standard Bitcoin API)
    url = "https://mempool.space/api/v1/fees/recommended"
    response = requests.get(url).json()
    return response

def main():
    print("--- ⚡ Satoshi Fee Estimator ⚡ ---")
    print("Fetching live data...\n")
    
    try:
        price = get_bitcoin_price()
        fees = get_fees()
        
        print(f"💰 Current BTC Price: ${price:,.2f}")
        print("-" * 30)
        print(f"🚀 High Priority: {fees['fastestFee']} sats/vB")
        print(f"bw Half Hour Fee: {fees['halfHourFee']} sats/vB")
        print(f"🐢 Low Priority:  {fees['hourFee']} sats/vB")
        print("-" * 30)
        
        # Calculate cost for a standard transaction (approx 140 vBytes)
        tx_size = 140
        cost_sats = fees['fastestFee'] * tx_size
        cost_usd = (cost_sats / 100_000_000) * price
        
        print(f"Est. Cost for Standard Tx (Fast): {cost_sats} sats (~${cost_usd:.2f})")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
import requests
import time

def get_bitcoin_price():
    # Fetch current Bitcoin price in USD
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url).json()
    return response['bitcoin']['usd']

def get_fees():
    # Fetch recommended fees from mempool.space (Standard Bitcoin API)
    url = "https://mempool.space/api/v1/fees/recommended"
    response = requests.get(url).json()
    return response

def main():
    print("--- ⚡ Satoshi Fee Estimator ⚡ ---")
    print("Fetching live data...\n")
    
    try:
        price = get_bitcoin_price()
        fees = get_fees()
        
        print(f"💰 Current BTC Price: ${price:,.2f}")
        print("-" * 30)
        print(f"🚀 High Priority: {fees['fastestFee']} sats/vB")
        print(f"bw Half Hour Fee: {fees['halfHourFee']} sats/vB")
        print(f"🐢 Low Priority:  {fees['hourFee']} sats/vB")
        print("-" * 30)
        
        # Calculate cost for a standard transaction (approx 140 vBytes)
        tx_size = 140
        cost_sats = fees['fastestFee'] * tx_size
        cost_usd = (cost_sats / 100_000_000) * price
        
        print(f"Est. Cost for Standard Tx (Fast): {cost_sats} sats (~${cost_usd:.2f})")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()