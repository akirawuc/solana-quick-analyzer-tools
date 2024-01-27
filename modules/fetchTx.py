import requests as r


def getTx(sig):
    url = 'http://api.mainnet-beta.solana.com'
    content = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTransaction",
        "params": [
          sig,
          "json"
        ]
      }
    return r.post(url, json=content)
