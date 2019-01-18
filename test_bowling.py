from bowling import score


def test_no_strikes_no_spares():
    result = '34 34 34 34 34 34 34 34 34 34 '
    assert score(result) == 70
