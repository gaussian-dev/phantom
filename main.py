from fhe import *

def location_circuit(location: [[FHEUint8]], guesses:[[FHEUint8]]): 
    '''
    Returns whether `location` is one of the location guesses in `guesses`

    location: location represented as bytes
    guesses: array of guesses represented as bytes
    '''
    out = FHEBool.trivial(False)
    
    for g in guesses:
        # check location matches with `g`
        # Note: any location is array of bytes
        o = FHEBool.trivial(True)
        for (b0 , b1) in zip(g, location):
            o = o and (b0 == b1)

        out = out or o
    pass
    
def debt_cancel_circuit(a: [FHEUint32], a_is_owed: [FHEUint32], b: [FHEUint32], b_owes:[FHEUint32], a_owes_b: u32) -> ([FHEUint32], [FHEUint32], FHEUint32):
    '''
    A needs to pay `a_owes_b` amount to B. Can we cancel the debt via friends they (may) have in common?

    a: array of identity of people that owe some amount to A
    a_is_owed: i^th identity in `a` owes A `a_is_owed` amount
    b: array of identity of people to whom B owes some amount
    b_owes: B owes i^th identity b[i] b_owes[i] amount

    out_identity: Identity of friends in common that participated in cancellation
    out_amount: out_identity[i] now owes out_amount[i] less to a and is owed out_amount[i] less by b
    '''

    amount_left = FHEUint32.trivial(a_owes_b)

    out_identity = []
    out_amount = []

    # for each of people that owe some amount to A check whether B owes them. If yes, decrease `amount_left` by min(amount_left, owed amount)
    for a_i in range(0, len(a)):
        
        for b_j in range(0, len(b)):
            # think of is_equal as `if`
            is_equal = a[a_i] == b[b_j]

            # how much can we subtract
            tmp = (a_is_owed[a_i].min(b_owes[b_j]) * is_equal)
            amount = tmp.min(
                amount_left
            )
            

            out_identity.append(b[b_j] * is_equal)
            out_amount.append(amount)

            amount_left = amount_left - amount

            
    return (out_identity, out_amount, amount_left)

pk = CollectivePublicKey()

# A owes B 100. A and B are stranger but they happen to have C (identity: 5) as friend in common
a = [pk.encryptU32(5), pk.encryptU32(11)]
a_is_owed = [pk.encryptU32(50), pk.encryptU32(100)]

b = [pk.encryptU32(5), pk.encryptU32(12)]
b_owes = [pk.encryptU32(40), pk.encryptU32(1000)]
a_owes_b = 100

(out_identity, out_amount, amount_left) = debt_cancel_circuit(a=a, a_is_owed=a_is_owed, b=b, b_owes=b_owes, a_owes_b=a_owes_b)

out_identity_dec = [CollectiveDecrypt(i) for i in out_identity]
out_amount_dec = [CollectiveDecrypt(i) for i in out_amount]
amount_left_dec = CollectiveDecrypt(amount_left)

print(out_identity_dec, out_amount_dec, amount_left_dec)
