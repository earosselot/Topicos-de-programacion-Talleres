divisor = 100000


def fix(value):
    return value * divisor


def unfix(value):
    return float(value) / divisor


print((fix(10.05) - fix(15.75)) // fix(3.1415))

print(unfix(fix(fix(10.05)-fix(15.75))//fix(3.1415)))
print((10.05 - 15.75) // 3.1415)
print(fix(10.05))
print(fix(15.75))
print('-----------------------')

print(fix(0.00000456))
print(fix(9223372036854775807))
print(fix(43.001 * 0.00751))
print(fix(0.00000001 * 1.4142135623730951))
print(fix(0.1+0.1+0.1-0.3))
print('-----------------------')

print(float(0.00000456))
print(float(9223372036854775807))
print(float(43.001 * 0.00751))
print(float(0.00000001 * 1.4142135623730951))
print(float(0.1+0.1+0.1-0.3))


