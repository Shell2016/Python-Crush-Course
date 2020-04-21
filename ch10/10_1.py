with open('ch10/learning_python.txt') as file_object:
    contents = file_object.readlines()
for line in contents:
    print(line.rstrip().replace('Python', 'C'))
