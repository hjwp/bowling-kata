from bowling import score


def test_no_strikes_no_spares():
    result = '34 34 34 34 34 34 34 34 34 34 '
    assert score(result) == 70
    result = '35 35 35 35 35 35 35 35 35 35 '
    assert score(result) == 80

def test_including_misses():
    result = '30 30 30 30 30 30 30 30 30 30 '
    assert score(result) == 30
