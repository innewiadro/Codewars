def sing():
    song = []
    for i in range(99, 0, -1):
        b1 = "bottle" if i == 1 else "bottles"
        b2 = "bottle" if i-1 == 1 else "bottles"
        next_b = f"{i-1} {b2}" if i > 1 else "no more bottles"
        song.append(f"{i} {b1} of beer on the wall, {i} {b1} of beer.")
        song.append(f"Take one down and pass it around, {next_b} of beer on the wall.")
    song.append("No more bottles of beer on the wall, no more bottles of beer.")
    song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return song