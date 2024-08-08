import requests
import json
from time import sleep

def printArbitrage(d, startAdd):
    for key,val in d.items():
        print(key,"-->",val)
        if val==startAdd:
            print("Arbitrage cycle complete")
    return 


def findArbitrage():
    counter = 0
    url = "https://api.bscscan.com/api?module=account&action=txlistinternal&startblock=40784970&endblock=40784980&page=1&offset=10&sort=asc&apikey=X22TPFNDFN4XH54WMRFQUYFWPZV9KKRKUF"

    x = requests.get(url)
    response = json.loads(x.text)

    transactions = response["result"]

    transTypes = ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822","0x19b47279256b2a23a1665c810c8d55a1758940ee09377d4f8d26497a3577dc83"]

    for transaction in transactions:
        transactionHash = transaction["hash"]
        print(transactionHash)
        headers = {
        'Content-Type': 'application/json',
        }
        json_data = {
            'jsonrpc': '2.0',
            'method': 'eth_getTransactionReceipt',
            'params': [
                transactionHash,
            ],
            'id': 1,
        }

        receiptResponse = requests.post('https://docs-demo.bsc.quiknode.pro/', headers=headers, json=json_data)
        # preventing request timeout
        counter += 1
        if (counter % 5 == 0):
            sleep(1)

        receipt = (json.loads(receiptResponse.text))["result"]

        srcToDest = dict()

        for eventLog in receipt["logs"]:
            if eventLog["topics"][0] == transTypes[0]:
                # looking for transfer types
                src = eventLog["topics"][1]
                dest = eventLog["topics"][2]
                srcToDest[src] = dest
                if dest in srcToDest.keys():
                    # arbitrage cycle found!
                    printArbitrage(srcToDest, dest)
        
        print("--- transaction done ---\n")
        
findArbitrage()
