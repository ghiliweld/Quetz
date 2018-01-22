Contract: ERC721
QZ: 0.0.1 # Quetz compiler version, will be important in case the standard changes as time goes on

# Hashtags are used for commenting

# Events of the token.
Event: Transfer logs a from{address}, a to{address}, a tokenId{num}
Event: NewToken logs a creator{address}, a tokenId{num}


# Variables of the token.
# Watch how variables are declared
# variableName{variableType} = variableValue
name{string} = "ERC721"
symbol{string} = "721"
tokenIndexToOwner{mapping}: address[num]  # mappingName{mapping}: valueType[keyType]
ownershipTokenCount{mapping}: num[adress]

All Token have:     # This is how structs are created
    - mintedBy{address}
    - mintedAt{timestamp}

tokens{array}: Token # An array of our token struct
# FUNCTIONS known as ACTIONS in Quetz
# Functions in Quetz are called Actions, that react to calls and assess and act on parameters fed to them
# Action _actionName_ takes(paramName{paramType}) *takes is optional, is _visibilityStatus, is _read/payable *(this is optional), gives _returnType *gives is optional
Action symbol, is public, is read, gives a string:
    give symbol of this contract
    # this contract will be standard keywords to literally mean this contract on which the function is being called

#What is the balance of a particularaccount?
Action balanceOf takes(_owner{address}), is public, is read, gives a num:
    give ownershipTokenCount of _owner

#Who is the owner of a token?
Action ownerOf takes(_tokenId{num}), is public, is read, gives a address:
    give tokenIndexToOwner of _tokenId

#Who is the owner of a token?
Action _owns takes(_claimant{address}, _tokenId{num}), is private, is read, gives a bool:
    check if tokenIndexToOwner of _claimant equal _claimant
    give check

# Return total supply of token.
Action totalSupply, is public, is read, gives num:
    give tokens length

Action _transfer takes( _from{address}, _to{address}, _tokenId{num256}), is private:
    ownershipTokenCount of _to plusequal 1
    tokenIndexToOwner of _tokenId equal _to
    if _from isnot address0:
        ownershipTokenCount of _from minusequal 1

    Transfer: _from, _to, _tokenId # Transfer event call

# Send `_value` tokens to `_to` from your account
Action transfer takes(_to{address}, _tokenId{num}), is public:
    require _to isnot address0
    require _to isnot msg.sender
    require _owns(msg.sender, _tokenId)
    call _transfer take msg.sender, _to, _tokenId

Action _mint, is public:
    token is a Token
    mintedBy of token is msg.sender
    mintedAt of token is now
    tokenId of token is (add token to tokens) - 1

    NewToken: msg.sender, _tokenId
    call _transfer take this contract, msg.sender, _tokenId
