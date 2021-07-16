class DMM_POOL_ABI:
    def __init__(self, web3_connection, addr):
        self.web3 = web3_connection
        self.addr = addr
        self.abi = [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'Burn', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'name': 'Mint', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0In', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1In', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0Out', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1Out', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'feeInPrecision', 'type': 'uint256'}], 'name': 'Swap', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'vReserve0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'vReserve1', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'reserve0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'reserve1', 'type': 'uint256'}], 'name': 'Sync', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'shortEMA', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'longEMA', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint128', 'name': 'lastBlockVolume', 'type': 'uint128'}, {'indexed': False, 'internalType': 'uint256', 'name': 'skipBlock', 'type': 'uint256'}], 'name': 'UpdateEMA', 'type': 'event'}, {'inputs': [], 'name': 'MINIMUM_LIQUIDITY', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'PERMIT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'ampBps', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'burn', 'outputs': [{'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'domainSeparator', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'factory', 'outputs': [{'internalType': 'contract IDMMFactory', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getReserves', 'outputs': [{'internalType': 'uint112', 'name': '_reserve0', 'type': 'uint112'}, {'internalType': 'uint112', 'name': '_reserve1', 'type': 'uint112'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getTradeInfo', 'outputs': [{'internalType': 'uint112', 'name': '_reserve0', 'type': 'uint112'}, {'internalType': 'uint112', 'name': '_reserve1', 'type': 'uint112'}, {'internalType': 'uint112', 'name': '_vReserve0', 'type': 'uint112'}, {'internalType': 'uint112', 'name': '_vReserve1', 'type': 'uint112'}, {'internalType': 'uint256', 'name': 'feeInPrecision', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getVolumeTrendData', 'outputs': [{'internalType': 'uint128', 'name': '_shortEMA', 'type': 'uint128'}, {'internalType': 'uint128', 'name': '_longEMA', 'type': 'uint128'}, {'internalType': 'uint128', 'name': '_currentBlockVolume', 'type': 'uint128'}, {'internalType': 'uint128', 'name': '_lastTradeBlock', 'type': 'uint128'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20', 'name': '_token0', 'type': 'address'}, {'internalType': 'contract IERC20', 'name': '_token1', 'type': 'address'}, {'internalType': 'uint32', 'name': '_ampBps', 'type': 'uint32'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'kLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': 'liquidity', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'skim', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amount0Out', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1Out', 'type': 'uint256'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'bytes', 'name': 'callbackData', 'type': 'bytes'}], 'name': 'swap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'sync', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'token0', 'outputs': [{'internalType': 'contract IERC20', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'token1', 'outputs': [{'internalType': 'contract IERC20', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}]        
        self.contract = self.web3.eth.contract(addr, abi=self.abi)

    def MINIMUM_LIQUIDITY(self):

        """
        Args:
            None

        Returns:
            MINIMUM_LIQUIDITY_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.MINIMUM_LIQUIDITY().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.MINIMUM_LIQUIDITY_OUTPUT_0 = output[0]
        output_dict["MINIMUM_LIQUIDITY_OUTPUT_0"] = output[0]
        return output_dict


    def PERMIT_TYPEHASH(self):

        """
        Args:
            None

        Returns:
            PERMIT_TYPEHASH_OUTPUT_0 (bytes32)

        """
        output = self.contract.functions.PERMIT_TYPEHASH().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.PERMIT_TYPEHASH_OUTPUT_0 = output[0]
        output_dict["PERMIT_TYPEHASH_OUTPUT_0"] = output[0]
        return output_dict


    def allowance(self, owner, spender):
        """
        Args:
            owner (address)
            spender (address)

        Returns:
            allowance_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.allowance(owner, spender, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.allowance_OUTPUT_0 = output[0]
        output_dict["allowance_OUTPUT_0"] = output[0]
        return output_dict


    def ampBps(self):

        """
        Args:
            None

        Returns:
            ampBps_OUTPUT_0 (uint32)

        """
        output = self.contract.functions.ampBps().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.ampBps_OUTPUT_0 = output[0]
        output_dict["ampBps_OUTPUT_0"] = output[0]
        return output_dict


    def approve(self, spender, amount):
        """
        Args:
            spender (address)
            amount (uint256)

        Returns:
            approve_OUTPUT_0 (bool)

        """
        output = self.contract.functions.approve(spender, amount, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.approve_OUTPUT_0 = output[0]
        output_dict["approve_OUTPUT_0"] = output[0]
        return output_dict


    def balanceOf(self, account):
        """
        Args:
            account (address)

        Returns:
            balanceOf_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.balanceOf(account, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.balanceOf_OUTPUT_0 = output[0]
        output_dict["balanceOf_OUTPUT_0"] = output[0]
        return output_dict


    def burn(self, to):
        """
        Args:
            to (address)

        Returns:
            amount0 (uint256)
            amount1 (uint256)

        """
        output = self.contract.functions.burn(to, ).call()
        output_dict={}
        return output_dict


    def decimals(self):

        """
        Args:
            None

        Returns:
            decimals_OUTPUT_0 (uint8)

        """
        output = self.contract.functions.decimals().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.decimals_OUTPUT_0 = output[0]
        output_dict["decimals_OUTPUT_0"] = output[0]
        return output_dict


    def decreaseAllowance(self, spender, subtractedValue):
        """
        Args:
            spender (address)
            subtractedValue (uint256)

        Returns:
            decreaseAllowance_OUTPUT_0 (bool)

        """
        output = self.contract.functions.decreaseAllowance(spender, subtractedValue, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.decreaseAllowance_OUTPUT_0 = output[0]
        output_dict["decreaseAllowance_OUTPUT_0"] = output[0]
        return output_dict


    def domainSeparator(self):

        """
        Args:
            None

        Returns:
            domainSeparator_OUTPUT_0 (bytes32)

        """
        output = self.contract.functions.domainSeparator().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.domainSeparator_OUTPUT_0 = output[0]
        output_dict["domainSeparator_OUTPUT_0"] = output[0]
        return output_dict


    def factory(self):

        """
        Args:
            None

        Returns:
            factory_OUTPUT_0 (address)

        """
        output = self.contract.functions.factory().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.factory_OUTPUT_0 = output[0]
        output_dict["factory_OUTPUT_0"] = output[0]
        return output_dict


    def getReserves(self):

        """
        Args:
            None

        Returns:
            _reserve0 (uint112)
            _reserve1 (uint112)

        """
        output = self.contract.functions.getReserves().call()
        output_dict={}
        return output_dict


    def getTradeInfo(self):

        """
        Args:
            None

        Returns:
            _reserve0 (uint112)
            _reserve1 (uint112)
            _vReserve0 (uint112)
            _vReserve1 (uint112)
            feeInPrecision (uint256)

        """
        output = self.contract.functions.getTradeInfo().call()
        output_dict={}
        return output_dict


    def getVolumeTrendData(self):

        """
        Args:
            None

        Returns:
            _shortEMA (uint128)
            _longEMA (uint128)
            _currentBlockVolume (uint128)
            _lastTradeBlock (uint128)

        """
        output = self.contract.functions.getVolumeTrendData().call()
        output_dict={}
        return output_dict


    def increaseAllowance(self, spender, addedValue):
        """
        Args:
            spender (address)
            addedValue (uint256)

        Returns:
            increaseAllowance_OUTPUT_0 (bool)

        """
        output = self.contract.functions.increaseAllowance(spender, addedValue, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.increaseAllowance_OUTPUT_0 = output[0]
        output_dict["increaseAllowance_OUTPUT_0"] = output[0]
        return output_dict


    def initialize(self, _token0, _token1, _ampBps):
        """
        Args:
            _token0 (address)
            _token1 (address)
            _ampBps (uint32)

        Returns:
            None

        """
        output = self.contract.functions.initialize(_token0, _token1, _ampBps, ).call()
        output_dict={}
        return output_dict


    def kLast(self):

        """
        Args:
            None

        Returns:
            kLast_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.kLast().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.kLast_OUTPUT_0 = output[0]
        output_dict["kLast_OUTPUT_0"] = output[0]
        return output_dict


    def mint(self, to):
        """
        Args:
            to (address)

        Returns:
            liquidity (uint256)

        """
        output = self.contract.functions.mint(to, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        return output_dict


    def name(self):

        """
        Args:
            None

        Returns:
            name_OUTPUT_0 (string)

        """
        output = self.contract.functions.name().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.name_OUTPUT_0 = output[0]
        output_dict["name_OUTPUT_0"] = output[0]
        return output_dict


    def nonces(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            nonces_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.nonces(INPUT_0, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.nonces_OUTPUT_0 = output[0]
        output_dict["nonces_OUTPUT_0"] = output[0]
        return output_dict


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
        output_dict={}
        return output_dict


    def skim(self, to):
        """
        Args:
            to (address)

        Returns:
            None

        """
        output = self.contract.functions.skim(to, ).call()
        output_dict={}
        return output_dict


    def swap(self, amount0Out, amount1Out, to, callbackData):
        """
        Args:
            amount0Out (uint256)
            amount1Out (uint256)
            to (address)
            callbackData (bytes)

        Returns:
            None

        """
        output = self.contract.functions.swap(amount0Out, amount1Out, to, callbackData, ).call()
        output_dict={}
        return output_dict


    def symbol(self):

        """
        Args:
            None

        Returns:
            symbol_OUTPUT_0 (string)

        """
        output = self.contract.functions.symbol().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.symbol_OUTPUT_0 = output[0]
        output_dict["symbol_OUTPUT_0"] = output[0]
        return output_dict


    def sync(self):

        """
        Args:
            None

        Returns:
            None

        """
        output = self.contract.functions.sync().call()
        output_dict={}
        return output_dict


    def token0(self):

        """
        Args:
            None

        Returns:
            token0_OUTPUT_0 (address)

        """
        output = self.contract.functions.token0().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.token0_OUTPUT_0 = output[0]
        output_dict["token0_OUTPUT_0"] = output[0]
        return output_dict


    def token1(self):

        """
        Args:
            None

        Returns:
            token1_OUTPUT_0 (address)

        """
        output = self.contract.functions.token1().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.token1_OUTPUT_0 = output[0]
        output_dict["token1_OUTPUT_0"] = output[0]
        return output_dict


    def totalSupply(self):

        """
        Args:
            None

        Returns:
            totalSupply_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.totalSupply().call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.totalSupply_OUTPUT_0 = output[0]
        output_dict["totalSupply_OUTPUT_0"] = output[0]
        return output_dict


    def transfer(self, recipient, amount):
        """
        Args:
            recipient (address)
            amount (uint256)

        Returns:
            transfer_OUTPUT_0 (bool)

        """
        output = self.contract.functions.transfer(recipient, amount, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.transfer_OUTPUT_0 = output[0]
        output_dict["transfer_OUTPUT_0"] = output[0]
        return output_dict


    def transferFrom(self, sender, recipient, amount):
        """
        Args:
            sender (address)
            recipient (address)
            amount (uint256)

        Returns:
            transferFrom_OUTPUT_0 (bool)

        """
        output = self.contract.functions.transferFrom(sender, recipient, amount, ).call()
        output_list = []
        output_list.append(output)
        output=output_list
        output_dict={}
        self.transferFrom_OUTPUT_0 = output[0]
        output_dict["transferFrom_OUTPUT_0"] = output[0]
        return output_dict

