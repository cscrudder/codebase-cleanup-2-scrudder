from app.utils import to_usd

def test_to_usd():
    assert to_usd(0) == "$0.00"
    assert to_usd(1) == "$1.00"
    assert to_usd(0.009) == "$0.01"
    assert to_usd(1000) == "$1,000.00"
    assert to_usd(1234567.89) == "$1,234,567.89"

