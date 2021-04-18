color1 = input('Please input the first primary color to mix: ')
color2 = input('Please input the second primary color to mix: ')

if (color1 != 'red' and color1 != 'blue' and color1 != 'yellow') or (color2 != 'red' and color2 != 'blue' and color2 != 'yellow'):
    print('Input must be a primary color!')
else:
    if color1 == 'red':
        if color2 == 'red':
            print('The resulting color is red!')
        if color2 == 'blue':
            print('The resulting color is purple!')
        if color2 == 'yellow':
            print('The resulting color is orange!')
    if color1 == 'blue':
        if color2 == 'red':
            print('The resulting color is purple!')
        if color2 == 'blue':
            print('The resulting color is blue!')
        if color2 == 'yellow':
            print('The resulting color is green!')
    if color1 == 'yellow':
        if color2 == 'red':
            print('The resulting color is orange!')
        if color2 == 'blue':
            print('The resulting color is green!')
        if color2 == 'yellow':
            print('The resulting color is yellow!')
