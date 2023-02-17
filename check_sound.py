from pm4py.evaluation.replay_fitness.variants import alignment_based, token_replay
from pm4py.algo.conformance import alignments
from pm4py.objects.conversion.log import converter as log_conversion
from pm4py.util import exec_utils
from pm4py.objects.petri_net.utils.check_soundness import check_easy_soundness_net_in_fin_marking
from enum import Enum
import deprecation
from pm4py.meta import VERSION
import warnings
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.evaluation.replay_fitness import evaluator as replay_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from pm4py.algo.conformance.alignments import algorithm
import pm4py.algo.evaluation.replay_fitness
count = 0
#sub = ['8','26','28','30','37','42','50','55','56','64']
#sub = ['7','14','19','24','28','30','33','50','56','58'] 
#sub = ['2','4','8','17','18','20','21','22','26','29','31','33','48','63','105']
sub = ['29','31','39','52','57','62','71','73','75','77'] 
alg = ['goldratt_singleton','greedy_singleton','knapsack']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
path = 'C:/Users/crist/Desktop/FileBDA/risultati_evaluation/nuovi/count_reti_non_sound/testbank2000SCCUpdated/testbank2000SCCUpdated/'
for a in alg: #seleziona l'algoritmo a nell'array alg per iterare sui diversi algoritmi
    
    for s in sub: #itera sul numero delle sub
        
        for r in rr: #itera sulle risorse di riparazione

            petri_net, initial_marking, final_marking = pnml_importer.apply(path + str(a) +'/' + 'testlog_' + str(s) +'/' + 'new_repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) +'.pnml')

            if not (check_easy_soundness_net_in_fin_marking(petri_net, initial_marking,final_marking)):
                count = count + 1  

print(count)