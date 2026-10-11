# Type your code here.
input_file_name = input()


f = open(input_file_name)

for file_name in f:
    file_name = file_name.replace("photo.jpg", "info.txt")
    print(file_name, end="")


f.close()