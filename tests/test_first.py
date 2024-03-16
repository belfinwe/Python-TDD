from src.app.first import plus_one, plus_two

def test_plus_one():
    assert plus_one(1) == 2, "Fail"


def test_plus_one_false():
    assert plus_one(1) != 3, "Fail"


def test_plus_two_main():
    assert plus_two(2) == 4, "Fail"


def test_plus_two_type():
    assert isinstance(plus_two(2), float), "Fail"
