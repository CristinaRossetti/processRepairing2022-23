from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.evaluation.replay_fitness import evaluator as replay_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from pm4py.algo.conformance.alignments import algorithm
import pm4py.algo.evaluation.replay_fitness


rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
path = 'C:/Users/crist/Desktop/FileBDA/testbank2000SCCUpdated/goldratt_multiple/testlog_77/'

import os
os.chdir(path)

for r in rr:
    count = 0
    for file in os.listdir(path):
        source = path + file
        if file.startswith("REPAIRED.GOLDRATT." + r + "."):
            count = count + 1
            if count > 1:
                destination = path + "REPAIRED.GOLDRATT." + r + "_(" + str(count - 1) + ")" + ".pnml"
                os.rename(source, destination)
            else: 
                destination = path + "REPAIRED.GOLDRATT." + r + ".pnml"
                os.rename(source, destination)

res = os.listdir(path)
print(res)
