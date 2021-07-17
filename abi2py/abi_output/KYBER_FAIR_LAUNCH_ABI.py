class KYBER_FAIR_LAUNCH_ABI:
    def __init__(self, web3_connection, addr):
        self.web3 = web3_connection
        self.addr = addr
        self.abi = [{'inputs': [{'internalType': 'address', 'name': '_admin', 'type': 'address'}, {'internalType': 'address[]', 'name': '_rewardTokens', 'type': 'address[]'}, {'internalType': 'contract IKyberRewardLocker', 'name': '_rewardLocker', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'stakeToken', 'type': 'address'}, {'indexed': True, 'internalType': 'uint32', 'name': 'startBlock', 'type': 'uint32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'endBlock', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'rewardPerBlocks', 'type': 'uint256[]'}], 'name': 'AddNewPool', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'previousAdmin', 'type': 'address'}], 'name': 'AdminClaimed', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'user', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'pid', 'type': 'uint256'}, {'indexed': True, 'internalType': 'uint256', 'name': 'blockNumber', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Deposit', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'user', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'pid', 'type': 'uint256'}, {'indexed': True, 'internalType': 'uint256', 'name': 'blockNumber', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'EmergencyWithdraw', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'user', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'pid', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'rewardToken', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'lockedAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'blockNumber', 'type': 'uint256'}], 'name': 'Harvest', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'pid', 'type': 'uint256'}, {'indexed': True, 'internalType': 'uint32', 'name': 'startBlock', 'type': 'uint32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'endBlock', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'rewardPerBlocks', 'type': 'uint256[]'}], 'name': 'RenewPool', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'pendingAdmin', 'type': 'address'}], 'name': 'TransferAdminPending', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'pid', 'type': 'uint256'}, {'indexed': True, 'internalType': 'uint32', 'name': 'endBlock', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'rewardPerBlocks', 'type': 'uint256[]'}], 'name': 'UpdatePool', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'user', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'pid', 'type': 'uint256'}, {'indexed': True, 'internalType': 'uint256', 'name': 'blockNumber', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Withdraw', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': '_stakeToken', 'type': 'address'}, {'internalType': 'uint32', 'name': '_startBlock', 'type': 'uint32'}, {'internalType': 'uint32', 'name': '_endBlock', 'type': 'uint32'}, {'internalType': 'uint256[]', 'name': '_rewardPerBlocks', 'type': 'uint256[]'}], 'name': 'addPool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'admin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'rewardTokenIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'adminWithdraw', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'claimAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}, {'internalType': 'bool', 'name': '_shouldHarvest', 'type': 'bool'}], 'name': 'deposit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}], 'name': 'emergencyWithdraw', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}], 'name': 'getPoolInfo', 'outputs': [{'internalType': 'uint256', 'name': 'totalStake', 'type': 'uint256'}, {'internalType': 'address', 'name': 'stakeToken', 'type': 'address'}, {'internalType': 'uint32', 'name': 'startBlock', 'type': 'uint32'}, {'internalType': 'uint32', 'name': 'endBlock', 'type': 'uint32'}, {'internalType': 'uint32', 'name': 'lastRewardBlock', 'type': 'uint32'}, {'internalType': 'uint256[]', 'name': 'rewardPerBlocks', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': 'accRewardPerShares', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getRewardTokens', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}, {'internalType': 'address', 'name': '_account', 'type': 'address'}], 'name': 'getUserInfo', 'outputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256[]', 'name': 'unclaimedRewards', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': 'lastRewardPerShares', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}], 'name': 'harvest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256[]', 'name': '_pids', 'type': 'uint256[]'}], 'name': 'harvestMultiplePools', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'pendingAdmin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}, {'internalType': 'address', 'name': '_user', 'type': 'address'}], 'name': 'pendingRewards', 'outputs': [{'internalType': 'uint256[]', 'name': 'rewards', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'poolExists', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'poolLength', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}, {'internalType': 'uint32', 'name': '_startBlock', 'type': 'uint32'}, {'internalType': 'uint32', 'name': '_endBlock', 'type': 'uint32'}, {'internalType': 'uint256[]', 'name': '_rewardPerBlocks', 'type': 'uint256[]'}], 'name': 'renewPool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'rewardLocker', 'outputs': [{'internalType': 'contract IKyberRewardLocker', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'rewardTokens', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'transferAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'transferAdminQuickly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}, {'internalType': 'uint32', 'name': '_endBlock', 'type': 'uint32'}, {'internalType': 'uint256[]', 'name': '_rewardPerBlocks', 'type': 'uint256[]'}], 'name': 'updatePool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}], 'name': 'updatePoolRewards', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_pid', 'type': 'uint256'}], 'name': 'withdrawAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'stateMutability': 'payable', 'type': 'receive'}]        
        self.contract = self.web3.eth.contract(addr, abi=self.abi)

    def addPool(self, _stakeToken, _startBlock, _endBlock, _rewardPerBlocks):
        """
        Args:
            _stakeToken (address)
            _startBlock (uint32)
            _endBlock (uint32)
            _rewardPerBlocks (uint256[])

        Returns:
            None

        """
        output = self.contract.functions.addPool(_stakeToken, _startBlock, _endBlock, _rewardPerBlocks, ).call()
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


    def adminWithdraw(self, rewardTokenIndex, amount):
        """
        Args:
            rewardTokenIndex (uint256)
            amount (uint256)

        Returns:
            None

        """
        output = self.contract.functions.adminWithdraw(rewardTokenIndex, amount, ).call()
        output_items={}
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


    def deposit(self, _pid, _amount, _shouldHarvest):
        """
        Args:
            _pid (uint256)
            _amount (uint256)
            _shouldHarvest (bool)

        Returns:
            None

        """
        output = self.contract.functions.deposit(_pid, _amount, _shouldHarvest, ).call()
        output_items={}
        return output_items


    def emergencyWithdraw(self, _pid):
        """
        Args:
            _pid (uint256)

        Returns:
            None

        """
        output = self.contract.functions.emergencyWithdraw(_pid, ).call()
        output_items={}
        return output_items


    def getPoolInfo(self, _pid):
        """
        Args:
            _pid (uint256)

        Returns:
            totalStake (uint256)
            stakeToken (address)
            startBlock (uint32)
            endBlock (uint32)
            lastRewardBlock (uint32)
            rewardPerBlocks (uint256[])
            accRewardPerShares (uint256[])

        """
        output = self.contract.functions.getPoolInfo(_pid, ).call()
        output_items={}
        self.totalStake = output[0]
        output_items["totalStake"] = output[0]
        self.stakeToken = output[1]
        output_items["stakeToken"] = output[1]
        self.startBlock = output[2]
        output_items["startBlock"] = output[2]
        self.endBlock = output[3]
        output_items["endBlock"] = output[3]
        self.lastRewardBlock = output[4]
        output_items["lastRewardBlock"] = output[4]
        self.rewardPerBlocks = output[5]
        output_items["rewardPerBlocks"] = output[5]
        self.accRewardPerShares = output[6]
        output_items["accRewardPerShares"] = output[6]
        return output_items


    def getRewardTokens(self):

        """
        Args:
            None

        Returns:
            getRewardTokens_OUTPUT_0 (address[])

        """
        output = self.contract.functions.getRewardTokens().call()
        output_items={}
        self.getRewardTokens_OUTPUT_0 = output
        output_items = output
        return output_items


    def getUserInfo(self, _pid, _account):
        """
        Args:
            _pid (uint256)
            _account (address)

        Returns:
            amount (uint256)
            unclaimedRewards (uint256[])
            lastRewardPerShares (uint256[])

        """
        output = self.contract.functions.getUserInfo(_pid, _account, ).call()
        output_items={}
        self.amount = output[0]
        output_items["amount"] = output[0]
        self.unclaimedRewards = output[1]
        output_items["unclaimedRewards"] = output[1]
        self.lastRewardPerShares = output[2]
        output_items["lastRewardPerShares"] = output[2]
        return output_items


    def harvest(self, _pid):
        """
        Args:
            _pid (uint256)

        Returns:
            None

        """
        output = self.contract.functions.harvest(_pid, ).call()
        output_items={}
        return output_items


    def harvestMultiplePools(self, _pids):
        """
        Args:
            _pids (uint256[])

        Returns:
            None

        """
        output = self.contract.functions.harvestMultiplePools(_pids, ).call()
        output_items={}
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


    def pendingRewards(self, _pid, _user):
        """
        Args:
            _pid (uint256)
            _user (address)

        Returns:
            rewards (uint256[])

        """
        output = self.contract.functions.pendingRewards(_pid, _user, ).call()
        output_items={}
        self.rewards = output
        output_items = output
        return output_items


    def poolExists(self, INPUT_0):
        """
        Args:
            INPUT_0 (address)

        Returns:
            poolExists_OUTPUT_0 (bool)

        """
        output = self.contract.functions.poolExists(INPUT_0, ).call()
        output_items={}
        self.poolExists_OUTPUT_0 = output
        output_items = output
        return output_items


    def poolLength(self):

        """
        Args:
            None

        Returns:
            poolLength_OUTPUT_0 (uint256)

        """
        output = self.contract.functions.poolLength().call()
        output_items={}
        self.poolLength_OUTPUT_0 = output
        output_items = output
        return output_items


    def renewPool(self, _pid, _startBlock, _endBlock, _rewardPerBlocks):
        """
        Args:
            _pid (uint256)
            _startBlock (uint32)
            _endBlock (uint32)
            _rewardPerBlocks (uint256[])

        Returns:
            None

        """
        output = self.contract.functions.renewPool(_pid, _startBlock, _endBlock, _rewardPerBlocks, ).call()
        output_items={}
        return output_items


    def rewardLocker(self):

        """
        Args:
            None

        Returns:
            rewardLocker_OUTPUT_0 (address)

        """
        output = self.contract.functions.rewardLocker().call()
        output_items={}
        self.rewardLocker_OUTPUT_0 = output
        output_items = output
        return output_items


    def rewardTokens(self, INPUT_0):
        """
        Args:
            INPUT_0 (uint256)

        Returns:
            rewardTokens_OUTPUT_0 (address)

        """
        output = self.contract.functions.rewardTokens(INPUT_0, ).call()
        output_items={}
        self.rewardTokens_OUTPUT_0 = output
        output_items = output
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


    def updatePool(self, _pid, _endBlock, _rewardPerBlocks):
        """
        Args:
            _pid (uint256)
            _endBlock (uint32)
            _rewardPerBlocks (uint256[])

        Returns:
            None

        """
        output = self.contract.functions.updatePool(_pid, _endBlock, _rewardPerBlocks, ).call()
        output_items={}
        return output_items


    def updatePoolRewards(self, _pid):
        """
        Args:
            _pid (uint256)

        Returns:
            None

        """
        output = self.contract.functions.updatePoolRewards(_pid, ).call()
        output_items={}
        return output_items


    def withdraw(self, _pid, _amount):
        """
        Args:
            _pid (uint256)
            _amount (uint256)

        Returns:
            None

        """
        output = self.contract.functions.withdraw(_pid, _amount, ).call()
        output_items={}
        return output_items


    def withdrawAll(self, _pid):
        """
        Args:
            _pid (uint256)

        Returns:
            None

        """
        output = self.contract.functions.withdrawAll(_pid, ).call()
        output_items={}
        return output_items

