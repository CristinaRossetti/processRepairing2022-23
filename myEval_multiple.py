from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.evaluation.replay_fitness import evaluator as replay_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from pm4py.algo.conformance.alignments import algorithm
import pm4py.algo.evaluation.replay_fitness

import csv

log = xes_importer.apply('C:/Users/crist/OneDrive - Università Politecnica delle Marche/Desktop/Magistrale INF/Primo anno/Big Data Analytics e Machine Learning/Progetto_ BDA/ProcessRepairing/patterns_file_bpi2012decompositionExpr/bpi2012decompositionExpr.xes') 
sub = ['8','26','28','30','37','42','50','55','56','64']
#alg = ['goldtratt_singleton','greedy_singleton','knapsack']
alg = ['goldratt_multiple','greedy_multiple']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/'
f = open(path + '/results_eval_multiple_bpi2012.csv', 'a')
writer = csv.writer(f)
head = ['algorithm','sub','repair resources','sound','fitness', 'precision', 'generalization','semplicity']
writer.writerow(head)
sound = True

import os


for a in alg: #seleziona l'algoritmo a nell'array alg per iterare sui diversi algoritmi
    
    for s in sub: #itera sul numero delle sub
        
        for r in rr: #itera sulle risorse di riparazione
            path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/' + str(a) +'/' + 'testlog_' + str(s) +'/' + 'r_' + str(r) +'/'
            os.chdir(path)
            count = 0 #conteggio per le reti multiple
            
            for file in os.listdir(path):
                if(os.path.exists(path + 'repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) + '_(' + str(count) + ')' +'.pnml')):
                    net, initial_marking, final_marking = pnml_importer.apply(path + 'repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) + '_(' + str(count) + ')' +'.pnml')
                    count = count + 1
             
                    try:
                        fitness = replay_evaluator.apply(log, net, initial_marking, final_marking, variant=replay_evaluator.Variants.ALIGNMENT_BASED)
                        precision = precision_evaluator.apply(log, net, initial_marking, final_marking, variant=precision_evaluator.Variants.ALIGN_ETCONFORMANCE)
                        generalization = generalization_evaluator.apply(log, net, initial_marking, final_marking)
                        simplicity = simplicity_evaluator.apply(net)
                        row1 = [str(a), str(s), str(r),'yes', str(fitness) ,str(precision),str(generalization),str(simplicity)]
                        writer.writerow(row1)
                        print("Fitness: ", fitness)
                
                    except:
                        fitness = replay_evaluator.apply(log, net, initial_marking, final_marking, variant=replay_evaluator.Variants.TOKEN_BASED)
                        precision = precision_evaluator.apply(log, net, initial_marking, final_marking)
                        generalization = generalization_evaluator.apply(log, net, initial_marking, final_marking)
                        simplicity = simplicity_evaluator.apply(net)
                        print("Fitness: ", fitness)
                        row1 = [str(a), str(s), str(r),'no', str(fitness) ,str(precision),str(generalization),str(simplicity)]
                        writer.writerow(row1)
                        sound = False
f.close()