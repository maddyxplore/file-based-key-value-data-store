import json
import os

data = [{"name":"madhan","age":20,"email":"madhansubramani20022000@gmail.com","friend":"pradeep"}]
# NF - Non-Functional
# F - functional 

with open("data_file.json", "w") as write_file: # F.1 w-mode will open the file if exists or create the file if doesn't exist

    def check_size(): # to check the size NF1
        if os.path.getsize("data_file.json")<(1024*1024*1024):
            return True
        else:
            raise Exception("Error!! File size limit Exceeded...")
    
    temp = json.dumps(data,indent=4)
    write_file.write(temp)

def create():
    try:
        check_size()
        print("created")

    except Exception as e:
        print(e)

print(os.path.getsize("data_file.json")) # to check the size of the JSON file
create()
