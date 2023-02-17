import subprocess
from timeit import default_timer as timer
import pandas as pd
from pandas.core.common import flatten
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
# from pm4py.objects.log.adapters.pandas import csv_import_adapter as csv_importer #pm4py-1.5.0.1
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from pm4py.visualization.petri_net import visualizer as petrinet_visualizer
from pm4py.visualization.petri_net.variants import token_decoration_frequency
from pm4py.objects.log.obj import EventLog
from pm4py.objects.log.obj import Trace
from pm4py.objects.log.obj import Event
from pm4py.objects.petri_net.obj import PetriNet
from pm4py.objects.petri_net.utils import petri_utils as utils
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from database.query import *
from database.query import query_with_fetchall
from pm4py.algo.conformance.alignments.petri_net import algorithm as alignment
from pm4py.algo.evaluation.replay_fitness import algorithm as replay_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
from progress.bar import IncrementalBar
import random
import argparse
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter
from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from pm4py import write_pnml, read_pnml
from pm4py.objects.petri_net.obj import Marking

log = xes_importer.apply('C:/Users/crist/OneDrive - Università Politecnica delle Marche/Desktop/Magistrale INF/Primo anno/Big Data Analytics e Machine Learning/Progetto_ BDA/ProcessRepairing/patterns_file_bpi2012decompositionExpr/bpi2012decompositionExpr.xes')
sub = ['8','26','28','30','37','42','50','55','56','64']
alg = ['goldratt_multiple','greedy_multiple']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/'
import os,csv
f = open(path + '/ALIGN_results_eval_multiple_bpi2012.csv', 'a')
writer = csv.writer(f)
head = ['algorithm','sub','repair resources','fitness', 'precision', 'generalization','semplicity']
writer.writerow(head)

for a in alg:
    for s in sub:
        for r in rr:
            path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/' + str(a) +'/' + 'testlog_' + str(s) +'/' + 'r_' + str(r) +'/'
            os.chdir(path)
            count = 0
            for file in os.listdir(path):
                if(os.path.exists(path + 'repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) + '_(' + str(count) + ')' +'.pnml')):
                    net, initial_marking, final_marking = pnml_importer.apply(path + 'repaired_sub' + str(s) + '_' + str(a) + '_' + str(r) + '_(' + str(count) + ')' +'.pnml')
                    netPrint = 'repaired_sub'+ s + '_' + a + '_' + r + '_(' + str(count) + ')' +'.pnml'
                    print(netPrint)
                    places = net.places
                    arcs=net.arcs
                    im= Marking()
                    for place in places:
                        found=0
                        for arc in arcs:
                            if arc.target.name==place.name:
                                found=1
                                break
                        if found==0:
                            print("\nPLACE: "+place.name)
                            im[place] = 1
                            break
            
                    
                    write_pnml(net, im, final_marking, "new_repaired_sub" + s + "_" + a + "_" + r + '_(' + str(count) + ')' +".pnml")
                    net, initial_marking, final_marking = read_pnml("new_repaired_sub" + s + "_" + a + "_" + r + '_(' + str(count) + ')' +".pnml")

                    fitness = replay_evaluator.apply(log, net, initial_marking, final_marking, variant=replay_evaluator.Variants.ALIGNMENT_BASED)
                    precision = precision_evaluator.apply(log, net, initial_marking, final_marking, variant=precision_evaluator)
                    generalization = generalization_evaluator.apply(log, net, initial_marking, final_marking)
                    simplicity = simplicity_evaluator.apply(net)
                    row1 = [str(a), str(s), str(r), str(fitness) ,str(precision),str(generalization),str(simplicity)]
                    writer.writerow(row1)
                    print("Fitness: ", fitness)
                    print("Precision: ", precision)
                    print("Generalization: ", generalization)
                    print("Simplicity: ", simplicity)
                count = count + 1
f.close()