import os


def write(data):
    while True:
        file_name = input("Enter file name: ")
        if file_name.strip() != "":
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            try:
                if not os.path.exists("Uploads/"):
                    os.makedirs("Uploads/")
                with open("Uploads/" + file_name, 'w') as f:
                    f.write(data)
                print("The art was uploaded successfully")
                break
            except IOError:
                raise IOError("The file could not be uploaded, please try again")
        else:
            print("Please enter a valid file name")