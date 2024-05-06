def draw_xyz(N):
    pattern = ""
    for i in range(N):
        row = ""
        for j in range(N):
            if (i + j) % 3 == 0:
                row += "Y "
            elif (i + j) % 3 == 1:
                row += "Z "
            else:
                row += "X "
        pattern += row.strip() + "\n"
    return pattern.strip()

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """

    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """
