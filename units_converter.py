def units_converter(val, unit):
    un_dict = {
        'j': (4.359 * 10 ** (-18), 'Ha'),
        'mj': (4.359 * 10 ** (-15), 'Ha'),
        'uj': (4.359 * 10 ** (-12), 'Ha'),
        'nj': (4.359 * 10 ** (-9), 'Ha'),
        'kj': (4.359 * 10 ** (-21), 'Ha'),
        'm': (45.291 * 10 ** (-11), 'a_0'),
        'mm': (45.291 * 10 ** (-8), 'a_0'),
        'um': (45.291 * 10 ** (-5), 'a_0'),
        'nm': (45.291 * 10 ** (-2), 'a_0'),
        'km': (45.291 * 10 ** (-14), 'a_0'),
        'kg': (9.109 * 10 ** (-31), 'm_e'),
        'g': (9.109 * 10 ** (-28), 'm_e'),
        'mg': (9.109 * 10 ** (-25), 'm_e'),
        'ug': (9.109 * 10 ** (-22), 'm_e'),
        'ng': (9.109 * 10 ** (-19), 'm_e'),
        'c': (1.602 * 10 ** (-19), "e"),
        'mc': (1.602 * 10 ** (-16), 'e'),
        'uc': (1.602 * 10 ** (-13), 'e'),
        'nc': (1.602 * 10 ** (-10), 'e'),
        'kc': (1.602 * 10 ** (-22), 'e'),
        'j*s': (1.054 * 10 ** (-34), '\u0127'),
        'mj*s': (1.054 * 10 ** (-31), '\u0127'),
        'uj*s': (1.054 * 10 ** (-28), '\u0127'),
        'nj*s': (1.054 * 10 ** (-25), '\u0127'),
        'kj*s': (1.054 * 10 ** (-37), '\u0127'),
        's': (2.419 * 10 ** (-17), '\u0127/Ha'),
        'ms': (2.419 * 10 ** (-14), '\u0127/Ha'),
        'us': (2.419 * 10 ** (-11), '\u0127/Ha'),
        'ns': (2.419 * 10 ** (-8), '\u0127/Ha'),
    }
    x = un_dict[unit.lower()][0] * val
    return float('{:.3e}'.format(x)), un_dict[unit.lower()][1]


print("This script converts SI base units to Hartree atomic units.")
print("Enter the value in the SI system that you want to convert, e.g. 400 uJ or 15 nJ*s. If you want to learn more "
      "about this units and why is this converter needed, print 'help', for exit print 'exit'")
text = input().split()
while text[0] != 'exit':
    if text[0] == 'help':
        print("The Hartree atomic units are a system of natural units of measurement which is especially convenient for "
              "atomic physics and computational chemistry calculations. They are named after the physicist Douglas "
              "Hartree. In this system the numerical values of the following four fundamental physical constants are "
              "all unity by definition:")
        print("Reduced Planck constant: \u0127 = 1, also known as the atomic unit of action")
        print("Elementary charge: e = 1, also known as the atomic unit of charge")
        print("Bohr radius: a_0 = 1, also known as the atomic unit of length")
        print("Electron mass: m_e = 1 , also known as the atomic unit of mass")
        print("Source: https://en.wikipedia.org/wiki/Hartree_atomic_units")
        print("You can convert  Energy (J), Mass (kg), Action (J*s), Length (m), Electric charge (C)")
        text = input().split()
    elif type(text[0]) == str:
        break
    else:
        a = int(text[0])
        b = str(text[1])
        c = units_converter(a, b)
        print(text[0], text[1], 'is', c[0], c[1])
        text = input().split()
