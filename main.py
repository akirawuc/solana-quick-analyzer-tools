import requests as r
import json
import argparse
parser = argparse.ArgumentParser(description='help getting the tx')

parser.add_argument('-t', '--type', type=str,
                    help='identify which method to use')

parser.add_argument('-s', '--sig', type=str,
                    help='the signature of the tx')

args = parser.parse_args()

'''
- modify the whole fetching code to factory pattern.
    - getResp(reqType)
    - reqType: different implementation of different rpc method
'''


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


def replacingInvalid(string: str) -> str:
    string = string.replace('null', '"null"')
    string = string.replace('false', 'False')
    string = string.replace('true', 'True')
    return string


if __name__ == '__main__':
    print(f'Checking the content of {args.sig}:')
    thisTx = eval(replacingInvalid(getTx(args.sig).text))
    print(json.dumps(thisTx, indent=3))
