from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.evaluation.replay_fitness import evaluator as replay_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from pm4py.algo.conformance.alignments import algorithm
import pm4py.algo.evaluation.replay_fitness


sub = ['8','26','28','30','37','42','50','55','56','64']
#alg = ['goldtratt_singleton','greedy_singleton','knapsack']
alg = ['goldratt_singleton']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
path = 'C:/Users/crist/Desktop/FileBDA/testbank2000SCCUpdated/knapsack/testlog_77/'

import os
os.chdir(path)

for r in rr:
    for file in os.listdir(path):
        source = path + file
        if file.startswith("REPAIRED.KNAPSACK." + r + "."):
            destination = path + "REPAIRED.KNAPSACK." + r + ".pnml"
            os.rename(source, destination)

res = os.listdir(path)
print(res)