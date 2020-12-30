import time
import json
import os

data = {}

def check_file(): # to check json file is present or not , if not create a new one with initial data
    global data
    if os.path.exists("data_file.json"):
        data = json.loads(open("data_file.json").read())
        print(data)
    else:
        with open("data_file.json","w") as data_file:
            d = {"name":"madhan","age":20}
            data1 = json.dumps(d,indent=2)
            data_file.write(data1)
            data_file.close()
        data = json.loads(open("data_file.json").read())
        print(data)


def check_size(value): # to check the size of the file and check the value size
    value = len(value)
    if os.path.getsize("data_file.json")<(1024*1024*1024) and value<(16*1024*1024):
        return True
    elif os.path.getsize("data_file.json")>=(1024*1024*1024) and value<(16*1024*1024):
        raise Exception("Error!! File size limit Exceeded...")
    elif os.path.getsize("data_file.json")<(1024*1024*1024) and value>=(16*1024*1024):
        raise Exception("Error!! Value size limit Exceeded...")
    else:
        raise Exception("Error!! file and value limit Exceeded...")

def create(key,value,time_to_live=0):
    try:
        if check_size(value) and key.isalpha(): # constraints to check the size and key whether it is a alphabet or not
            if key not in data: # check whether key is present in data or not
                ex_time = time.time() + time_to_live
                data[key] = {value,ex_time}
                with open("data_file.json","w") as data_file:
                    temp_data = json.dumps(data,indent=2)
                    data_file.write(temp_data)
                    data_file.close()
            else:
                print("Error || key is already present in data_store")
        else:
            print("Error || Key must Contains only alphabet characters")
    except Exception as e:
        print(e)

check_file()
create("nametwo","madhan",0)
print(data)

