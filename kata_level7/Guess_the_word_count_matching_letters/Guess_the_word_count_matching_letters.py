def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise ValueError("Words must have the same length")

    count = 0
    for i in range(len(correct)):
        if correct[i] == guess[i]:
            count += 1

    return count