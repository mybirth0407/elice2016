def main():
    r = input() # First line
    g = input() # Second line
    b = input() # Third line

    # change r, g, b into integer...

    print(rgb2hex(r, g, b))


def rgb2hex(r, g, b):
    hex_color = "#"
    hex_color += ("%02X" % int(r)) + ("%02X" % int(g)) + ("%02X" % int(b))
    return hex_color

if __name__ == "__main__":
    main()
