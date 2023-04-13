def rgb(r, g, b):

    def to_normal(num):
        if num <= 0 or isinstance(num, str):
            return '00'
        if num < 16:
            return '0'+hex(num)[2:].upper()
        elif num >= 255:
            return 'FF'
        else:
            return hex(num)[2:].upper()

    output = to_normal(r) + to_normal(g) + to_normal(b)
    return output


print(rgb(1, 2, 3))

