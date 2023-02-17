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

sub = ['8','26','28','30','37','42','50','55','56','64']
alg = ['goldratt_multiple','greedy_multiple']
#alg = ['goldratt_multiple']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

#import della rete di Petri  

path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/'
import os



for a in alg: 
     
    for s in sub:
        
        for r in rr:
            path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/' + str(a) +'/' + 'testlog_' + str(s) +'/' + 'r_' + str(r) +'/'
            os.chdir(path)
            count = 0
            for file in os.listdir(path):   
                if  a == 'goldratt_multiple':
                    if count == 0:
                        net, initial_marking, final_marking = pnml_importer.apply(path + 'REPAIRED.GOLDRATT.'+ r +'.pnml')
                        count = count + 1
                    else:
                        net, initial_marking, final_marking = pnml_importer.apply(path + 'REPAIRED.GOLDRATT.'+ r + '_(' + str(count) + ')'+'.pnml')
                        count = count + 1
            
                elif a == 'greedy_multiple':
                    if count == 0:
                        net, initial_marking, final_marking = pnml_importer.apply(path + 'REPAIRED.GREEDY.'+ r +'.pnml')
                        count = count + 1
                    else:
                        net, initial_marking, final_marking = pnml_importer.apply(path + 'REPAIRED.GREEDY.'+ r + '_(' + str(count) + ')' +'.pnml')
                        count = count + 1
            
                for trans in net.transitions:
                    if "tau" in trans.label: 
                        trans.label = None
                    print(trans.label)
            
                pnml_exporter.apply(net, initial_marking, "repaired_sub" + s + "_" + a + "_" + r + "_(" + str(count - 1) + ")" +".pnml", final_marking)
          
