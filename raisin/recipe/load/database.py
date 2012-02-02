import csv

PATH = "../extract/workspace/%s"

def read_csv(file_name):
    return csv.DictReader(open(PATH % file_name, 'r'), 
                               delimiter='\t', 
                               skipinitialspace=True)

def main(options, buildout):
    accessions = read_csv("accessions.csv")
    profiles = read_csv("profiles.csv")
    annotations = read_csv("annotations.csv")
    files = read_csv("files.csv")
