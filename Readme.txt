This is the POC for the Social-Recovery-Wallet project

Steps to run the application
--------------------------------------

Step 1 : Install external libraries
pip3 install coincurve bip39 bip44 bip32 web3 py-solc-x

Step 2 : Setup packages
python setup.py clean install or python3 setup.py clean install

Step 3 : Run flutter-python desktop app
Go to view folder : cd View/
Run main file :  flet main.py -d

-----------------------------------
Public Contract 


Alice -		secret owner -  ["Share1","Share2","Share3"]
Bob -		Share holder 
Charlie -	share holder 
David - 	Share holder
Eve-		Share Requester
