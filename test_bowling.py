from bowling import score


def test_no_strikes_no_spares():
    result = '34 34 34 34 34 34 34 34 34 34 '
    assert score(result) == 70
    result = '35 35 35 35 35 35 35 35 35 35 '
    assert score(result) == 80


def test_misses():
    result = '30 30 30 30 30 30 30 30 30 30 '
    assert score(result) == 30


def test1_spare():
    result = '3/ 12 34 00 00 00 00 00 00 00 '
    expected = (10 + 1) + (1 + 2) + (3 + 4)
    assert score(result) == expected

def test2_spare():
    result = '2/ 9/ 12 00 00 00 00 00 00 00 '
    expected = (10 + 9) + (10 + 1) + (1 + 2)
    assert score(result) == expected


def test_strike():
    result = 'XX 12 34 00 00 00 00 00 00 00 '
    expected = (10 + 1 + 2 + 3 + 4) + (1 + 2) + (3 + 4)
    assert score(result) == expected

