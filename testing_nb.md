

```python
from web3 import Web3
from DMM_POOL_ABI import DMM_POOL_ABI
```


```python
addr = "0x306121f1344ac5F84760998484c0176d7BFB7134"
http_provider = "https://mainnet.infura.io/v3/yourToken"
web3 = Web3(Web3.HTTPProvider(http_provider))
contract = DMM_POOL_ABI(web3, addr)
```


```python
contract.totalSupply()
```




    {'totalSupply_OUTPUT_0': 53495213276709}




```python
contract.totalSupply_OUTPUT_0
```




    53495213276709




```python
contract.token0()
```




    {'token0_OUTPUT_0': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'}




```python
contract.token1()
```




    {'token1_OUTPUT_0': '0xdAC17F958D2ee523a2206206994597C13D831ec7'}


