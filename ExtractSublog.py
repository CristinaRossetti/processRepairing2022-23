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
import mysql

def search_trace(log, dict_trace, graph):
    trace = Trace()
    for t in log:
        if t.attributes['concept:name'] == dict_trace[graph]:
            trace = t
    return trace

def export_eventlog_test(graph_list, log, dict_trace, sub):
    new_eventlog = EventLog()
    for gra in graph_list:
        tra = search_trace(log, dict_trace, gra)
        new_eventlog.append(tra)

    xes_exporter.apply(new_eventlog, '../testlog_' + sub + '.xes')

def list_graph_occurence(sub_ocmatrix_file, subname):
   
    df = pd.read_csv(sub_ocmatrix_file, sep=';')
    graphs = [] #lista dei grafi che contengono la sub
    for x in range(len(df)): #si iterano i grafi presenti nel file 
        if (df.loc[x]["Sub" + subname] == 1): #se il grafo contiene la sub 
            grafo = df.loc[x]['grafo']
            n = grafo[5:]
            graphs.append("graph" + n) #aggiungi il grafo alla lista dei grafi che contengono la sub
    return graphs

pattern = "../patterns_file_testBankSCCUpdatedCopia/"
dataset = "testBankSCCUpdatedCopia"
sub = "64"
log = xes_importer.apply(pattern + dataset + '.xes') 


def create_dict_trace(name_database):
    dict_traceid = {}

    traceid = query_with_fetchall(name_database)
    for x in traceid:
        dict_traceid['graph' + x[0]] = x[1]
    return dict_traceid

dict_trace = create_dict_trace(dataset)

graph_list = list_graph_occurence(pattern + dataset + "_table2_on_file.csv", sub)

export_eventlog_test(graph_list, log, dict_trace, sub)
