"""
JSON to CSV converter

For broadn

AUTHOR: Madeline Porcaro

"""
import os
import sys
import json
import csv

def read_json(filename: str):

    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file and encountered an error.")
    return data

def clean_json(data):

    clean_data = dict()
    # print(f'data: {type(data)}')
    print("Made it to clean_data()")
        
       
def main(argv):

    try:
        argv[1].endswith('.json')
        print("Success! It's a JSON file!")
        data = read_json(sys.argv[1])
        clean = clean_json(data)

    except:
        Exception('File does not end with .json')

if __name__ == '__main__':
    print("Begin conversion")
    main(sys.argv)
    print("End conversion")
