class AccountNotFoundError(Exception):
    """Raised when account number is not found."""
    pass


class InvalidAmountError(Exception):
    """Raised when deposit/withdraw amount is invalid."""
    pass


class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass