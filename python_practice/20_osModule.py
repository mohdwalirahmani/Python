import os

# print(os.listdir())

'''
print("Current directory:", os.getcwd())

print("Files:", os.listdir())

os.mkdir("test_folder")
print("Folder created.")

os.rename("test_folder", "renamed_folder")
print("Folder renamed.")

print("Exists?", os.path.exists("renamed_folder"))

we can do a lots of shit using this, for which we have to check on gfg or chatgpt

'''
if (not os.path.exists("Data")):
    os.mkdir("Data")

for i in range (1,11):
    os.mkdir(f"Data/Date{i}")

# this will create a folder with 10 sub folders date wise