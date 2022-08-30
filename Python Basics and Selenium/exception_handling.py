# Raise exception if items in cart is not equal to 2

items = int(input('Enter the items'))
if items<2:
    raise Exception("Items should be 2 or more")
else:
    print("All good!")

assert(items == 2)

# try block - risky code- try to execute else raise exception

# text.txt does not exist so it will raise exception and terminate the program, hence we need try excep block
# Exception - FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'

# using try-except block, if error is raised it will transfer the control to except block without terminating the code
try:
    with open("read.txt", "r") as reader:
        print(reader.read())
except :
    print('Failure in try block') # USed to handle the popup-handling

    # when to use finally - You created some records and after your work you want to delete records
    # so finally you will delete the records, so that is inside finally  block - Delete Cookies
finally:
    print('I am Finally block who will always run')


# How to know what Python had the error lets see the code
try:
    with open("text.txt", "r") as reader:
        print(reader.read())
except Exception as e:
    print(e) # Print the exception

# Program does not terinates if there is error
print('END')