import random

def makeTransaction(max = 3):
    sign = int(random.getrandbits(1))*2 - 1
    amount = random.randint(1,max)
    gtmPays = sign * amount
    bobbyPays = -1 * gtmPays
    return {u'GTM':gtmPays,u'Bobby':bobbyPays}

def update(txn, state):
    state = state.copy()
    for key in txn:
        if key in state.keys():
            state[key] += txn[key]
        else:
            state[key] = txn[key]
    return state

def isValidTxn(txn, state):
    if sum(txn.values()) != 0:
        return False
    for key in txn.keys():
        if key in state.keys():
            acctBalance = state[key]
        else:
            acctBalance = 0
        if(acctBalance + txn[key] < 0):
            return False
    return True 