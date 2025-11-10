import json
jsonstrfmt='{"SNO":"100","NAME":"TRAVIS","MARKS":"44,55"}'
print("Content of jsonstrformat={} and Type={}".format(jsonstrfmt,type(jsonstrfmt)))
print("_"*50)
dojb=json.loads(jsonstrfmt)
print("Content of dict obj={} and Type={}".format(dojb,type(dojb)))
for k,v in dojb.items():
    print("\t{}---->{}".format(k,v))
print("_"*50)