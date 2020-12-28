import json
import os


data = [{"name":"madhan","age":20,"email":"madhansubramani20022000@gmail.com","friend":"pradeep"}]


with open("data_file.json", "w") as write_file: # w-mode will open the file if exists or create the file if doesn't exist
    temp = json.dumps(data,indent=4)
    write_file.write(temp)

print(os.path.getsize("data_file.json")) # to check the size of the JSON file
