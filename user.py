""" Represents a User """


class User:
    """Represents a User"""

    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name
