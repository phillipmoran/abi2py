class standard_erc20:
    def __init__(self, web3_connection, addr):
        self.web3 = web3_connection
        self.addr = addr
        self.abi = [{'constant': True, 'inputs': [], 'name': 'name', 'outputs': [{'name': '', 'type': 'string'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_upgradedAddress', 'type': 'address'}], 'name': 'deprecate', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_spender', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'deprecated', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_evilUser', 'type': 'address'}], 'name': 'addBlackList', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'totalSupply', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_from', 'type': 'address'}, {'name': '_to', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'upgradedAddress', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '', 'type': 'address'}], 'name': 'balances', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'decimals', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'maximumFee', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': '_totalSupply', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'unpause', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '_maker', 'type': 'address'}], 'name': 'getBlackListStatus', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '', 'type': 'address'}, {'name': '', 'type': 'address'}], 'name': 'allowed', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'paused', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'who', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'pause', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'getOwner', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'owner', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'symbol', 'outputs': [{'name': '', 'type': 'string'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_to', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'newBasisPoints', 'type': 'uint256'}, {'name': 'newMaxFee', 'type': 'uint256'}], 'name': 'setParams', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'amount', 'type': 'uint256'}], 'name': 'issue', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'amount', 'type': 'uint256'}], 'name': 'redeem', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '_owner', 'type': 'address'}, {'name': '_spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'name': 'remaining', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'basisPointsRate', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [{'name': '', 'type': 'address'}], 'name': 'isBlackListed', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_clearedUser', 'type': 'address'}], 'name': 'removeBlackList', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'MAX_UINT', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'newOwner', 'type': 'address'}], 'name': 'transferOwnership', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_blackListedUser', 'type': 'address'}], 'name': 'destroyBlackFunds', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'name': '_initialSupply', 'type': 'uint256'}, {'name': '_name', 'type': 'string'}, {'name': '_symbol', 'type': 'string'}, {'name': '_decimals', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'amount', 'type': 'uint256'}], 'name': 'Issue', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'amount', 'type': 'uint256'}], 'name': 'Redeem', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'newAddress', 'type': 'address'}], 'name': 'Deprecate', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': 'feeBasisPoints', 'type': 'uint256'}, {'indexed': False, 'name': 'maxFee', 'type': 'uint256'}], 'name': 'Params', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': '_blackListedUser', 'type': 'address'}, {'indexed': False, 'name': '_balance', 'type': 'uint256'}], 'name': 'DestroyedBlackFunds', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': '_user', 'type': 'address'}], 'name': 'AddedBlackList', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'name': '_user', 'type': 'address'}], 'name': 'RemovedBlackList', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'owner', 'type': 'address'}, {'indexed': True, 'name': 'spender', 'type': 'address'}, {'indexed': False, 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'name': 'from', 'type': 'address'}, {'indexed': True, 'name': 'to', 'type': 'address'}, {'indexed': False, 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'Pause', 'type': 'event'}, {'anonymous': False, 'inputs': [], 'name': 'Unpause', 'type': 'event'}]        
        self.contract = self.web3.eth.contract(addr, abi=self.abi)

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


    def deprecate(self, _upgradedAddress):
        """
        Args:
            _upgradedAddress (address)

        Returns:
            None

        """
        output = self.contract.functions.deprecate(_upgradedAddress, ).call()
        output_items={}
        return output_items


    def approve(self, _spender, _value):
        """
        Args:
            _spender (address)
            _value (uint256)

        Returns:
            None

        """
        output = self.contract.functions.approve(_spender, _value, ).call()
        output_items={}
        return output_items


    def deprecated(self):

        """
        Args:
            None

        Returns:
            deprecated_OUTPUT_0 (bool)

        """
        output = self.contract.functions.deprecated().call()
        output_items={}
        self.deprecated_OUTPUT_0 = output
        output_items = output
        return output_items


    def addBlackList(self, _evilUser):
        """
        Args:
            _evilUser (address)

        Returns:
            None

        """
        output = self.contract.functions.addBlackList(_evilUser, ).call()
        output_items={}
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


    def transferFrom(self, _from, _to, _value):
        """
        Args:
            _from (address)
            _to (address)
            _value (uint256)

        Returns:
            None

        """
        output = self.contract.functions.transferFrom(_from, _to, _value, ).call()
        output_items={}
        return output_items


    def upgradedAddress(self):

        """
        Args:
            None

        Returns:
            upgradedAddress_OUTPUT_0 (address)

        """
        output = self.contract.functions.upgradedAddress().call()
        output_items={}
        self.upgradedAddress_OUTPUT_0 = output
        output_items = output
        return output_items


    def balances(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            balances_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.balances(INPUT_0, ).call()
        output_items={}
        self.balances_OUTPUT_0 = output
        output_items = output
        return output_items


    def decimals(self):

        """
        Args:
            None

        Returns:
            decimals_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.decimals().call()
        output_items={}
        self.decimals_OUTPUT_0 = output
        output_items = output
        return output_items


    def maximumFee(self):

        """
        Args:
            None

        Returns:
            maximumFee_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.maximumFee().call()
        output_items={}
        self.maximumFee_OUTPUT_0 = output
        output_items = output
        return output_items


    def _totalSupply(self):

        """
        Args:
            None

        Returns:
            _totalSupply_OUTPUT_0 (uint256)

        """
        output = self.contract.functions._totalSupply().call()
        output_items={}
        self._totalSupply_OUTPUT_0 = output
        output_items = output
        return output_items


    def unpause(self):

        """
        Args:
            None

        Returns:
            None

        """
        output = self.contract.functions.unpause().call()
        output_items={}
        return output_items


    def getBlackListStatus(self, _maker):
        """
        Args:
            _maker (address)

        Returns:
            getBlackListStatus_OUTPUT_0 (bool)

        """
        output = self.contract.functions.getBlackListStatus(_maker, ).call()
        output_items={}
        self.getBlackListStatus_OUTPUT_0 = output
        output_items = output
        return output_items


    def allowed(self, INPUT_0, INPUT_1):
        """
        Args:
            INPUT_0 (address)
            INPUT_0 (address)

        Returns:
            allowed_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.allowed(INPUT_0, INPUT_1, ).call()
        output_items={}
        self.allowed_OUTPUT_0 = output
        output_items = output
        return output_items


    def paused(self):

        """
        Args:
            None

        Returns:
            paused_OUTPUT_0 (bool)

        """
        output = self.contract.functions.paused().call()
        output_items={}
        self.paused_OUTPUT_0 = output
        output_items = output
        return output_items


    def balanceOf(self, who):
        """
        Args:
            who (address)

        Returns:
            balanceOf_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.balanceOf(who, ).call()
        output_items={}
        self.balanceOf_OUTPUT_0 = output
        output_items = output
        return output_items


    def pause(self):

        """
        Args:
            None

        Returns:
            None

        """
        output = self.contract.functions.pause().call()
        output_items={}
        return output_items


    def getOwner(self):

        """
        Args:
            None

        Returns:
            getOwner_OUTPUT_0 (address)

        """
        output = self.contract.functions.getOwner().call()
        output_items={}
        self.getOwner_OUTPUT_0 = output
        output_items = output
        return output_items


    def owner(self):

        """
        Args:
            None

        Returns:
            owner_OUTPUT_0 (address)

        """
        output = self.contract.functions.owner().call()
        output_items={}
        self.owner_OUTPUT_0 = output
        output_items = output
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


    def transfer(self, _to, _value):
        """
        Args:
            _to (address)
            _value (uint256)

        Returns:
            None

        """
        output = self.contract.functions.transfer(_to, _value, ).call()
        output_items={}
        return output_items


    def setParams(self, newBasisPoints, newMaxFee):
        """
        Args:
            newBasisPoints (uint256)
            newMaxFee (uint256)

        Returns:
            None

        """
        output = self.contract.functions.setParams(newBasisPoints, newMaxFee, ).call()
        output_items={}
        return output_items


    def issue(self, amount):
        """
        Args:
            amount (uint256)

        Returns:
            None

        """
        output = self.contract.functions.issue(amount, ).call()
        output_items={}
        return output_items


    def redeem(self, amount):
        """
        Args:
            amount (uint256)

        Returns:
            None

        """
        output = self.contract.functions.redeem(amount, ).call()
        output_items={}
        return output_items


    def allowance(self, _owner, _spender):
        """
        Args:
            _owner (address)
            _spender (address)

        Returns:
            remaining (uint256)

        """
        output = self.contract.functions.allowance(_owner, _spender, ).call()
        output_items={}
        self.remaining = output
        output_items = output
        return output_items


    def basisPointsRate(self):

        """
        Args:
            None

        Returns:
            basisPointsRate_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.basisPointsRate().call()
        output_items={}
        self.basisPointsRate_OUTPUT_0 = output
        output_items = output
        return output_items


    def isBlackListed(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            isBlackListed_OUTPUT_0 (bool)

        """
        output = self.contract.functions.isBlackListed(INPUT_0, ).call()
        output_items={}
        self.isBlackListed_OUTPUT_0 = output
        output_items = output
        return output_items


    def removeBlackList(self, _clearedUser):
        """
        Args:
            _clearedUser (address)

        Returns:
            None

        """
        output = self.contract.functions.removeBlackList(_clearedUser, ).call()
        output_items={}
        return output_items


    def MAX_UINT(self):

        """
        Args:
            None

        Returns:
            MAX_UINT_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.MAX_UINT().call()
        output_items={}
        self.MAX_UINT_OUTPUT_0 = output
        output_items = output
        return output_items


    def transferOwnership(self, newOwner):
        """
        Args:
            newOwner (address)

        Returns:
            None

        """
        output = self.contract.functions.transferOwnership(newOwner, ).call()
        output_items={}
        return output_items


    def destroyBlackFunds(self, _blackListedUser):
        """
        Args:
            _blackListedUser (address)

        Returns:
            None

        """
        output = self.contract.functions.destroyBlackFunds(_blackListedUser, ).call()
        output_items={}
        return output_items

