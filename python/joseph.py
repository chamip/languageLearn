def josephLoop():
    persons = [True] * 30
    count, index, number = 0, 0, 0
    while count < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                count += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    josephLoop()
