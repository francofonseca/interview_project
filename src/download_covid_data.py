from requests import get, exceptions
from json import dump, load
from os import path

# Tuple with all valid countries
# Note: this can be extended to a more proper csv or local file that has all ISO country codes
# We can even download all data on the fly using the API and filter it but this will cause more time delay
# For purposes of interview I decided to mantain a simple tuple to handle my countries
tuple_iso_countries = ('MX')

# Simple function to build the json file with the data
# This file doesn't have a timestamp or something that differentiates one from another so once is created it never calls API again
# This can be simply removed adding a timestamp and after certain time we can download again a new file with the most recent info
def store_api_call(request, country):
    file_name='{}{}{}{}'.format('../local_cache/','data_', country, '.json')
    with open(file_name, 'w') as json_ref:
        dump(request.json(), json_ref)
    return file_name


def call_to_api(country):
    # I build the URL on the fly but is still attached to use only cases and AB ISO name
    # This can refactored in a generic way to call it
    api_url = 'https://covid-api.mmediagroup.fr/v1/'
    # TODO Add options and types of calls
    option = 'cases'
    type_of_call = 'ab='
    URL = '{}{}{}{}{}'.format(api_url, option, '?', type_of_call, country)
    # Simple rest call with simple handling nothing fancy on it
    try:
        output = get(URL)
    except exceptions.RequestException as e:
        return '{}{}'.format('Bad REST call return code: ', e.errno)
    #Store output on a file
    file_name = store_api_call(output, country)
    return file_name

# I decided to use local storage in order to be have a more simple solution
def check_cache_call(country):
    path_to_cache = '../local_cache/'
    file_name = '{}{}{}'.format('data_', country, '.json')
    total_file_name = '{}{}'.format(path_to_cache, file_name)
    if path.exists(total_file_name):
        return total_file_name
    else:
        return ''
    
# Quick validation of country on the tuple
def validate_argument(argument):
    if argument in tuple_iso_countries:
        return argument
    else:
        return 'Not valid country'

# Check if there is a file with info in case of true there is no need to call the API
# With this base we can play a little bit more with adding timestamps to refresh files or more options to the behaviour of the calls
def retrieve_country_info(argument):
    country = validate_argument(argument)
    country_file = check_cache_call(country)
    if not country_file:
        country_file = call_to_api(country)
    with open(country_file, 'r') as country_file_ref:
            json_ref = load(country_file_ref)
    return json_ref