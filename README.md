# python-blockchain
a python implementation of a basic blockchain with transaction validation and cryptographic hashing.

## features

- transaction creation and validation  
- block creation and cryptographic linking  
- full chain verification  
- SHA-256 hashing for data integrity  
- state and balance tracking  
- JSON-based serialization  

## main technologies used 

- [SHA-256](https://en.wikipedia.org/wiki/SHA-2) cryptographic hashing
- [random module](https://docs.python.org/3/library/random.html) for transaction simulation

## architecture

- **modular design**: each core functionality resides in its own file  
- **object-oriented**: clean and scalable code structure  
- **state-based ledger**: manages balances and transaction states  
- **linked blocks**: Uses hash chaining for block integrity  

## security features

- SHA-256 based hashing
- Per-transaction validation
- Block integrity and linkage checks
- Full-chain consistency verification

## testing & validation

- transaction validation logic
- block hash verification
- chain integrity checks
- state and balance consistency