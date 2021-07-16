# abi2py
 Converts Ethereum ABI functions (in json file) to a Python class

## Possible improvements
 - Would be nice for output py file to be async
 - Automatic formatting (black?) would be cool
 - Add functionality to suppress dictionary output if user doesn't care to receive it

## Notes
 - When there is no name for an output, gives name as funcname_OUTPUT_counter
 - Does something similar for inputs with no name
 - Outputs are returned both to a self attribute of the class instance and as a separate dictionary

## How to
 Give web3 api provider, and contract address

```python
from abi2py import ABI2py

file = "DMM_POOL_ABI.json"
ABI2py(file)
```


## Example
 Give web3 api provider, and contract address

```python
from web3 import Web3
from DMM_POOL_ABI import DMM_POOL_ABI # This is the output from running ABI2py(file)
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


