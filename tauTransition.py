import subprocess
from timeit import default_timer as timer
import pandas as pd
from pandas.core.common import flatten
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
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
alg = ['goldratt_singleton','greedy_singleton','knapsack']
rr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
path = 'C:/Users/crist/Desktop/FileBDA/TEST FINALI BPI2012 - RISULTATI/TEST FINALI BPI2012 - RISULTATI/'
#import della rete di Petri bpi2012  

for a in alg:     
    for s in sub:
        log = xes_importer.apply(path + 'testlog_' + s +'.xes')
        for r in rr:
            if  a == 'goldratt_singleton':
                net, initial_marking, final_marking = pnml_importer.apply(path + '/'+ a +'/' + 'testlog_' + s +'/' + '/REPAIRED.GOLDRATT.'+ r +'.pnml')
            elif a == 'greedy_singleton':
                net, initial_marking, final_marking = pnml_importer.apply(path + '/'+ a +'/' + 'testlog_' + s +'/' + '/REPAIRED.GREEDY.'+ r +'.pnml')
            elif a == 'knapsack':
                net, initial_marking, final_marking = pnml_importer.apply(path + '/'+ a +'/' + 'testlog_' + s +'/' + '/REPAIRED.KNAPSACK.'+ r +'.pnml')
            for trans in net.transitions:
                if "tau" in trans.label: 
                    trans.label = None
                print(trans.label)
            pnml_exporter.apply(net, initial_marking, "repaired_sub" + s + "_" + a + "_" + r +".pnml", final_marking)
