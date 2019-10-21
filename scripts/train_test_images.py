#Set-up
from pathlib import Path
import shutil
import pandas as pd
import os
import re
import random

# Patients and CDT_images directories.
dir_excel=Path('/home/abraham/Escritorio/PAE2/PAE/pae2019/CLOCK')
dir_CDT=Path('/home/abraham/Escritorio/PAE2/PAE/pae2019/CLOCK/CDT_images')

#Test and train directories

train_directory=dir_CDT / "train"
train_health_directory=train_directory / "health"
train_dementia_directory=train_directory /"dementia"

test_directory=dir_CDT / "test"
test_health_directory=test_directory / "health"
test_dementia_directory=test_directory /"dementia"

#Remove existent directories
shutil.rmtree(train_directory,ignore_errors=True)
shutil.rmtree(test_directory,ignore_errors=True)

#List with image names
os.chdir(dir_CDT)
images=os.listdir()

#Generate directories with each classes:
os.mkdir(train_directory)
os.mkdir(train_health_directory)
os.mkdir(train_dementia_directory)
os.mkdir(test_directory)
os.mkdir(test_health_directory)
os.mkdir(test_dementia_directory)

#Directory that contains the patients information

os.chdir(dir_excel)

#Read data
patientsdata=pd.read_excel('Resumen_Datos_UPC.xls')
patientsdata.head()

#Join each patient with their class
IDIPAD=list(patientsdata['IDIPAD'])
NUM_SALUD=list(patientsdata['NUM_SALUD'])
class_patients= dict(zip(IDIPAD,NUM_SALUD))



# Shuffle the images and choose the percentatge of train and test data.
random.shuffle(images)
length=len(images)
percentage_train=0.7
train_number=int(length*percentage_train)
test_number=length-train_number
train_images=images[0:train_number]
test_images=images[train_number:train_number+test_number]

#Copy each image in its matching directory
for image in train_images:
    pattern="(.*?).png"
    if re.findall(pattern,image):
        b=int(re.findall(pattern,image)[0])
        c=class_patients.get(b)
    if c!=None:
        if c==0:
            shutil.copyfile(dir_CDT / image,train_health_directory/image)
        elif c==1:
            shutil.copyfile(dir_CDT / image,train_dementia_directory/image)

for image in test_images:
    pattern="(.*?).png"
    if re.findall(pattern,image):
        b=int(re.findall(pattern,image)[0])
        c=class_patients.get(b)
    if c!=None:
        if c==0:
            shutil.copyfile(dir_CDT / image,test_health_directory/image)
        elif c==1:
            shutil.copyfile(dir_CDT / image,test_dementia_directory/image)




