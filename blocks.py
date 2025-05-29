from hash_utils import hashMe
from transactions import isValidTxn, update

def makeBlock(txns, chain):
    parentBlock = chain[-1]
    parentHash = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    blockContents = {u'blockNumber':blockNumber,u'parentHash':parentHash,
                      u'txnCount':len(txns),'txns':txns}
    blockHash = hashMe(blockContents)
    block = {u'hash':blockHash,u'contents':blockContents}
    return block

def checkBlockHash(block):
    expectedHash = hashMe(block['contents'])
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block %s'%
                        block['contents']['blockNumber'])
    return

def checkBlockValidity(block, parent, state):    
    parentNumber = parent['contents']['blockNumber']
    parentHash = parent['hash']
    blockNumber = block['contents']['blockNumber']
    
    for txn in block['contents']['txns']:
        if isValidTxn(txn,state):
            state = update(txn,state)
        else:
            raise Exception('Invalid transaction in block %s: %s'%(blockNumber,txn))

    checkBlockHash(block)

    if blockNumber!=(parentNumber+1):
        raise Exception('Hash does not match contents of block %s'%blockNumber)

    if block['contents']['parentHash'] != parentHash:
        raise Exception('Parent hash not accurate at block %s'%blockNumber)
    
    return state 