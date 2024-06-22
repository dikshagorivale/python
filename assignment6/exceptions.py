class CustomException(Exception):
    pass

class InvalidMenuItemError(CustomException):
    def __init__(self, name):
        super().__init__(f"Invalid menu item: {name}")

class InsufficientQuantityError(CustomException):
    def __init__(self, name):
        super().__init__(f"Insufficient quantity for item: {name}")

class DuplicateMenuItemError(CustomException):
    pass
