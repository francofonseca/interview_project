from csv import writer

# Convert json file to csv 
# This functions works assuming the usage of the COVID API
# Even if is not totally generic for every json 
# It converts every country to a easy way to handle the data on any geographic plotter

# Final columns of the CSV are 
# state,lat,long,confirmed,recovered,deaths,updated

def json_2_csv(json_ref):
    #Retrieve states of the republic and the headers based on the first state
    states=list(json_ref.keys())
    headers=list(json_ref[states[1]].keys())
    #Insert state name on the list of headers
    headers.insert(0,'state')

    #Create the csv file
    try:
        data_ref = open('../local_cache/json_2_csv.csv','w')
    except OSError:
        print('Error creating/opening the file')
        return ''
    
    csv_writer = writer(data_ref)
    #Insert headers
    csv_writer.writerow(headers)
    
    #Insert rows of data ordered
    for index in range(1,len(states)):
        tmp_row=list(json_ref[states[index]].values())
        tmp_row.insert(0,states[index])
        csv_writer.writerow(tmp_row)
    
    #Close csv
    data_ref.close()
    return '../local_cache/json_2_csv.csv'