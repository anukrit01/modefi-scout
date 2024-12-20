from dotenv import load_dotenv
import os
from web3 import Web3
import json

# Load environment variables
load_dotenv()

class ModeFiScout:
    def __init__(self):
        self.setup_web3()
        
    def setup_web3(self):
        """Initialize Web3 connection to Mode Network"""
        mode_rpc_url = os.getenv('MODE_RPC_URL')
        self.w3 = Web3(Web3.HTTPProvider(mode_rpc_url))
        
        # Check connection
        if self.w3.is_connected():
            print("Successfully connected to Mode Network")
        else:
            print("Failed to connect to Mode Network")

    def get_eth_balance(self, address):
        """Get ETH balance for an address"""
        try:
            balance = self.w3.eth.get_balance(address)
            return self.w3.from_wei(balance, 'ether')
        except Exception as e:
            return f"Error getting balance: {str(e)}"

def main():
    # Initialize agent
    agent = ModeFiScout()
    
    # Test functionality
    test_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example address
    balance = agent.get_eth_balance(test_address)
    print(f"Balance for {test_address}: {balance} ETH")

if __name__ == "__main__":
    main()