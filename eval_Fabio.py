from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.evaluation.replay_fitness import evaluator as replay_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from pm4py.algo.conformance.alignments import algorithm
import pm4py.algo.evaluation.replay_fitness
import csv

path= 'C:/Users/crist/OneDrive - Università Politecnica delle Marche/Desktop/Magistrale INF/Primo anno/Big Data Analytics e Machine Learning/Progetto_ BDA/ProcessRepairing/patterns_file_testBankSCCUpdatedCopia/'
log = xes_importer.apply(path + 'testBank2000SCCUpdatedCopia.xes') 
#sub = ['8','26','28','30','37','42','50','55','56','64']
#sub = ['7','14','19','24','28','30','33','50','56','58'] 
#sub = ['2','4','8','17','18','20','21','22','26','29','31','33','48','63','105']
sub = ['29','31','39','52','57','62','71','73','75','77'] 
f = open(path + 'ALIGN_results_eval_testBank2000SSCUpdated_Fabio.csv', 'a')
writer = csv.writer(f)
head = ['sub','fitness', 'precision', 'generalization','semplicity']
writer.writerow(head)
sound = True

    
for s in sub: #itera sul numero delle sub
        
    net, initial_marking, final_marking = pnml_importer.apply(path + 'test_repairing/'+ 'Sub_' +str(s) + '/' + 'repaired_Sub' + str(s) + '_petriNet.pnml')
 
    fitness = replay_evaluator.apply(log, net, initial_marking, final_marking, variant=replay_evaluator.Variants.ALIGNMENT_BASED)
    precision = precision_evaluator.apply(log, net, initial_marking, final_marking, variant=precision_evaluator)
    generalization = generalization_evaluator.apply(log, net, initial_marking, final_marking)
    simplicity = simplicity_evaluator.apply(net)
    print("Fitness: ", fitness)
    row1 = [str(s),str(fitness) ,str(precision),str(generalization),str(simplicity)]
    writer.writerow(row1)
    
f.close()







