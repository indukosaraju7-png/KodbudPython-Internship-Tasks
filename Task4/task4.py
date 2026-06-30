import os
folder_path = input("Enter the folder path: ")
files=os.listdir(folder_path)
count=1
for file_name in files:
    old_path=os.path.join(folder_path,file_name)
    if os.path.isfile(old_path):
        file_extension=os.path.splitext(file_name)[1]
        new_name=f"file{count}{file_extension}"
        new_path=os.path.join(folder_path,new_name)
        os.rename(old_path,new_path)
        print(f"Renamed '{file_name}' to '{new_name}'")
        count+=1
print("File renaming completed.")