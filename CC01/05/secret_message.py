import os

def rename_files() :
    # (1) get file names from a folder
    file_list = os.listdir("/Users/anujaverma/Desktop/NanoDegree/CC01/05/prank")
    print (file_list)

    # (2) for each file, rename filename
    saved_path= os.getcwd() #get current working directory
    os.chdir("/Users/anujaverma/Desktop/NanoDegree/CC01/05/prank")
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("new Name - "+file_name.translate(str.maketrans('', '', '0123456789')))
        os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))

rename_files()