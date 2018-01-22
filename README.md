# Quetz: A smart contract programming language built for human readability and simplicity

**Quetz**, short for Quetzalcoatl, is a proposal for an alternate smart contract programming language. Not one meant to replace [Solidity](http://solidity.readthedocs.io/en/develop/) or [Viper](https://vyper.readthedocs.io/en/latest/index.html) completely, but one that can complement these languages and reduce complexity when coding trivial contracts.

## Why?
- While Solidity and Viper are relatively simple languages, they still have a slight barrier to entry for beginners to programming and are tricky even for programming experts (security wise). If we're really going for decentralization, then I believe coding and reading smart contracts should be as easy as reading English (no, not legalese English). The power to code contracts should **not** be centralized in the hands of a few developers. Auditing would be way simpler too.
- I thought proposing my own language would be a fun challenge so why not?

## How?
- To be honest, I'm not a very good programmer. I've yet to deploy my own Dapp, much less code my own language. I will be proposing a possible syntax that could be used, however I have no means to make it a reality on my own. What I plan on doing is replicating common contracts in the "Quetz style" that I have in mind and building it together with the Ethereum community (who are far talented developers).
- With what I have in mind, Quetz will probably be very similar to Viper (and Python by extension). Human readable code, with whitespace to separate functions and declarations, etc...
- If this were to work, Quetz would be heavily dependent on predetermined sentence structures that the compiler can recognize, sometimes at the cost of grammar hindering the readability in a way. For example, `Event: _eventName_ logs a _paramName_{_paramType_}, a _paramName_{_paramType_}, a _paramName_{_paramType_}`. Every word in that sentence surrounded by underscores would be variables. For the rest however, those would the predetermined sentence structures. Change how it's structured and you'll get a compiling error.
- Feel free to fork this repo (it's MIT btw), I'd love to see what ideas y'all have in mind!

## Quetz details
For now, Quetz files will have the extension `q.py` to take advantage of Python code highlighting (Quetz will be heavily based on Python). Eventually, I'm aiming for something `.qz`.
Ex:
`contractName.q.py`
`contractName.qz`

Docs will be written once all the Quetz contract examples have been written and I can find a standard format that works.

The repo is organized in this way:

1. Quetz repository
    1. contract folder
        1. contract.q.py or contract.qz
        2. contract.sol
        3. contract.v.py or contract.vy

Contract folders will have names like "token" or "auction" and they will contain Quetz, Solidity and Viper versions written for comparison.

## Disclaimer
The code in this repo has **not** been audited. The Solidity and Viper code here is under the MIT license meaning it's free to use for commercial purposes but I have no liability for any damages or loss of funds.

**Have a suggestion? Leave an issue and I'll check it out real quick!**
