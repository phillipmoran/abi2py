class UNISWAPV2PAIR:
    def __init__(self, web3_connection, addr):
        self.web3 = web3_connection
        self.addr = addr
        self.abi = [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'Burn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'name': 'Mint', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0In', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1In', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0Out', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1Out', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'Swap', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint112', 'name': 'reserve0', 'type': 'uint112'}, {'indexed': False, 'internalType': 'uint112', 'name': 'reserve1', 'type': 'uint112'}], 'name': 'Sync', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [], 'name': 'DOMAIN_SEPARATOR', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'MINIMUM_LIQUIDITY', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'PERMIT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'burn', 'outputs': [{'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'factory', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getReserves', 'outputs': [{'internalType': 'uint112', 'name': '_reserve0', 'type': 'uint112'}, {'internalType': 'uint112', 'name': '_reserve1', 'type': 'uint112'}, {'internalType': 'uint32', 'name': '_blockTimestampLast', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_token0', 'type': 'address'}, {'internalType': 'address', 'name': '_token1', 'type': 'address'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'kLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': 'liquidity', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'price0CumulativeLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'price1CumulativeLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'skim', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amount0Out', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1Out', 'type': 'uint256'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'swap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'sync', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'token0', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'token1', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}]        
        self.contract = self.web3.eth.contract(addr, abi=self.abi)

    def DOMAIN_SEPARATOR(self):

        """
        Args:
            None

        Returns:
            DOMAIN_SEPARATOR_OUTPUT_0 (bytes32)

        """
        output = self.contract.functions.DOMAIN_SEPARATOR().call()
        output_items={}
        self.DOMAIN_SEPARATOR_OUTPUT_0 = output
        output_items = output
        return output_items


    def MINIMUM_LIQUIDITY(self):

        """
        Args:
            None

        Returns:
            MINIMUM_LIQUIDITY_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.MINIMUM_LIQUIDITY().call()
        output_items={}
        self.MINIMUM_LIQUIDITY_OUTPUT_0 = output
        output_items = output
        return output_items


    def PERMIT_TYPEHASH(self):

        """
        Args:
            None

        Returns:
            PERMIT_TYPEHASH_OUTPUT_0 (bytes32)

        """
        output = self.contract.functions.PERMIT_TYPEHASH().call()
        output_items={}
        self.PERMIT_TYPEHASH_OUTPUT_0 = output
        output_items = output
        return output_items


    def allowance(self, INPUT_0, INPUT_1):
        """
        Args:
            INPUT_0 (address)
            INPUT_0 (address)

        Returns:
            allowance_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.allowance(INPUT_0, INPUT_1, ).call()
        output_items={}
        self.allowance_OUTPUT_0 = output
        output_items = output
        return output_items


    def approve(self, spender, value):
        """
        Args:
            spender (address)
            value (uint256)

        Returns:
            approve_OUTPUT_0 (bool)

        """
        output = self.contract.functions.approve(spender, value, ).call()
        output_items={}
        self.approve_OUTPUT_0 = output
        output_items = output
        return output_items


    def balanceOf(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            balanceOf_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.balanceOf(INPUT_0, ).call()
        output_items={}
        self.balanceOf_OUTPUT_0 = output
        output_items = output
        return output_items


    def burn(self, to):
        """
        Args:
            to (address)

        Returns:
            amount0 (uint256)
            amount1 (uint256)

        """
        output = self.contract.functions.burn(to, ).call()
        output_items={}
        self.amount0 = output[0]
        output_items["amount0"] = output[0]
        self.amount1 = output[1]
        output_items["amount1"] = output[1]
        return output_items


    def decimals(self):

        """
        Args:
            None

        Returns:
            decimals_OUTPUT_0 (uint8)

        """
        output = self.contract.functions.decimals().call()
        output_items={}
        self.decimals_OUTPUT_0 = output
        output_items = output
        return output_items


    def factory(self):

        """
        Args:
            None

        Returns:
            factory_OUTPUT_0 (address)

        """
        output = self.contract.functions.factory().call()
        output_items={}
        self.factory_OUTPUT_0 = output
        output_items = output
        return output_items


    def getReserves(self):

        """
        Args:
            None

        Returns:
            _reserve0 (uint112)
            _reserve1 (uint112)
            _blockTimestampLast (uint32)

        """
        output = self.contract.functions.getReserves().call()
        output_items={}
        self._reserve0 = output[0]
        output_items["_reserve0"] = output[0]
        self._reserve1 = output[1]
        output_items["_reserve1"] = output[1]
        self._blockTimestampLast = output[2]
        output_items["_blockTimestampLast"] = output[2]
        return output_items


    def initialize(self, _token0, _token1):
        """
        Args:
            _token0 (address)
            _token1 (address)

        Returns:
            None

        """
        output = self.contract.functions.initialize(_token0, _token1, ).call()
        output_items={}
        return output_items


    def kLast(self):

        """
        Args:
            None

        Returns:
            kLast_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.kLast().call()
        output_items={}
        self.kLast_OUTPUT_0 = output
        output_items = output
        return output_items


    def mint(self, to):
        """
        Args:
            to (address)

        Returns:
            liquidity (uint256)

        """
        output = self.contract.functions.mint(to, ).call()
        output_items={}
        self.liquidity = output
        output_items = output
        return output_items


    def name(self):

        """
        Args:
            None

        Returns:
            name_OUTPUT_0 (string)

        """
        output = self.contract.functions.name().call()
        output_items={}
        self.name_OUTPUT_0 = output
        output_items = output
        return output_items


    def nonces(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            nonces_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.nonces(INPUT_0, ).call()
        output_items={}
        self.nonces_OUTPUT_0 = output
        output_items = output
        return output_items


    def permit(self, owner, spender, value, deadline, v, r, s):
        """
        Args:
            owner (address)
            spender (address)
            value (uint256)
            deadline (uint256)
            v (uint8)
            r (bytes32)
            s (bytes32)

        Returns:
            None

        """
        output = self.contract.functions.permit(owner, spender, value, deadline, v, r, s, ).call()
        output_items={}
        return output_items


    def price0CumulativeLast(self):

        """
        Args:
            None

        Returns:
            price0CumulativeLast_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.price0CumulativeLast().call()
        output_items={}
        self.price0CumulativeLast_OUTPUT_0 = output
        output_items = output
        return output_items


    def price1CumulativeLast(self):

        """
        Args:
            None

        Returns:
            price1CumulativeLast_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.price1CumulativeLast().call()
        output_items={}
        self.price1CumulativeLast_OUTPUT_0 = output
        output_items = output
        return output_items


    def skim(self, to):
        """
        Args:
            to (address)

        Returns:
            None

        """
        output = self.contract.functions.skim(to, ).call()
        output_items={}
        return output_items


    def swap(self, amount0Out, amount1Out, to, data):
        """
        Args:
            amount0Out (uint256)
            amount1Out (uint256)
            to (address)
            data (bytes)

        Returns:
            None

        """
        output = self.contract.functions.swap(amount0Out, amount1Out, to, data, ).call()
        output_items={}
        return output_items


    def symbol(self):

        """
        Args:
            None

        Returns:
            symbol_OUTPUT_0 (string)

        """
        output = self.contract.functions.symbol().call()
        output_items={}
        self.symbol_OUTPUT_0 = output
        output_items = output
        return output_items


    def sync(self):

        """
        Args:
            None

        Returns:
            None

        """
        output = self.contract.functions.sync().call()
        output_items={}
        return output_items


    def token0(self):

        """
        Args:
            None

        Returns:
            token0_OUTPUT_0 (address)

        """
        output = self.contract.functions.token0().call()
        output_items={}
        self.token0_OUTPUT_0 = output
        output_items = output
        return output_items


    def token1(self):

        """
        Args:
            None

        Returns:
            token1_OUTPUT_0 (address)

        """
        output = self.contract.functions.token1().call()
        output_items={}
        self.token1_OUTPUT_0 = output
        output_items = output
        return output_items


    def totalSupply(self):

        """
        Args:
            None

        Returns:
            totalSupply_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.totalSupply().call()
        output_items={}
        self.totalSupply_OUTPUT_0 = output
        output_items = output
        return output_items


    def transfer(self, to, value):
        """
        Args:
            to (address)
            value (uint256)

        Returns:
            transfer_OUTPUT_0 (bool)

        """
        output = self.contract.functions.transfer(to, value, ).call()
        output_items={}
        self.transfer_OUTPUT_0 = output
        output_items = output
        return output_items


    def transferFrom(self, from_, to, value):
        """
        Args:
            from_ (address)
            to (address)
            value (uint256)

        Returns:
            transferFrom_OUTPUT_0 (bool)

        """
        output = self.contract.functions.transferFrom(from_, to, value, ).call()
        output_items={}
        self.transferFrom_OUTPUT_0 = output
        output_items = output
        return output_items

