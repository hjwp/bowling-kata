def score(frames):
    result = 0
    last_was_spare, last_was_strike = False, False
    for roll1, roll2 in frames.split():
        if last_was_spare:
            result += int(roll1)
            last_was_spare = False
        if last_was_strike:
            result += int(roll1)
            last_was_strike = False

        if roll2 == '/':
            result += 10
            last_was_spare = True
        elif roll2 == 'X':
            result += 10
            last_was_strike = True
        else:
            result += int(roll1)
            result += int(roll2)
    return result
