import setup
currentpath='/home/abraham/Escritorio/PAE/pae2019/DATABASE/PENCIL TRAZO Y RELOJ'
json_files=setup.search_json_files_Clock_Test(currentpath)
setup.clean_empties_json(json_files)
pattern="patientID_(.*?)/"
format_image=".png"
image_path='/home/abraham/Escritorio/PAE/pae2019/CLOCK/CDT_images'
setup.image_generator(image_path,json_files,pattern,format_image)
setup.rotate_images('/home/abraham/Escritorio/PAE/pae2019/CLOCK/CDT_images')