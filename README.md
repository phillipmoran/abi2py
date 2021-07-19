# abi2py
 Converts Ethereum ABI functions (in json file) to a Python class

## Possible improvements
 - Would be nice for output py file to be async
 - Automatic formatting (black?) would be cool
 - Add functionality to suppress dictionary output if user doesn't care to receive it
 - Is it common (or possible) for function outputs to have same names across funcs in ABI? Could cause issues and would need to tweak self.output data returned at func call.

## Notes
 - When there is no name for an output, gives name as funcname_OUTPUT_counter
 - Does something similar for inputs with no name
 - Outputs are returned both to a self attribute of the class instance and as a separate dictionary (if there is more than one output) or simply returning the output (if only one output)

## How to
###
Pop your ABI json files in the abi_folder.
Run in cmd prompt
```
> python abi2py.py
```
The python objects of the ABI json's will be output to the abi_output folder.
You can also give a different path for input ABI files and output directory. Just check out abi2py.py.

### Using the created scripts
 Give web3 api provider, and contract address


```python
from web3 import Web3
from abi_output.DMM_POOL_ABI import DMM_POOL_ABI
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




    54362452575909




```python
contract.totalSupply_OUTPUT_0
```




    54362452575909




```python
contract.token0()
```




    '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'




```python
contract.token1()
```




    '0xdAC17F958D2ee523a2206206994597C13D831ec7'




```python
contract.symbol()
```




    'DMM-LP USDC-USDT'




```python
# Multiple outputs returned as a dictionary
contract.getReserves()
```




    {'_reserve0': 54317737309760, '_reserve1': 54412737982824}

