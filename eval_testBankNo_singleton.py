from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.evaluation.replay_fitness import evaluator as replay_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from pm4py.algo.conformance.alignments import algorithm
import pm4py.algo.evaluation.replay_fitness
import csv

#importa l'event log - file xes
log = xes_importer.apply('C:/Users/crist/OneDrive - Università Politecnica delle Marche/Desktop/Magistrale INF/Primo anno/Big Data Analytics e Machine Learning/Progetto_ BDA/ProcessRepairing/patterns_file_testBank2000NoRandomNoise/testBank2000NoRandomNoise.xes') 
sub = ['2','4','8','17','18','20','21','22','26','29','31','33','48','63','105']
alg = ['goldratt_singleton','greedy_singleton','knapsack']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

path = 'C:/Users/crist/Desktop/FileBDA/testBank2000NoRandomNoise/' #path della cartella che ti ho mandato

f = open(path + '/results_eval_singleton_testBank2000NoRandomNoise.csv', 'a') #nome file csv dei risultati
writer = csv.writer(f)
head = ['algorithm','sub','repair resources','sound','fitness', 'precision', 'generalization','semplicity']
writer.writerow(head)
sound = True
for a in alg: #seleziona l'algoritmo a nell'array alg per iterare sui diversi algoritmi
    
    for s in sub: #itera sul numero delle sub
        
        for r in rr: #itera sulle risorse di riparazione
            #Importa la rete con il path corrispondente all'algoritmo, al sottolog e alla risorsa di riparazione correnti
            net, initial_marking, final_marking = pnml_importer.apply(path + '/'+ a +'/' + 'testlog_' + s +'/' + 'repaired_sub'+ s + '_' + a + '_' + r +'.pnml')
            netPrint = 'repaired_sub'+ s + '_' + a + '_' + r +'.pnml'
            print(netPrint)
            
            fitness = replay_evaluator.apply(log, net, initial_marking, final_marking, variant=replay_evaluator.Variants.TOKEN_BASED)
            precision = precision_evaluator.apply(log, net, initial_marking, final_marking, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)
            generalization = generalization_evaluator.apply(log, net, initial_marking, final_marking)
            simplicity = simplicity_evaluator.apply(net)
            row1 = [str(a), str(s), str(r),'no', str(fitness) ,str(precision),str(generalization),str(simplicity)]
            writer.writerow(row1)
            
f.close()







