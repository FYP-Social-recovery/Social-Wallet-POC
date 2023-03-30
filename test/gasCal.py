# Open the input and output files
with open('gasInputs.txt', 'r') as input_file, open('gasUSD.txt', 'w') as result_file:
    # Loop through each line of the input file
    for line in input_file:
        # Parse the gas value from the input line
        gas = int(line.strip())
        
        # Define the other variables
        gas_per_gwei = 38  # replace 5 with the actual gas per gwei value
        price_of_ether = 1802  # replace 2000 with the actual price of ether value
        
        # Calculate the result
        result = gas * gas_per_gwei * price_of_ether / 1000000000
        
        # Write the result to the output file
        result_file.write(str(result) + '\n')
