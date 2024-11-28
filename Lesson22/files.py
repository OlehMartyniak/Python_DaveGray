# read
# append
# write 
# create

# file = open("/Users/olegmartyniak/Desktop/Programming/Python/Python_DaveGray/Lesson22/names.txt", "r")

# можна прочитати весь файл
# print(file.read())

# можна прочитати лінію
# print(file.readline())

# можна вивести інформацію з допомогою циклу

# for line in file:
#    print(line)

# важливо одразу закривати файл
# file.close()

try:
    file = open("/Users/olegmartyniak/Desktop/Programming/Python/Python_DaveGray/Lesson22/names.txt", "r")
    print(file.read())
except:
    print("The file you want to read doesn't exist")
finally:
    file.close()



# Append - adds information into a file or creates one if it doesn't exist

file = open("/Users/olegmartyniak/Desktop/Programming/Python/Python_DaveGray/Lesson22/names.txt", "a")
file.write("\nBartolomey")
file.close()

file = open("/Users/olegmartyniak/Desktop/Programming/Python/Python_DaveGray/Lesson22/names.txt", "r")
print(file.read())
file.close()
