from solcx import compile_standard, install_solc
def compile():
    # location for the contracts 
    with open("./Node.sol","r") as file:   #for windows  with open("contract/Node.sol","r") as file:
        node_file = file.read()

    with open("./PublicContract.sol","r") as file:
        public_contract_file = file.read()

    import json  # to save the output in a JSON file
    install_solc("0.8.17")

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
    # print(compiled_sol)     #compiled solidity file 
    with open("./compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

compile()


