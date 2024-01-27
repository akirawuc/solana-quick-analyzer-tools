# TODO methods

- Get Balance
`curl http://localhost:8899 -X POST -H "Content-Type: application/json" -d '
  {"jsonrpc":"2.0", "id":1, "method":"getBalance", "params":["83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri"]}
'`

- Subscribe account
https://docs.solana.com/developing/clients/jsonrpc-api#accountsubscribe
`{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "accountSubscribe",
  "params": [
    "CM78CPUeXjn8o3yroDHxUtKsZZgoy4GPkPPXfouKNH12",
    {
      "encoding": "base64",
      "commitment": "finalized"
    }
  ]
}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "accountSubscribe",
  "params": [
    "CM78CPUeXjn8o3yroDHxUtKsZZgoy4GPkPPXfouKNH12",
    {
      "encoding": "jsonParsed"
    }
  ]
}`
`
