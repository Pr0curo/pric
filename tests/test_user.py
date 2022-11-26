from ..user import User


def test_user_creation() -> None:
    user: User = User(name="Mike")


def test_user_name() -> None:
    user: User = User(name="Jan")
    assert user.name == "Jan"

