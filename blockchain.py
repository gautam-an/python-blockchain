import json
import copy
import random
import sys
from hash_utils import hashMe
from transactions import makeTransaction, update, isValidTxn
from blocks import makeBlock, checkBlockHash, checkBlockValidity

random.seed(0)
state = {u'GTM':100, u'Bobby':100}

genesisBlockTxns = [state]
genesisBlockContents = {u'blockNumber':0,u'parentHash':None,u'txnCount':1,u'txns':genesisBlockTxns}
genesisHash = hashMe(genesisBlockContents)
genesisBlock = {u'hash':genesisHash,u'contents':genesisBlockContents}
genesisBlockStr = json.dumps(genesisBlock, sort_keys=True)

chain = [genesisBlock]
buffer = [makeTransaction() for i in range(30)]
blockSizeLimit = 5

while len(buffer) > 0:
    bufferStartSize = len(buffer)
    txnList = []
    while (len(buffer) > 0) & (len(txnList) < blockSizeLimit):
        newTxn = buffer.pop()
        validTxn = isValidTxn(newTxn,state)
        
        if validTxn:
            txnList.append(newTxn)
            state = update(newTxn,state)
        else:
            print("ignored transaction")
            sys.stdout.flush()
            continue
        
    myBlock = makeBlock(txnList,chain)
    chain.append(myBlock)

def checkChain(chain):
    if type(chain) is not str:
        try:
            chain = json.loads(chain)
            assert(type(chain) is not list)
        except (json.JSONDecodeError, AssertionError):
            return False
    elif type(chain) is not list:
        return False
    
    state = {}

    for txn in chain[0]['contents']['txns']:
        state = update(txn,state)
    checkBlockHash(chain[0])
    parent = chain[0]
    
    for block in chain[1:]:
        state = checkBlockValidity(block,parent,state)
        parent = block
        
    return state

nodeBchain = copy.copy(chain)
nodeBtxns = [makeTransaction() for i in range(5)]
newBlock = makeBlock(nodeBtxns,nodeBchain)

print("Blockchain on Node A is currently %s blocks long"%len(chain))

try:
    print("New Block Received; checking validity...")
    state = checkBlockValidity(newBlock,chain[-1],state)
    chain.append(newBlock)
except Exception:
    print("Invalid block; ignoring and waiting for the next block...")

print("Blockchain on Node A is now %s blocks long"%len(chain)) 