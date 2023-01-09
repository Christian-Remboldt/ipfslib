from ipfslib import *

api = Connect()
cid = IPFS.add(api, 'helloworld.txt')

print(cid)