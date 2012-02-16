import os
import csv
import sqlite3

def read_csv(staging, file_name):
    path = os.path.join(staging, file_name)
    read = open(path, 'r')
    items = []
    for item in csv.DictReader(read, delimiter='\t', skipinitialspace=True):
        items.append(item)
    return items


def get_experiments(data):
    experiments = {}
    for experiment in data['experiments']:
        key = (experiment['project_id'], experiment['accession_id'])
        experiments[key] = experiment
    return experiments


def get_accessions(data):
    accessions = {}
    for accession in data['accessions']:
        key = (accession['project_id'], accession['accession_id'])
        accessions[key] = accession
    return accessions


def get_view(data):
    views = {}
    for view in data['view']:
        key = (view['project_id'],
               view['accession_id'],
               view['file_location']
              )
        views[key] = view
    return  views


def get_files(data):
    files = {}
    for afile in data['files']:
        key = (afile['project_id'],
               afile['accession_id'],
               afile['file_location'])
        files[key] = afile
    return files


def get_read_lengths(data):
    read_lengths = {}
    for read_length in data['read_length']:
        key = (read_length['project_id'], read_length['accession_id'])
        read_lengths[key] = read_length
    return read_lengths


def main(staging):
    data = {'accessions': read_csv(staging, "accessions.csv"),
            'profiles': read_csv(staging, "profiles.csv"),
            'annotations':  read_csv(staging, "annotations.csv"),
            'files': read_csv(staging, "files.csv"),
            'experiments': read_csv(staging, "experiments.csv"),
            'read_length': read_csv(staging, "read_length.csv"),
            'view': read_csv(staging, "view.csv"),
           }

    headers = ["project_id",
               "accession_id",
               "species",
               "cell",
               "readType",
               "read_length",
               "qualities",
               "file_location",
               "dataType",
               "rnaExtract",
               "localization",
               "replicate",
               "lab",
               "view",
               "type"
               ]

    template = '\t'.join(['%s'] * len(headers)) + '\n'
    path = os.path.join(staging, "database.csv")
    output_file = open(path, "w")
    output_file.write('\t'.join(headers) + '\n')

    experiments = get_experiments(data)
    accessions = get_accessions(data)
    views = get_view(data)
    files = get_files(data)
    read_lengths = get_read_lengths(data)

    path = os.path.join(staging, "database.db")
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('''create table files (%s)''' % ",".join(["%s text" % h for h in headers]))

    for key, afile in files.items():
        project_id, accession_id, file_location = key
        experiment = experiments[(project_id, accession_id)]
        accession = accessions[(project_id, accession_id)]
        view = views[key]
        read_length = read_lengths[(project_id, accession_id)]

        row = (afile['project_id'],
               afile['accession_id'],
               accession['species'],
               accession['cell'],
               accession['readType'],
               read_length['read_length'],
               accession['qualities'],
               file_location,
               accession['dataType'],
               accession['rnaExtract'],
               accession['localization'],
               experiment['replicate_id'],
               accession['lab'],
               view['view'],
               accession['type']
               )
        output_file.write(template % row)
        c.execute("""insert into files values %s""" % str(row))
    
    conn.commit()
    c.close()
     

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 