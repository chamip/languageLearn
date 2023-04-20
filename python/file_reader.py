with open('pi.digits.txt') as file_obj:
    contents = file_obj.read()
print(contents.strip())

filename = 'pi.digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
