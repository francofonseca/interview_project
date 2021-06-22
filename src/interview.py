#!/bin/python
import sys

import download_covid_data
import file_converter
import plot_map

def main(argv):
    # TODO Use argparse to add the next arguments
    #print('usage: interview.py [options] country')
    #print('  options: ')
    #print('    -h Help              Prints usage')
    #print('    -v Verbose           Useful for debug')
    #print('    -n Country Name      i.e. Mexico')
    #print('    -i Country Alpha2    i.e. MX')
    #print('    -c Country Code      i.e. 484')
    
    # Because of time we used only one case to work
    dummy_argument='MX'
    
    # Retrieve data
    json_info = download_covid_data.retrieve_country_info(dummy_argument)
    
    # Convert it to a csv file to a more easy handle
    if json_info:
        path_to_csv = file_converter.json_2_csv(json_info)

    # Plot it!
    if path_to_csv:
        plot_map.plotly_map_csv(path_to_csv)     


if __name__ == "__main__":
    main(sys.argv[1:])
