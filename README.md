## ***How to use***

`fetchaf uniprotID`

<br/>

<br/>

### **1. Script modification**

`line 9` : Enter the path of save directory of this python script (fetch_af.py)

    py_direc = '/opt/plugins/'

for windows ...

    py_direc = 'C:\\Users\\Username'

<br/>

### **2. Set the pymolrc**

1) Open PyMOL

2) File >> Edit pymolrc

3) Enter this command

    run /path/to/script

eg. 

    run /opt/plugins/fetch_af.py

for windows ...

    run C:\\Users\\Username\\fetch_af.py

3) Restart PyMOL

<br/>

### **3. Fetch**

Check the uniprot ID you want, and enter the command in PyMOL as follows.

    fetchaf Q5VSL9


You can enter the uniprot ID in lowercase letters.

    fetchaf q5vsl9
