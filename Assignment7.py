# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file and try/catch blocks
# ChangeLog: Jeremy Warren,05/30/2022,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "ab")
    pickle.dump(list_of_data, file)
    file.close()


def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data


# Presentation ------------------------------------ #
try:
    id = int(input("Enter the ID: "))
    if type(id) == str:
        raise Exception

    str_name = (input('Enter Name: '))
    if str_name.isnumeric():
        raise Exception('Do not use numbers for Name')

    lstCustomer = [id, str_name]
    save_data_to_file(strFileName, lstCustomer)

except Exception as e:
    print("Do not sse letters for numbers")
    print("Do not use numbers for name")

input('Press enter to finish')



#
#https://www.youtube.com/watch?v=Pl4Hp8qwwes
#https://www.youtube.com/watch?v=NIWwJbo-9_8