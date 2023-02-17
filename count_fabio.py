import os
import xml.etree.ElementTree as ET
import csv

#sub =  ['8','26','28','30','37','42','50','55','56','64']
#sub = ['7','14','19','24','28','30','33','50','56','58'] 
#sub = ['2','4','8','17','18','20','21','22','26','29','31','33','48','63','105']
sub = ['29','31','39','52','57','62','71','73','75','77'] 
path = 'C:/Users/crist/OneDrive - Università Politecnica delle Marche/Desktop/Magistrale INF/Primo anno/Big Data Analytics e Machine Learning/Progetto_ BDA/ProcessRepairing/patterns_file_testBankSCCUpdatedCopia/'

rete_originale = path +'testBank2000SCCUpdatedCopia_petriNet.pnml'
tree = ET.parse(rete_originale)
root = tree.getroot()
arc_count_originale = 0
trans_count_originale = 0
place_count_originale = 0
    # Incrementa il contatore per gli archi, i nodi, le transizioni e i posti
arc_count_originale += len(root.findall(".//arc"))
trans_count_originale += len(root.findall(".//transition"))
place_count_originale += len(root.findall(".//place"))
with open(path + 'count_Fabio.csv', 'w', newline="") as f:
    # Crea un oggetto writer
    writer = csv.writer(f)

    # Scrive l'intestazione delle colonne
    writer.writerow(["sub","diff_archi","diff_transition","diff_places"])
    for s in sub: #itera sul numero delle sub
        os.chdir(path)
        rete_Fabio = path + 'test_repairing/'+ 'Sub_' +str(s) + '/' + 'repaired_Sub' + str(s) + '_petriNet.pnml'
 
        tree = ET.parse(rete_Fabio)
        root = tree.getroot()
        arc_count_Fabio = 0
        trans_count_Fabio = 0
        place_count_Fabio = 0
    # Incrementa il contatore per gli archi, i nodi, le transizioni e i posti
        arc_count_Fabio += len(root.findall(".//arc"))
        trans_count_Fabio += len(root.findall(".//transition"))
        place_count_Fabio += len(root.findall(".//place"))
        writer.writerow([str(s), arc_count_Fabio - arc_count_originale,trans_count_Fabio - trans_count_originale,place_count_Fabio - place_count_originale])


print("Numero archi: ",arc_count_Fabio - arc_count_originale)
print("Numero transitios: ",trans_count_Fabio - trans_count_originale)
print("Numero di places: ",place_count_Fabio - place_count_originale)
f.close()