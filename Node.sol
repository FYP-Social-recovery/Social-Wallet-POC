//SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./PublicContract.sol";
// contract of a node
contract Node {

    address public owner;  //Owner address

    string public userName; //my user name after registering

    address payable[] public requestedShareHolders; //temporary list of share holders

    address[] public  shareHolders; //My secret holders

    string[] public shares;    //Shares list belonging to the user 

    mapping(address => string) public shareHoldersMap; //My secret baring holders

    mapping(address => string) public sharesMap; //The secrets I'm holding

    address[] public secretOwners;  //The owners of the secrets that I'm holding 

    string[] public regeneratedShares;      //regenerated shares as a requester
    
    address public myContractAddress; //mycontract address 

    PublicContract contract_new; //Public contract obeject

    string public myState;

    constructor() { 
        owner = msg.sender;
        //Hard coded deployment of the public contract
        contract_new=PublicContract(0xd9145CCE52D386f254917e481eB44e9943F39138);
        myContractAddress = address(this);
        myState="NODE_CREATED";

    }
    // struct AddHolderRequest{
    //     address secretOwner;
    //     address shareHolder;
    // }

    // msg.data (bytes): complete calldata
    // msg.gas (uint): remaining gas
    // msg.sender (address): sender of the message (current call)
    // msg.sig (bytes4): first four bytes of the calldata (i.e. function identifier)
    // msg.value (uint): number of wei sent with the message

//modifiers 
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner has the privilege");
        _;
    }
    modifier checkIsRegistered() {
	require(isRegistered(), "Owner has to register to public contract");
	_;
    }

//function to check the userName is already registered 
    function isUserNameExist(string memory tempUserName)public view returns(bool){
        return  contract_new.isExists(tempUserName);
    }

//function to check the user is registered or not 
    function isRegistered()public view returns(bool){
       return  contract_new.isExists(userName);
    }

//Every node should register with a name into the public contract 
    function registerToPublicContract(string memory name)public onlyOwner{
        contract_new.register(name,owner,myContractAddress);
        userName=name;
        return;

    }


//!Share Holder's role-------------------------------------------------------------------------//

//Check the requests from the secret owner to a node to add as a share holder
    function checkRequestsForBeAHolder()public onlyOwner view returns (address[] memory){
    address[] memory _requestsForMe = contract_new.checkRequestsByShareholder(owner);
    return _requestsForMe;
    }

//Accept the share holder invitation
    function acceptInvitation(address secretOwner) public onlyOwner  {
        contract_new.respondToBeShareHolder(owner,secretOwner,true);
    }
//Reject the share holder invitation
    function rejectInvitation(address secretOwner) public onlyOwner {
       contract_new.respondToBeShareHolder(owner,secretOwner,true);
        
    }

//Take the secret form the secret owner and write the share in the shares map 
//( this is access though the public contract by the secret owner ) 

    function takeTheSecretFromTheOwner(address ownerAddress,string memory sharedString) public{
        secretOwners.push(ownerAddress);
        sharesMap[ownerAddress]=sharedString;
    }


//Check the requests from the requester to release the secret
    function checkRequestsForShare()public onlyOwner view returns (address[] memory){
    address[] memory _shareRequests = contract_new.checkRequestsForTheSeceret(secretOwners);
    return _shareRequests;
    }

//release the secret to the requester
    function releaseSecret(address secretOwnerAddress) public onlyOwner checkIsRegistered {
        string memory myShare =sharesMap[secretOwnerAddress];
        contract_new.releaseTheSecret(secretOwnerAddress,myShare);
        
    }


    
    

//!Secret owners role----------------------------------------------------------------------//
//Check all the temporary holders have accepted 
    function checkAcceptance()public onlyOwner returns(bool){
        makeShareHoldersListToDistribute();
        if(shareHolders.length>=requestedShareHolders.length){
            return true;
        }
        return false;
    }

//Get my state
    function getMyState()public onlyOwner returns(string memory){
        //FUNCTION TO   check all the shareholders accepted 
        //if(myState =="SHAREHOLDER_REQUESTED"){
        if(keccak256(bytes(myState)) == keccak256(bytes("SHAREHOLDER_REQUESTED"))){
            if(checkAcceptance()){
                myState="SHAREHOLDER_ACCEPTED";
                return myState;
            }
        }
        return myState;
    }
//Addiing a share holder to a temporary list
    function addTemporaryShareHolders(address payable shareHolder) public onlyOwner checkIsRegistered {
        requestedShareHolders.push(shareHolder);
        
    }

//add my shares to the contract 
    function addMyShares(string[] memory myShares)public onlyOwner{
       shares =myShares ;
    }

//get my shares 
    function getMyShares() public onlyOwner view returns(string[] memory){
        return shares;
    }


//get my share holders 
    function getShareHolders() public view returns (address[] memory)  {
        return shareHolders;
    } 


    function remove(uint256 index) public {
        // Move the last element into the place to delete
        requestedShareHolders[index] = requestedShareHolders[requestedShareHolders.length - 1];
        // Remove the last element
        requestedShareHolders.pop();
    }

//Removing a share holder from the list 
    function removeShareHolders(address payable shareHolder) public onlyOwner checkIsRegistered {
        uint256 i = 0;
        for (i; i < requestedShareHolders.length; i++) {
            if (requestedShareHolders[i] == shareHolder) {
                break;
            }
        }
        remove(i);
    }



//Make the be holder requests 
    function makingHolderRequests() public onlyOwner checkIsRegistered{
        myState="SHAREHOLDER_REQUESTED";
        uint256 i = 0;
        for (i; i<requestedShareHolders.length; i++){
            address temporaryHolder= requestedShareHolders[i];
            contract_new.makeARequestToBeAShareHolder(owner,temporaryHolder);

        }
    }

//check the holder request acceptance and make the share holders list 
    function makeShareHoldersListToDistribute()public  onlyOwner checkIsRegistered{
        address[] memory _requestAcceptedHolders=contract_new.getRequestAcceptedHoldersList(owner);  

        for (uint256 i = 0; i<_requestAcceptedHolders.length; i++){
            address temporaryHolder= _requestAcceptedHolders[i];
            shareHolders.push(temporaryHolder);
            //shareHolders[i]=temporaryHolder;

        }
    }

//Distribute the share function 
//Need to improve this with validations 
    function distribute() public onlyOwner checkIsRegistered{
        myState="SHARES_DISTRIBUTED";
        require(shares.length <= shareHolders.length, "Not enough share holders!!");
        if (shares.length <= shareHolders.length) {
            for (uint256 i = 0; i < shares.length; i++) {
                shareHoldersMap[shareHolders[i]] = shares[i]; 
                contract_new.makeSharesAccessibleToTheHolders(owner,shareHolders[i],shares[i]);
            }
        }

    }

//requesting the shares from share holders 
    function requestSharesFromHolders(string memory name) public  checkIsRegistered {
        contract_new.makeARequestToGetShares(name,owner);
        return ;
    }

//saves the share to the requested nodes regenerated shsres list
    function saveToRegeneratedShares(string memory share)public checkIsRegistered{
        regeneratedShares.push(share);
        return;
    }

//Regenerate the secret after the responses from the holders 
    function regenerate() public view checkIsRegistered onlyOwner returns (string[] memory){
        //This should generate from the other nodes 
        return regeneratedShares;
    }
// //Repay the gas fee to the holders 
//     function repayGasFee()public onlyOwner{

//     }

}

