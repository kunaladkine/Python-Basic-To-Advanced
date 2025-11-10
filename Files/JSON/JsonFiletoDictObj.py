import json
#choose the json file and open in read mode
with open("student.json","r")as fp:
    dobj=json.load(fp)
    print("Content of Dict obj={} and Type={}".format(dobj,type(dobj)))
    for k,v in dobj.items():
        print("\t{}---->{}".format(k,v))