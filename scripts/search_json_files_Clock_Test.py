def search_json_files_Clock_Test(currentpath):
    os.chdir(currentpath)
    paths=[]
    for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                paths.append(os.path.join(root, name))
            for name in dirs:
                paths.append(os.path.join(root, name))
    pattern1=".(/patientID_.*?/testID_.*?/.*?-CD-.*?-.*?-[0-9].json)"
    pattern2=".(/mad pencil y trazo/patientID_.*?/testID_.*?/.*?-CD-.*?-.*?-migrated.json)"
    patterns=[pattern1,pattern2]
    json_files=[]
    for path in paths:
        for pattern in patterns:
            b=re.findall(pattern,path)
            if b:
                json_files.append(b)
    return json_files