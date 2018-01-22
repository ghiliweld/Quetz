# Viper Port of ERC721.sol and MyNonFungibleToken.sol
# THIS CONTRACT HAS NOT BEEN AUDITED!
# The code here is taken from: https://github.com/ghiliweld/ERC-ME/blob/master/viper-contracts/ERC721.v.py


# Events of the token.
Transfer: __log__({_from: indexed(address), _to: indexed(address), _tokenId: num256})
NewToken: __log__({_owner: indexed(address), _tokenId: num256})


# Variables of the token.
name = "ERC-ME"
symbol = "ME"
totalSupply: num
balances: num[address]

Token: {
    mintedBy: address,
    mintedAt: timestamp,
}

Tokens: public(Token[]) # An array of Tokens tied to a tokenIds (array index). Is this how it's done?

tokenIndexToOwner: public(address[num256])
ownershipTokenCount: public(num256[adress])
tokenIndexToApproved: public(address[num256]) # Still don't know why approved is a thing...

# THE FUNCTIONS

# What is the Token balance of a particular account?
@public
@constant
def balanceOf(_owner: address) -> (num256):

    return as_num256(ownershipTokenCount[_owner])


# What Token is this address the owner of?
@public
@constant
def ownerOf(_tokenId: num256) -> (address):

    owner = tokenIndexToOwner[_tokenId]
    assert owner != address(0)
    return owner

# Return total supply of token.
@public
@constant
def totalSupply() -> (num256):

    return as_num256(len(Tokens))


@private
@constant
def _owns(_claimant: address, _tokenId: num256) -> (bool):

    return (tokenIndexToOwner[_tokenId] == _claimant)

@private
@constant
def _approvedFor(_claimant: address, _tokenId: num256) -> (bool):

    return (tokenIndexToApproved[_tokenId] == _claimant)

@private
def _approve(_to: address, _tokenId: num256):

    tokenIndexToApproved[_tokenId] = _to
    log.Approval(tokenIndexToOwner[_tokenId], tokenIndexToApproved[_tokenId], _tokenId)

@public
def approve(_to: address, _tokenId: num256):

    assert _owns(msg.sender, _tokenId)
    _approve(_to, _tokenId)

# Send `_value` tokens to `_to` from your account
@private
def _transfer( _from: address, _to: address, _tokenId: num256):

    ownershipTokenCount[_to] += 1
    tokenIndexToOwner[_tokenId] = _to
    if _from != address(0):
        ownershipTokenCount[_from] -= 1
        delete tokenIndexToApproved[_tokenId]

    log.Transfer(_from, _to, _tokenId)

@public
def transfer(_to: address, _tokenId: num256):

    assert _to != address(0)
    assert _to != msg.sender
    assert _owns(msg.sender, _tokenId))

    _transfer(msg.sender, _to, _tokenId)

# Transfer allowed tokens from a specific account to another.
@public
def transferFrom(_to: address, _tokenId: num256):

    assert _to != address(0)
    assert _to != msg.sender
    assert _approvedFor(msg.sender, _tokenId)
    assert _owns(msg.sender, _tokenId))

    _transfer(msg.sender, _to, _tokenId)

@private
def _mint():

    token: Token
    token.mintedBy = msg.sender
    token.mintedAt = block.timestamp

    tokenId: num = tokens.append(token) - 1;

    log.NewToken(msg.sender, _tokenId)
    _transfer(0, msg.sender, tokenId)

@public
@constant
def TokensOfOwner(_owner: address) -> (num256[]):

    balance: num256 = balanceOf(_owner)

    if balance == 0
        return num256[0]
    else:
        result: num256[balance]
        uint256 maxtokenId = totalSupply()
        idx: num256 = 0

        tokenId: num256
        for tokenId in range(0, maxtokenId)
            if tokenIndexToOwner[tokenId] == _owner:
                result[idx] = tokenId
                idx += 1

    return result

@public
@constant
def getToken(_tokenId: num256) -> (mintedBy: address, mintedAt: timestamp):

    token: Token = tokens[_tokenId]
    mintedBy: address = Token.mintedBy
    mintedAt: timestamp = Token.mintedAt

@public
@constant
def getTokenMintedBy(_tokenId: num256) -> (mintedBy: address):

    token: Token = tokens[_tokenId]
    mintedBy: address = token.mintedBy

@public
@constant
def getTokenMintedAt(_tokenId: num256) -> (mintedAt: timestamp):

    token: Token = tokens[_tokenId]
    mintedAt: timestamp = Token.mintedAt
