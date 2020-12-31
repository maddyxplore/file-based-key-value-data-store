import threading
import time
import json
import os

data = {} # dictionary acts as a JSON in python
lock = threading.Lock() # used to lock the data_file to prevent incorrect data accessing (Thread Safe)

def check_file(): # to check json file is present or not , if not create a new one with initial data
    global data
    try:
        if os.path.exists("data_file.json"):
            temp = open("data_file.json")
            data = json.loads(temp.read())
            temp.close()
        else:
            with open("data_file.json","w") as data_file:
                data = {}
                data1 = json.dumps(data,indent=2)
                data_file.write(data1)
                data_file.close()
            data = json.loads(open("data_file.json").read())
        return True
    except Exception:
        return("File is Empty")

def check_size(key,value): # to check the size of the file and check the value size
    value = len(str(value))
    if os.path.getsize("data_file.json") < (1024*1024*1024):
        if value < (16*1024*1024):
            if len(key) <= 32:
                return True
            else:
                raise Exception("Error || length of key must be capped with 32 chars")
        else:
            raise Exception("Error!! value size limit Exceeded...")
    else:
        raise Exception("Error!! file limit Exceeded...")

def update():
    with open("data_file.json","w") as data_file:
        lock.acquire() # to use the data file for single thread at a time
        # data will set as lock for updating it
        temp_data = json.dumps(data,indent=2)
        data_file.write(temp_data)
        data_file.close()
        # data will release after updating
        lock.release()

def create(key,value,time_to_live=0):
    try:
        if check_size(key,value) and key.isalpha(): # constraints to check the size and key whether it is a alphabet or not
            if key not in data: # check whether key is present in data or not
                ex_time = time.time() + time_to_live if time_to_live != 0 else 0
                data[key] = [value,ex_time]
                update()
                return("data created")
            else:
                return("Error || key is already present in data_store")
        else:
            return("Error || Key must Contains only alphabet characters")
    except Exception as e:
        return(e)

def read(key):
    if check_file():
        if key in data:
            if data[key][1] ==0: # constraints to check the time_to_live for read
                return({key:data[key][0]})
            else:
                if data[key][1] >= time.time():
                    return({key:data[key][0]})
                else:
                    return("Error || key has been expired")
        else:
            return("Error || Key is not present in data")

def delete(key):
    if check_file():
        if key in data:
            if data[key][1] ==0: # constraints to check the time_to_live for read
                del (data[key])
                update() # to update the data
                return("Value Deleted")
            else:
                if data[key][1] >= time.time():
                    del (data[key])
                    update()
                    return("Value Deleted")
                else:
                    return("Error || key has been expired")
        else:
            return("Error || Key is not present in data")

check_file()
