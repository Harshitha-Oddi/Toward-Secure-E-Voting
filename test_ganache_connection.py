from web3 import Web3  
  
print("Testing Ganache Connection...")  
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  
if w3.is_connected():  
    print("Connected to Ganache!")  
else:  
    print("Cannot connect. Is Ganache running?") 
