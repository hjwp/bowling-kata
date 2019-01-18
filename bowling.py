def score(frames):
    return sum(
        int(roll1) + int(roll2)
        for roll1, roll2 in frames.split()
    )
