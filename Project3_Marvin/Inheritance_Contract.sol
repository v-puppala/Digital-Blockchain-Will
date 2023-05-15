pragma solidity 0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.1/contracts/token/ERC721/ERC721Full.sol";

contract Inheritance is ERC721Full {
    constructor() public ERC721Full("StockHoldings", "SNFT") {}

    struct Stock {
        string company;
        string ticker;
        uint256 shares;
        string brokerage;
    }

    mapping(uint256 => Stock) public stockPortfolio;

    event PortfolioUpdate(uint256 token_id, string company, string ticker, uint256 shares, string reportURI);

    function registerStock(
        address owner, 
        string memory company, 
        string memory ticker, 
        uint256 shares, 
        string memory brokerage, 
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        stockPortfolio[tokenId] = Stock(company, ticker, shares, brokerage);

        return tokenId;
    }
}
