class NodeModel:
    from web3 import Web3
    from solcx import compile_standard, install_solc

    with open(r"F:\Sadaru Kavisha\Semester 7\Fyp\Final Project\Social-Wallet-POC\contract\Node.sol","r") as file:
        node_file = file.read()

    with open(r"F:\Sadaru Kavisha\Semester 7\Fyp\Final Project\Social-Wallet-POC\contract\PublicContract.sol","r") as file:
        public_contract_file = file.read()

    import json  # to save the output in a JSON file
    install_solc("0.8.0")

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "Node.sol": {"content": node_file},
                "PublicContract.sol":{"content":public_contract_file}
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        # output needed to interact with and deploy contract
                        "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                    }
                }
            },
        },
        solc_version="0.8.17",
    )
    print(compiled_sol)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)


    # get bytecode
    bytecode = compiled_sol["contracts"]["Node.sol"]["Node"]["evm"]["bytecode"]["object"]
    # get abi
    abi = json.loads(compiled_sol["contracts"]["Node.sol"]
                    ["Node"]["metadata"])["output"]["abi"]

    # For connecting to ganache
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    chain_id = 1337
    address = "0x305eC56922EDcF716F12C7a5c5961147933C0c41"
    # leaving the private key like this is very insecure if you are working on real world project
    private_key = "2e4d7319aad09af344608bde9dee0aa5a8243f847dc004545927a3488c0f8338"
    # Create the contract in Python
    ContactList = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Get the number of latest transaction
    nonce = w3.eth.getTransactionCount(address)


    # build transaction
    transaction = ContactList.constructor().buildTransaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": nonce,
        }
    )
    # Sign the transaction
    sign_transaction = w3.eth.account.sign_transaction(
        transaction, private_key=private_key)
    print("Deploying Contract!")
    # Send the transaction
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")