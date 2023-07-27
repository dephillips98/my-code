#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    ## first grab credentials
    nasacreds = returncreds()
    date = "start_date=2000-01-01&end_date=2023-07-26"
    neowrequest = requests.get(NEOURL + date + "&" + nasacreds)
    data = neowrequest.json() 
    size_num1 = 0
    near_num1 = 0
    near_num2 = 0
    size = data['near_earth_objects']['2023-07-27'][size_num1]['estimated_diameter']['miles']['estimated_diameter_max']
    near = data['near_earth_objects']['2023-07-27'][near_num1]['close_approach_data'][near_num2]['miss_distance']['miles']
    
    #for astroid in 

if __name__ == "__main__":
    main()
