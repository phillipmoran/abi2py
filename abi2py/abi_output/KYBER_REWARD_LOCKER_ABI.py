class KYBER_REWARD_LOCKER_ABI:
    def __init__(self, web3_connection, addr):
        self.web3 = web3_connection
        self.addr = addr
        self.abi = [{'inputs': [{'internalType': 'address', 'name': '_admin', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'previousAdmin', 'type': 'address'}], 'name': 'AdminClaimed', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'rewardContract', 'type': 'address'}, {'indexed': True, 'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isAdded', 'type': 'bool'}], 'name': 'RewardContractAdded', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint64', 'name': 'vestingDuration', 'type': 'uint64'}], 'name': 'SetVestingDuration', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'pendingAdmin', 'type': 'address'}], 'name': 'TransferAdminPending', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'beneficiary', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'vestedQuantity', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}], 'name': 'Vested', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'beneficiary', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'startBlock', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'endBlock', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'quantity', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}], 'name': 'VestingEntryCreated', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}, {'indexed': True, 'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'beneficiary', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'quantity', 'type': 'uint256'}], 'name': 'VestingEntryQueued', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'contract IERC20Ext', 'name': '', 'type': 'address'}], 'name': 'accountEscrowedBalance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'contract IERC20Ext', 'name': '', 'type': 'address'}], 'name': 'accountVestedBalance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': '_rewardContract', 'type': 'address'}], 'name': 'addRewardsContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'admin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'claimAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}], 'name': 'getRewardContractsPerToken', 'outputs': [{'internalType': 'address[]', 'name': 'rewardContracts', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}], 'name': 'getVestingScheduleAtIndex', 'outputs': [{'components': [{'internalType': 'uint64', 'name': 'startBlock', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endBlock', 'type': 'uint64'}, {'internalType': 'uint128', 'name': 'quantity', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'vestedQuantity', 'type': 'uint128'}], 'internalType': 'struct IKyberRewardLocker.VestingSchedule', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}], 'name': 'getVestingSchedules', 'outputs': [{'components': [{'internalType': 'uint64', 'name': 'startBlock', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endBlock', 'type': 'uint64'}, {'internalType': 'uint128', 'name': 'quantity', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'vestedQuantity', 'type': 'uint128'}], 'internalType': 'struct IKyberRewardLocker.VestingSchedule[]', 'name': 'schedules', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'quantity', 'type': 'uint256'}], 'name': 'lock', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'quantity', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'startBlock', 'type': 'uint256'}], 'name': 'lockWithStartBlock', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}], 'name': 'numVestingSchedules', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'pendingAdmin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': '_rewardContract', 'type': 'address'}], 'name': 'removeRewardsContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'uint64', 'name': '_vestingDuration', 'type': 'uint64'}], 'name': 'setVestingDuration', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'transferAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'transferAdminQuickly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}], 'name': 'vestCompletedSchedules', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext[]', 'name': 'tokens', 'type': 'address[]'}], 'name': 'vestCompletedSchedulesForMultipleTokens', 'outputs': [{'internalType': 'uint256[]', 'name': 'vestedAmounts', 'type': 'uint256[]'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'uint256[]', 'name': 'indexes', 'type': 'uint256[]'}], 'name': 'vestScheduleAtIndices', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext[]', 'name': 'tokens', 'type': 'address[]'}, {'internalType': 'uint256[][]', 'name': 'indices', 'type': 'uint256[][]'}], 'name': 'vestScheduleForMultipleTokensAtIndices', 'outputs': [{'internalType': 'uint256[]', 'name': 'vestedAmounts', 'type': 'uint256[]'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': 'token', 'type': 'address'}, {'internalType': 'uint256', 'name': 'startIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'endIndex', 'type': 'uint256'}], 'name': 'vestSchedulesInRange', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'contract IERC20Ext', 'name': '', 'type': 'address'}], 'name': 'vestingDurationPerToken', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]        
        self.contract = self.web3.eth.contract(addr, abi=self.abi)

    def accountEscrowedBalance(self, INPUT_0, INPUT_1):
        """
        Args:
            INPUT_0 (address)
            INPUT_0 (address)

        Returns:
            accountEscrowedBalance_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.accountEscrowedBalance(INPUT_0, INPUT_1, ).call()
        output_items={}
        self.accountEscrowedBalance_OUTPUT_0 = output
        output_items = output
        return output_items


    def accountVestedBalance(self, INPUT_0, INPUT_1):
        """
        Args:
            INPUT_0 (address)
            INPUT_0 (address)

        Returns:
            accountVestedBalance_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.accountVestedBalance(INPUT_0, INPUT_1, ).call()
        output_items={}
        self.accountVestedBalance_OUTPUT_0 = output
        output_items = output
        return output_items


    def addRewardsContract(self, token, _rewardContract):
        """
        Args:
            token (address)
            _rewardContract (address)

        Returns:
            None

        """
        output = self.contract.functions.addRewardsContract(token, _rewardContract, ).call()
        output_items={}
        return output_items


    def admin(self):

        """
        Args:
            None

        Returns:
            admin_OUTPUT_0 (address)

        """
        output = self.contract.functions.admin().call()
        output_items={}
        self.admin_OUTPUT_0 = output
        output_items = output
        return output_items


    def claimAdmin(self):

        """
        Args:
            None

        Returns:
            None

        """
        output = self.contract.functions.claimAdmin().call()
        output_items={}
        return output_items


    def getRewardContractsPerToken(self, token):
        """
        Args:
            token (address)

        Returns:
            rewardContracts (address[])

        """
        output = self.contract.functions.getRewardContractsPerToken(token, ).call()
        output_items={}
        self.rewardContracts = output
        output_items = output
        return output_items


    def getVestingScheduleAtIndex(self, account, token, index):
        """
        Args:
            account (address)
            token (address)
            index (uint256)

        Returns:
            getVestingScheduleAtIndex_OUTPUT_0 (tuple)

        """
        output = self.contract.functions.getVestingScheduleAtIndex(account, token, index, ).call()
        output_items={}
        self.getVestingScheduleAtIndex_OUTPUT_0 = output
        output_items = output
        return output_items


    def getVestingSchedules(self, account, token):
        """
        Args:
            account (address)
            token (address)

        Returns:
            schedules (tuple[])

        """
        output = self.contract.functions.getVestingSchedules(account, token, ).call()
        output_items={}
        self.schedules = output
        output_items = output
        return output_items


    def lock(self, token, account, quantity):
        """
        Args:
            token (address)
            account (address)
            quantity (uint256)

        Returns:
            None

        """
        output = self.contract.functions.lock(token, account, quantity, ).call()
        output_items={}
        return output_items


    def lockWithStartBlock(self, token, account, quantity, startBlock):
        """
        Args:
            token (address)
            account (address)
            quantity (uint256)
            startBlock (uint256)

        Returns:
            None

        """
        output = self.contract.functions.lockWithStartBlock(token, account, quantity, startBlock, ).call()
        output_items={}
        return output_items


    def numVestingSchedules(self, account, token):
        """
        Args:
            account (address)
            token (address)

        Returns:
            numVestingSchedules_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.numVestingSchedules(account, token, ).call()
        output_items={}
        self.numVestingSchedules_OUTPUT_0 = output
        output_items = output
        return output_items


    def pendingAdmin(self):

        """
        Args:
            None

        Returns:
            pendingAdmin_OUTPUT_0 (address)

        """
        output = self.contract.functions.pendingAdmin().call()
        output_items={}
        self.pendingAdmin_OUTPUT_0 = output
        output_items = output
        return output_items


    def removeRewardsContract(self, token, _rewardContract):
        """
        Args:
            token (address)
            _rewardContract (address)

        Returns:
            None

        """
        output = self.contract.functions.removeRewardsContract(token, _rewardContract, ).call()
        output_items={}
        return output_items


    def setVestingDuration(self, token, _vestingDuration):
        """
        Args:
            token (address)
            _vestingDuration (uint64)

        Returns:
            None

        """
        output = self.contract.functions.setVestingDuration(token, _vestingDuration, ).call()
        output_items={}
        return output_items


    def transferAdmin(self, newAdmin):
        """
        Args:
            newAdmin (address)

        Returns:
            None

        """
        output = self.contract.functions.transferAdmin(newAdmin, ).call()
        output_items={}
        return output_items


    def transferAdminQuickly(self, newAdmin):
        """
        Args:
            newAdmin (address)

        Returns:
            None

        """
        output = self.contract.functions.transferAdminQuickly(newAdmin, ).call()
        output_items={}
        return output_items


    def vestCompletedSchedules(self, token):
        """
        Args:
            token (address)

        Returns:
            vestCompletedSchedules_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.vestCompletedSchedules(token, ).call()
        output_items={}
        self.vestCompletedSchedules_OUTPUT_0 = output
        output_items = output
        return output_items


    def vestCompletedSchedulesForMultipleTokens(self, tokens):
        """
        Args:
            tokens (address[])

        Returns:
            vestedAmounts (uint256[])

        """
        output = self.contract.functions.vestCompletedSchedulesForMultipleTokens(tokens, ).call()
        output_items={}
        self.vestedAmounts = output
        output_items = output
        return output_items


    def vestScheduleAtIndices(self, token, indexes):
        """
        Args:
            token (address)
            indexes (uint256[])

        Returns:
            vestScheduleAtIndices_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.vestScheduleAtIndices(token, indexes, ).call()
        output_items={}
        self.vestScheduleAtIndices_OUTPUT_0 = output
        output_items = output
        return output_items


    def vestScheduleForMultipleTokensAtIndices(self, tokens, indices):
        """
        Args:
            tokens (address[])
            indices (uint256[][])

        Returns:
            vestedAmounts (uint256[])

        """
        output = self.contract.functions.vestScheduleForMultipleTokensAtIndices(tokens, indices, ).call()
        output_items={}
        self.vestedAmounts = output
        output_items = output
        return output_items


    def vestSchedulesInRange(self, token, startIndex, endIndex):
        """
        Args:
            token (address)
            startIndex (uint256)
            endIndex (uint256)

        Returns:
            vestSchedulesInRange_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.vestSchedulesInRange(token, startIndex, endIndex, ).call()
        output_items={}
        self.vestSchedulesInRange_OUTPUT_0 = output
        output_items = output
        return output_items


    def vestingDurationPerToken(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            vestingDurationPerToken_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.vestingDurationPerToken(INPUT_0, ).call()
        output_items={}
        self.vestingDurationPerToken_OUTPUT_0 = output
        output_items = output
        return output_items

