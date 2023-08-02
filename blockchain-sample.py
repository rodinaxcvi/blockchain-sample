'''

Blockchain basics and sample code:


Hoo-Wee Coin (HC)


Transactions (t1, t2, etc.):

t1: Vladimir_Z sends Jeremy132 40 HC
t2: NateDaMan sends Rasher 2000 HC
t3: Paul_Bunyan sends BillyBobJoel 1 HC 



How a blockchain works:


Block 1                 Hashed Data                                     Next Hash
|                            |                                              |
B1 ("AAA", t1, t2, t3) -> 65wr43, B2 (65wr43, t4, t5, t6) -> (Next Hash) 8564rr, B3 (8564rr, t7)



B1, B2, B3: Each block containing the list of transactions. Having more blocks to hold transactions helps with scalability and security

            
"65wr43": Hash of B1



"B2(65wr43, t4, t5, t6)": This is Block 2 and it contains the hash of Block 1 to verify, along with more transactions



"8564rr": Hash of B2


-  SALTING OF HASHED DATA (??)

'''


import hashlib

class HooWeeCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Vladimir_Z sends Jeremy132 40 HC"
t2 = "NateDaMan sends Rasher 2000 HC"
t3 = "Paul_Bunyan sends BillyBobJoel 1 HC"
t4 = "MacnCheese sends MikeMike 30 HC"
t5 = "Jeremy132 sends NateDaMan 400 HC"
t6 = "Jeremy132 sends Jeremy133 30 HC"

initial_block = HooWeeCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)
