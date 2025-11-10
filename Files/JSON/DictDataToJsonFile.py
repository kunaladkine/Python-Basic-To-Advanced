import json
dobj={'SNO':'100','NAME':'TRAVIS','MARKS':'55.55'}
print("Content of dict obj={} and Type={}".format(dobj,type(dobj)))
print("_"*50)
with open("student.json","w")as fp:
    json.dump(dobj,fp)
    print("Dict Saved in Json File ---verify")