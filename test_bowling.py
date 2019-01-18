from bowling import score


def test_no_strikes_no_spares():
    result = '34 34 34 34 34 34 34 34 34 34 '
    assert score(result) == 70
    result = '35 35 35 35 35 35 35 35 35 35 '
    assert score(result) == 80

def test_misses():
    result = '30 30 30 30 30 30 30 30 30 30 '
    assert score(result) == 30

def test_spare():
    result = '3/ 10 10 00 00 00 00 00 00 00 '
    assert score(result) == 3 + 10 + 1 + 1 + 0
