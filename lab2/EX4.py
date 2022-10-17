# --------EX4: compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]------

def compose(musical_notes, moves, start):
    song = [musical_notes[start]]
    current_pos = start
    for move in moves:
        current_pos += move
        song.append(musical_notes[current_pos % len(musical_notes)])
    return song


def main():
    print(compose(['do', 're', 'mi', 'fa', 'sol'], [1, -3, 4, 2], 2))


if __name__ == '__main__':
    main()
