def read_json(file):
    with open(file, 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    filejson=str(obj.get('lines'))
    
    x_pattern="'x': (.*?),"
    y_pattern="'y': (.*?)}"
    force_pattern="'force': (.*?),"
    altitude_angle_pattern="'altitude_angle': (.*?),"
    azimuth_angle_pattern="'azimuth_angle': (.*?),"
    timestamp_pattern="'timestamp': (.*?),"
    
    
    
    x=re.findall(x_pattern,filejson)
    y=re.findall(y_pattern,filejson)
    force=re.findall(force_pattern,filejson)
    altitude_angle=re.findall(altitude_angle_pattern,filejson)
    azimuth_angle=re.findall(azimuth_angle_pattern,filejson)
    timestamp=re.findall(timestamp_pattern,filejson)
    
    x=np.array([float(i) for i in x])
    y=np.array([float(i) for i in y])
    force=np.array([float(i) for i in force])
    altitude_angle=np.array([float(i) for i in altitude_angle])
    azimuth_angle=np.array([float(i) for i in azimuth_angle])
    timestamp=np.array([float(i) for i in timestamp])
    
    return x,y,force,altitude_angle,azimuth_angle,timestamp