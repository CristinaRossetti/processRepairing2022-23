import os
import xml.etree.ElementTree as ET
import csv

# Percorso della cartella che contiene i file .pnml
path = 'C:/Users/crist/Desktop/FileBDA/risultati_evaluation/nuovi/fineExpNew/fineExp/'
alg = ['knapsack','goldratt_singleton','greedy_singleton']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
sub = ['7','14','19','24','28','30','33','50','56','58'] 

# Apre il file csv in modalità di scrittura
with open(path + 'new_count_singleton.csv', 'w', newline="") as f:
    # Crea un oggetto writer
    writer = csv.writer(f)

    # Scrive l'intestazione delle colonne
    writer.writerow(["algoritmo","sub","risorse","archi", "transition", "places","diff_archi","diff_transition","diff_places"])
    rete_originale = 'C:/Users/crist/OneDrive - Università Politecnica delle Marche/Desktop/Magistrale INF/Primo anno/Big Data Analytics e Machine Learning/Progetto_ BDA/ProcessRepairing/patterns_file_fineExp/fineExp_petriNet.pnml'

    tree = ET.parse(rete_originale)
    root = tree.getroot()
    arc_count_originale = 0
    trans_count_originale = 0
    place_count_originale = 0
    # Incrementa il contatore per gli archi, i nodi, le transizioni e i posti
    arc_count_originale += len(root.findall(".//arc"))
    trans_count_originale += len(root.findall(".//transition"))
    place_count_originale += len(root.findall(".//place"))
    # Per ogni file .pnml nella cartella specificata
    for a in alg:
        for s in sub:
            for r in rr:
                path = 'C:/Users/crist/Desktop/FileBDA/risultati_evaluation/nuovi/fineExpNew/fineExp/' + str(a) +'/' + 'testlog_' + str(s) +'/'
                arc_count = 0
                trans_count = 0
                place_count = 0
                
                
                os.chdir(path)
            
                        
                tree = ET.parse(path + 'new_repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) +'.pnml')
                        
                    #  Carica il file .pnml
                        #tree = ET.parse(os.path.join(path, filename))
                root = tree.getroot()

                        # Incrementa il contatore per gli archi, i nodi, le transizioni e i posti
                arc_count += len(root.findall(".//arc"))
                trans_count += len(root.findall(".//transition"))
                place_count += len(root.findall(".//place"))

                        # Scrive il risultato nel file csv
                writer.writerow([str(a),str(s),str(r), arc_count, trans_count, place_count, arc_count-arc_count_originale,trans_count-trans_count_originale,place_count-place_count_originale])

                        # Stampa il risultato su terminale
                print("File: "+ 'new_repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) +'.pnml')
                print("Numero di archi:", arc_count)
                print("Numero di transition:", trans_count)    
                print("Numero di place:", place_count)
                print("Differenza archi:",arc_count_originale-arc_count)
                print("Differenza transition:",trans_count_originale-trans_count)
                print("Differenza places",place_count_originale-place_count)
                        
f.close()
