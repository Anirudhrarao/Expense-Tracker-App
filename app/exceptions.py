class NoDataError(Exception):
    """
    Custom exception for missing data
    """
    def __init__(self, message = "No data available") -> None:
        self.message = message
        super().__init__(self.message)
        