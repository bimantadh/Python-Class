from student import StudentDetail

#Reading from a file
with open("ello.txt", "r") as file_object:
    file_contents = file_object.read()
    print(file_contents)

with open("ello.txt", "w") as file_object:
    file_object.write("update that file")
    
with open("ello.txt", "a") as file_object:
    file_object.write("\nupdate that file")