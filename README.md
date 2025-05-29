# python-blockchain
a python implementation of a basic blockchain with transaction validation and cryptographic hashing.

## Features

- Transaction creation and validation  
- Block creation and cryptographic linking  
- Full chain verification  
- SHA-256 hashing for data integrity  
- State and balance tracking  
- JSON-based serialization  

## Technologies Used

- [Python 3](https://www.python.org/)
- [JSON](https://www.json.org/json-en.html) for data serialization
- [SHA-256](https://en.wikipedia.org/wiki/SHA-2) cryptographic hashing
- [random module](https://docs.python.org/3/library/random.html) for transaction simulation

## Architecture

- **Modular design**: Each core functionality resides in its own file  
- **Object-Oriented**: Clean, scalable code structure  
- **State-Based Ledger**: Manages balances and transaction states  
- **Linked Blocks**: Uses hash chaining for block integrity  

## Security Features

- SHA-256 based hashing
- Per-transaction validation
- Block integrity and linkage checks
- Full-chain consistency verification

## Data Structures

- **Dictionaries**: For managing state and balances  
- **Lists**: For storing the blockchain  
- **JSON**: For consistent data formatting  
- **Hashes**: For secure block referencing

## Testing & Validation

- Transaction validation logic
- Block hash verification
- Chain integrity checks
- State and balance consistency