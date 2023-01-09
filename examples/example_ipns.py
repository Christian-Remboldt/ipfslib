from ipfslib import *

api = Connect()

keys = Key.list(api)

# Check id of 'example_key'
ipns_name = ''
for key in keys:
    if key['Name'] == 'example_key':
        ipns_name = key['Id']
        break

# Create 'example_key' if it doesn't exsist
if ipns_name == '':
    ipns_name = Key.generate(api, 'example_key')

# Add file to IPFS
cid = IPFS.add(api, 'helloworld.txt')

# Update the value of 'example_key'
ipns_data = Key.publish(api, cid, 'example_key')

print('Published "helloworld.txt" in IPNS:')
print('IPNS Name:', ipns_data[0])
print('Points to:', ipns_data[1])