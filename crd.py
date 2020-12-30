import json
import os

def check_file(): # to check json file is present or not , if not create a new one with initial data
    if os.path.exists("data_file.json"):
        data = json.loads(open("data_file.json").read())
        print(data)
    else:
        with open("data_file.json","w") as data_file:
            d = {"name":"madhan","age":20}
            data = json.dumps(d,indent=4)
            data_file.write(data)


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

check_file()
