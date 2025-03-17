class BankAccount:
    """银行账户类，支持存款、取款操作。
    Attributes:
        account_number (str): 账户号码
        balance (float): 当前余额
    """
    def deposit(self, amount):
        """存款操作。
        Args:
            amount (float): 存款金额（需大于0）
        Raises:
            ValueError: 当金额无效时抛出
        """
        if amount <= 0:
            raise ValueError("金额必须大于0")
        self.balance += amount
if __name__ == "__main__":
    help(BankAccount)       