pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract WillToken is ERC721Full {
    constructor() public ERC721Full("RealEstToken", "RE") {}

    struct RealEstate {
        string name;
        string ssn;
        string dob;
        string assetname;
        uint256 assetvalue;
    }

    mapping(uint256 => RealEstate) public land;

    event WillRecording(uint256 token_id, string name, string ssn, string assetname, uint256 assetvalue);


    function registerAsset(
        address owner,
        string memory name,
        string memory ssn,
        string memory dob,
        string memory assetname,
        uint256 assetvalue
    ) public returns (uint256) {
        uint256 tokenID = totalSupply();

        _mint(owner, tokenID);

        land[tokenID] = RealEstate(name, ssn, dob, assetname, assetvalue);

        return tokenID;
    }
}