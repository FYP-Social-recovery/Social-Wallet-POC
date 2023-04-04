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

Step :Start server
Goto api folder : cd api/
Run nodeAPI.py file : python nodeAPI.py

========================================================================================================
Default values for testing 
========================================================================================================

Admin
0x4A04D4fB008dceAA7Ff212f296Cd9F82874cEAff
a0dc1ea77cb68f16abb1671b44048c6a9f7822676d841f4a9908a5a981871fce

Alice - Owner
apart shallow normal poet demise absurd execute famous find high neither chef
0x1c36c98DC9b260564F17817241fED3BBA1402059
ec754553254fd6b9bcfa929e27d378b648b4ac8adf926b0663e41e13c03c174d

Bob - holder 1
zone dilemma real cancel expect cradle pave satisfy comfort silver speed work
0x20543FD8D854d500121215Abc542531987f6bc2e
58d0efedba9a8a61b2ac3f188dd079782e07aed904cdbc0e3340e073e85c7655

Charlie - holder 2
wonder jazz wall vanish stool track isolate aim hair loyal fatal cause
0x799fe4A6cb83c817ada12258fb3B3864Fb2B5027
7e67ba86219723f80c27e55d90c34eab27afe92d092da6eb4c05b3bbd49914c4

David - holder 3
payment eight quote olive silly ocean liberty flush electric inside boil physical
0xdDCED81E6D27C0C4EAEf81485661c81AC979399C
874a1cef37dee7bf7494da0c77dc2dc942ffca517be583408a639da347f961d4

Eve - Recover
curious crash rough make play spirit plate angry biology twenty veteran soul
0xc1dc99853409Cdf40F0CD1657749aA601B9827Df
3fdec33da5e0e37bff512e6234c0ab0f38710161057afcf9123a74deba75b236

=======================================================

========================================================================================================
Versions 
========================================================================================================

0.0.1- Key generation part using mnemonic and random mnemonic generation
0.0.2- Share holder request , show share holder acceptance distribute the secret
0.0.3- Key recovery from the share holders ,Optimize the smart contract and eliminate the vulnerabilities 
0.0.4- Screens and backend completed until the distribution eliminated vulnerabilities -name convention,immutable variables,redundant statements
1.0.0- Completed wallet release for layer 1
2.0.0- Completed wallet release for layer 2
2.1.0- Otp logic changed
2.1.1-
2.1.2- Vault hash returning bug fixed
