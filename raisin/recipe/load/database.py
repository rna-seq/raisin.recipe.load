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

    headers = ["project_id",
               "accession_id",
               "species",
               "cell",
               "readType",
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
    output_file = open("database.csv", "w")
    output_file.write('\t'.join(headers) + '\n')

    accession_id_for_file = {}
    for accession in accessions:
        accession_id_for_file[accession['file_location']] = accession['accession_id']

    for file in files:
        output_file.write(template % (file['project_id'],
                                      accession_id_for_file[file['file_location']],
                                      file['species'], 
                                      file['cell'], 
                                      file['readType'],
                                      file['qualities'],
                                      file['file_location'],
                                      file['dataType'],
                                      file['rnaExtract'],
                                      file['localization'],
                                      '1',
                                      file['lab'],
                                      file['view'],
                                      file['type']
                                      ))

if __name__ == '__main__':
    main()
