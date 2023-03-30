import requests
def convert():
    # Open the input and output files
    with open(r'./test/gasInputs.txt', 'r') as input_file, open(r'./test/gasUSD.txt', 'w') as result_file:
        gas_per_gwei = getGasPrice()  # replace 5 with the actual gas per gwei value
        price_of_ether = getEthereumPrice()  # replace 2000 with the actual price of ether value
        # Loop through each line of the input file
        for line in input_file:
            # Parse the gas value from the input line
            gas = int(line.strip())
            
            # Define the other variables
            
            
            # Calculate the result
            result = gas * gas_per_gwei * price_of_ether / 1000000000
            
            # Write the result to the output file
            result_file.write(str(result) + '\n')

def getGasPrice():

    API_KEY = 'VGXRM3NMVWJGGWFM3FEP4IHH3UAG4MCPKC'

    # Define the API endpoints
    GAS_PRICE_API = f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={API_KEY}'
    # Get the gas price
    response = requests.get(GAS_PRICE_API)
    gas_price = int(response.json()['result']['FastGasPrice'])
    print(f'Gas Price: {gas_price} Gwei')
    return gas_price

def getEthereumPrice():
  
    API_KEY = 'VGXRM3NMVWJGGWFM3FEP4IHH3UAG4MCPKC'
    PRICE_API = f'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={API_KEY}'
    # Get the Ethereum price
    response = requests.get(PRICE_API)
    eth_price = float(response.json()['result']['ethusd'])
    print(f'Ethereum Price: ${eth_price:.2f}')
    return eth_price







convert()




