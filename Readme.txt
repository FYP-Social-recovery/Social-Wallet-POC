This is the POC for the Social-Recovery-Wallet project
===================================================================================================
Steps to run the application
===================================================================================================

Step 1 : Install external libraries
pip3 install coincurve bip39 bip44 bip32 web3 py-solc-x pyperclip xclip

Step 2 : Setup packages
python setup.py clean install or python3 setup.py clean install

Step 3 : compile the solidity contracts 


Step 3 : Run flutter-python desktop app
Go to view folder : cd View/
Run main file :  flet main.py -d

========================================================================================================
Default values for testing 
========================================================================================================
Public Contract address 0x71404eaFfCFCb4678e79479c1Da26608623b963e
Test node contract address 0x90ebA7fCd273fB7A2EFE4BFf0c08064A219029BA


Test mnemonic :zone dilemma real cancel expect cradle pave satisfy comfort silver speed work
Test Public Key: 0x20543FD8D854d500121215Abc542531987f6bc2e
Test Secret Key: 58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655
Alice -		secret owner -  ["Share1","Share2","Share3"]
Bob -		Share holder 
Charlie -	share holder 
David - 	Share holder
Eve-		Share Requester


========================================================================================================
Versions 
========================================================================================================

0.0.1- Key generation part using mnemonic and random mnemonic generation
0.0.2- Share holder request , show share holder acceptance distribute the secret
0.0.3- Key recovery from the share holders ,Optimize the smart contract and eliminate the vulnerabilities 
