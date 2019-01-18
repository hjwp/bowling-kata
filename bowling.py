def score(frames):
    return sum([
        int(f[0]) + int(f[1])
        for f in frames.split()
    ])
