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
        if not mode_rpc_url:
            raise ValueError("MODE_RPC_URL not found in .env file")
            
        self.w3 = Web3(Web3.HTTPProvider(mode_rpc_url))
        
        # Check connection
        if self.w3.is_connected():
            print("Successfully connected to Mode Network")
            print(f"Current block number: {self.w3.eth.block_number}")
        else:
            print("Failed to connect to Mode Network")

    def get_eth_balance(self, address):
        """Get ETH balance for an address"""
        try:
            if not self.w3.is_address(address):
                return "Invalid Ethereum address"
            
            balance = self.w3.eth.get_balance(address)
            return self.w3.from_wei(balance, 'ether')
        except Exception as e:
            return f"Error getting balance: {str(e)}"

def main():
    try:
        # Initialize agent
        agent = ModeFiScout()
        
        # Test functionality with a valid Mode Network address
        test_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example address
        balance = agent.get_eth_balance(test_address)
        print(f"Balance for {test_address}: {balance} ETH")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()