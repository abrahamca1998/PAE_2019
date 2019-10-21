import os
import numpy as np
import json
import matplotlib.pyplot as plt
import re
from PIL import Image

def read_json(file):
    
    ## Read the json file
    #Inputs=name of json file(all path)
    
    with open(file, 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    filejson=str(obj.get('lines'))
    
    #Establish patterns in order to obtain the features of each 
    
    x_pattern="'x': (.*?),"
    y_pattern="'y': (.*?)}"
    force_pattern="'force': (.*?),"
    altitude_angle_pattern="'altitude_angle': (.*?),"
    azimuth_angle_pattern="'azimuth_angle': (.*?),"
    timestamp_pattern="'timestamp': (.*?),"
    
    # Find the features
    
    x=re.findall(x_pattern,filejson)
    y=re.findall(y_pattern,filejson)
    force=re.findall(force_pattern,filejson)
    altitude_angle=re.findall(altitude_angle_pattern,filejson)
    azimuth_angle=re.findall(azimuth_angle_pattern,filejson)
    timestamp=re.findall(timestamp_pattern,filejson)
    
    # Convert the features in numpy array to ease to facilitate the task of the predictive model
    x=np.array([float(i) for i in x])
    y=np.array([float(i) for i in y])
    force=np.array([float(i) for i in force])
    altitude_angle=np.array([float(i) for i in altitude_angle])
    azimuth_angle=np.array([float(i) for i in azimuth_angle])
    timestamp=np.array([float(i) for i in timestamp])
    
    return x,y,force,altitude_angle,azimuth_angle,timestamp
    
def search_json_files_Clock_Test(currentpath):
    ##This function returns all of the json files related to the clock drawing test.
    
    ##Change the current path to your path
    
    os.chdir(currentpath)
    
    #Search and save all paths of the files.
    
    paths=[]
    for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                paths.append(os.path.join(root, name))
            for name in dirs:
                paths.append(os.path.join(root, name))
   
    ## Patterns to search only the paths of the CDT files.
    pattern1="(/mad pencil y trazo/patientID_.*?/testID_.*?/.*?-CD-.*?-.*?-[0-9].json)"
    pattern2=".(/mad pencil y trazo/patientID_.*?/testID_.*?/.*?-CD-.*?-.*?-migrated.json)"
    pattern3="[^o](/patientID_.*?/testID_.*?/.*?-CD-.*?-.*?-[0-9].json)"
    patterns=[pattern1,pattern2,pattern3]
    
    ##Save the name of json files that complish the pattern
    
    json_files=[]
    for path in paths:
        for pattern in patterns:
            b=re.findall(pattern,path)
            if b:
                json_files.append(b)
                
   
    ##Clean the paths.
    
    path=currentpath+"{}"
    json_files=[str(i) for i in json_files]
    json_files=[i.replace(']','') for i in json_files]
    json_files=[i.replace('[','') for i in json_files]
    json_files=[i.replace("'","") for i in json_files]
    json_files=[path.format(i) for i in json_files]
    #for json_file in json_files:
    #   shutil.copy(json_file,'/home/abraham/Escritorio/PAE/numberdetection/PENCIL TRAZO Y RELOJ/samples')
        
    
    return json_files
def clean_empties_json(json_files):
    for json_file in json_files:
        x,_,_,_,_,_=read_json(json_file)
        if x.size==0:
            json_files.remove(json_file)    


def CDT_to_image(json_file,pattern,image_format):
    name="{}{}"
    x,y,_,_,_,_=read_json(json_file)
    fig=plt.gcf()
    plt.plot(x,y,'ro')
    patient=re.findall(pattern,json_file)[0]
    name=name.format(patient,image_format)
    plt.axis('off')
    plt.savefig(name)
    plt.close(fig)

def image_generator(image_path,json_files,pattern,format_image):
    os.chdir(image_path)
    for i in range(len(json_files)):
        CDT_to_image(json_files[i],pattern,format_image)
def rotate_images(image_path):
    os.chdir(image_path)
    images=os.listdir()
    for image in images:
        image_obj = Image.open(image)
        final_image = image_obj.rotate(180)
        final_image = final_image.transpose(Image.FLIP_LEFT_RIGHT)
        final_image.save(image)


