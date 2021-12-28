import os
import urllib.request

from pymol import cmd



dst = 'fetchaf_queries'
py_direc = '/path/to/python_script/'



def fetchaf (query, dst=dst):

    query = query.upper()

    pdb_file = f'AF-{query}-F1-model_v2.pdb'

    file_list = os.listdir(py_direc)
    pdb_list = [file for file in file_list if file.endswith('.pdb')]


    if dst in file_list:
        pass
        
    else:
        os.mkdir(f'{py_direc}/{dst}')



    if pdb_file in pdb_list:
        cmd.load(f'{py_direc}/{dst}/AF-{query}-F1-model_v2.pdb')

    else:
            
        try:
            url = f'https://alphafold.ebi.ac.uk/files/AF-{query}-F1-model_v2.pdb'
            urllib.request.urlretrieve(url, f'{py_direc}/{dst}/AF-{query}-F1-model_v2.pdb')
            cmd.load(f'{py_direc}/{dst}/AF-{query}-F1-model_v2.pdb')

        except urllib.request.HTTPError:
            print ('The query was not found in https://alphafold.ebi.ac.uk')



cmd.extend('fetchaf', fetchaf)

