import glob
import json
import os
import shutil

# Change this to your namespace
namespace = 'rabit_pet'

if not os.path.exists("input"):
    os.mkdir("input")
    exit()

if not os.path.exists("output"):
    os.mkdir("output")
else:
    shutil.rmtree("output")
    os.mkdir("output")
os.chdir("input")
for file_name in glob.glob("*.bbmodel"):
    with open(file_name, 'r') as file:
        filedata = file.read()
    json_object = json.loads(filedata)

    for x in range(0,len(json_object['textures'])):
        json_object['textures'][x]['namespace'] = namespace
        json_object['textures'][x]['folder'] = 'mobs'
    
    with open('../output/'+namespace+"_"+file_name, 'w') as file2:
        file2.write(json.dumps(json_object))
print("Done!")