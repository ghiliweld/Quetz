Contract: ERC20
QZ: 0.0.1 # Quetz compiler version, will be important in case the standard changes as time goes on

# Hashtags are used for commenting

# Events of the token.
Event: Transfer logs a from{address}, a to{address}, a value{num}


# Variables of the token.
# Watch how variables are declared
# _variableName_ is a _variableType_, set _variableValue_ or just _variableName_ is a _variableType_
name is a string, set "ERC20"
# v.s. variableName{variableType} = variableValue
# The second option has less writting so I'll stick to that but I'll consider both options later
name{string} = "ERC20"
symbol{string} = "20"
totalSupply{num} = 9001 # IT'S OVER 9000!!!!!!!
decimals{num} = 18
balances{mapping} = num[address] # mappingName{mapping} = valueType[keyType]

# FUNCTIONS known as ACTIONS in Quetz
# Functions in Quetz are called Actions, that react to calls and assess and act on parameters fed to them
# Action _actionName_ takes(paramName{paramType}) *takes is optional, is _visibilityStatus, is _read/payable *(this is optional), gives _returnType *gives is optional
Action symbol, is public, is read, gives a string:
    give symbol of this contract
    # this contract will be standard keywords to literally mean this contract on which the function is being called

#What is the balance of a particularaccount?
Action balanceOf takes(_owner{address}), is public, is read, gives a num:
    give balances of _owner

# Return total supply of token.
Action totalSupply, is public, is read, gives num:
    give totalSupply of this contract

# Send `_value` tokens to `_to` from your account
Action transfer takes(_to{address}, _amount{num}), is public, gives a bool:
    require _amount more than 0 # No negative amounts, require is a keyword
    # the sentence goes on to the part after the comma if the condition isn't fulfilled, returns what is given and throws the transaction
    require balances of msg.sender moreequal than _amount # You can't send more than you have
    balances of msg.sender minusequal _amount
    balances of _to plusequal _amount
    Transfer: msg.sender, _to, _amount # Transfer event call
    give True
