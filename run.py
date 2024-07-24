import glob
import json
import os
import shutil

# Change this to your namespace
namespace = 'bloon_bloom'

if not os.path.exists("input"):
    os.mkdir("input")
    exit()

if os.path.exists("output"):
    shutil.rmtree("output")
if not os.path.exists("output"):
    os.mkdir("output")

else:
    shutil.rmtree("output")
    os.mkdir("output")
os.chdir("input")
for file_name in glob.glob("*.bbmodel"):
    with open(file_name, 'r',encoding='utf-8') as file:
        filedata = file.read()
    json_object = json.loads(filedata)

    for x in range(0,len(json_object['textures'])):
        json_object['textures'][x]['namespace'] = namespace
        json_object['textures'][x]['folder'] = 'entity'
    
    with open('../output/'+file_name, 'w') as file2:
        file2.write(json.dumps(json_object))
print("Done!")