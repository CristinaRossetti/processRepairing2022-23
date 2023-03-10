# Process Repairing

In questa repository sono presenti tutti gli script in Python utilizzati per ottenere l’evaluation corretta delle reti riparate con l’approccio di Polyvanyy.

Il file [ExtractSublog.py](http://ExtractSublog.py) ha l’obiettivo di estrarre i sottolog inerenti alle diverse sub per ogni rete, al fine di poter riparare i modelli in input con i vari sottolog, anziché che con l’intero event log.

---

I files riparati sono posizionati nelle directory secondo la seguente logica: la directory più esterna ha il nome della rete originaria, più internamente si hanno tante cartelle quante sono le sub per quella rete. All’interno di ciascuna cartella della sub, abbiamo due casi:
-per gli algoritmi singleton si hanno le 16 reti riparate
-per gli algoritmi multiple ci sono 16 cartelle, ognuna inerente ad una risorsa di riparazione e in ogni cartella ci sono le varie riparazioni multiple per quella risorsa. Ad esempio, per la risorsa di riparazione 0, la cartella ha nome "r_0".

---

Dopo aver ottenuto le riparazioni, sono stati innanzitutto rinominati i files. Le reti, dopo la riparazione, venivano salvate con un nome del tipo "REPAIRED.GREEDY.1.900.pnml", dove il primo numero indica la risorsa di riparazione e il secondo il costo totale di riparazione. Effettuare l'evaluation iterando su file con questa denominazione era complesso e poco intuitivo. 
Per risolvere questo problema, è stato realizzato uno script che eliminasse i costi dai nomi dei files, ottenendo ad es. "REPAIRED.GREEDY.1.pnml". Gli script che risolvono tale problema sono nameFiles.py e nameFiles_multiple.py. Dopodichè sono state rinominate le transazioni invisibili delle reti riparate. Per ogni rete ci sono due files, uno per gli algoritmi singleton e un altro per gli algoritmi multiple, poiché le reti riparate con le due tipologie di algoritmo vengono salvate con nomi differenti (nelle riparazioni multiple c’è anche l’indicazione del numero della riparazione per una certa risorsa). Infatti, all’interno dei files che rinominano le transizioni invisibili, c’è anche un’istruzione che memorizza le nuove reti processate con una denominazione più chiara e omogenea. In particolare, questi files sono: 
tauTransition.py (rete bpi2012 riparata con algoritmi singleton)
tauTransition_multiple.py (rete bpi2012 riparata con algoritmi multiple)
numTransition.py (rete testBank2000SCCUpdated e testBank2000NoRandomNoise con algoritmi singleton)
numTransition_multiple.py (rete testBank2000SCCUpdated  e testBank2000NoRandomNoise con algoritmi multiple)
fineExp_transition.py (rete FineExp riparata con algoritmi singleton)
fineExp_transition_multiple.py (rete fineExp riparata con algoritmi multiple)

---

Nei files repair_places.py e repair_places_multiple.py viene effettuata un’ulteriore fase di processing in cui si vanno a inserire i marking iniziali nelle reti riparate. Dopodiché, nello stesso file, si effettua l’evaluation. Con un costrutto try … except si cattura l’eccezione che si può verificare nel caso in cui la rete non sia sound, quindi questa non viene valutata. 
Sono stati divisi i files per gli algoritmi singleton e multiple, poiché questi ultimi generano più reti per ogni risorsa di riparazione e l’iterazione sui files ha richiesto un’ulteriore ciclo sulla variabile count che indica il numero della rete per una determinata risorsa di riparazione.
I files check_sound.py e check_sound_multiple.py servono a conteggiare il numero di reti non sound ottenute.

---
Successivamente, è stata eseguita un'ulteriore analisi sulla complessità delle reti. A tal proposito, i files count_singleton.py e count_multiple.py restituiscono in output un file csv dove per ogni rete sono conteggiati gli archi, le transitions e i places ed è calcolata la differenza di questi valori con gli archi, le transitions e i places presenti nella rete originaria.
