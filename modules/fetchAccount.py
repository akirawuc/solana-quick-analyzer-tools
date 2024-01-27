import requests as r


def getAccount(address,
               rpc='http://api.mainnet-beta.solana.com'):
    content = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [
                address,
              {
                "encoding": "jsonParsed"
              }
            ]
            }
    return r.post(rpc, json=content)
