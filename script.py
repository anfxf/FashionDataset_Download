import pandas as pd
import wget

print("")
print("use ")
gender = input("Use '0' For Men, '1' For Women : ")
howMuch = int(input("How Many Images To Download: "))

image_file = pd.read_csv("images.csv", on_bad_lines='skip')
style_file = pd.read_csv("styles.csv", on_bad_lines="skip")

def Download():
    if(gender == "0"):
        filter_gender = style_file[['id','gender']][style_file['gender'] == "Men"]
    elif gender == "1":
        filter_gender = style_file[['id','gender']][style_file['gender'] == "Women"]
    else:
        print("ERROR")

    for id in filter_gender['id'][:howMuch]:
        file = f"{id}.jpg"
        file_id = image_file['filename']
        for x in file_id:
            if(file == x):
                src = image_file[image_file['filename'] == file]
                for s in src['link']:            
                    wget.download(s, f"./Downloads/{file}")

Download()
