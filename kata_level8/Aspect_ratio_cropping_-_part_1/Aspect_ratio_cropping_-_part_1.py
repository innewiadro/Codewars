from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    new_x = math.ceil(y * 16 / 9)
    return new_x, y
