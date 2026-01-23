def solution(arr_val, arr_unit) :
    G = 6.67e-11

    mass_units = {
        "kg": 1,
        "g": 1e-3,
        "mg": 1e-6,
        "μg": 1e-9,
        "lb": 0.453592
    }

    distance_units = {
        "m": 1,
        "cm": 1e-2,
        "mm": 1e-3,
        "μm": 1e-6,
        "ft": 0.3048
    }

    m1 = arr_val[0] * mass_units[arr_unit[0]]
    m2 = arr_val[1] * mass_units[arr_unit[1]]
    r  = arr_val[2] * distance_units[arr_unit[2]]

    return G * m1 * m2 / (r ** 2)