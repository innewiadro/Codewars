def can_play(hand, face_up):
    if not hand:
        return False

    face_color, face_number = face_up.split()

    for card in hand:
        color, number = card.split()
        if color == face_color or number == face_number:
            return True

    return False
