def calc(list, spaces, stars, i, p=1):
        if (i % 2) != 0: 
            for j in range(stars):
                x = (spaces*0.5+j)*5
                y = (5.775*(radius-i)+ 5.775)*p
                list.append((x,y))

        else: 
            for j in range(stars):
                x = (spaces*0.5+j)*5
                y = (5.775*(radius-i)+2.8875)*p
                list.append((x,y))
        return list


def print_pattern(radius):
    coords = []
    # Upper part of the pattern (including the middle row)
    for i in range(1, radius+1):
        spaces = radius - i  # Calculate spaces before the stars
        stars = i + radius - 1 # Number of stars in each row
        if i == radius + 1: p = 0
        else: p = 1
        coords = (calc(coords, spaces, stars, i, p))

    # Lower part of the pattern (after the middle row)
    for i in range(radius - 1, 0, -1):
        spaces = radius - i
        stars = i + radius - 1
        coords = (calc(coords, spaces, stars, i, -1))
    
    return coords

# Example usage:
radius = 3  # Can be any number
print(print_pattern(radius))

