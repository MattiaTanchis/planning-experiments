NAME = "NAME"
PATH_TO_DOMAINS = "PATH_TO_DOMAINS"
PLANNERS_X_DOMAINS = "PLANNERS_X_DOMAINS"
DOMAINS4VAL = "DOMAINS4VAL"
COMPILER = "COMPILER"
DOMAINS = "DOMAINS"
MEMORY = "MEMORY"
TIME = "TIME"
PRIORITY = "PRIORITY"
PPN = "PPN"
CONFIGS = "CONFIGS"
RUNS = "RUNS"
NO_VALIDATION_PERFORMED = 'NoValidationPerformed'

PDDL_EXTENSION = ".pddl"
DOMAIN_STR_CONST = "domain"

# Errors #####
DOMAIN_INSTANCES_ERROR = "ERROR! domain files and problem files don't match in number"
ALREADY_REGISTERED = "WARNING! planner {planner_name} already registered, skipped!"
PLANNER_NOT_FOUND = "WARNING! planner {planner_name} not found, skipped!"
PLANNER_REGISTERED = "Success! planner {planner_name} registered"
CFG_PLANNER_ERROR1 = 'ERROR! configurations file for {} not found'
CFG_PLANNER_ERROR2 = 'ERROR! configuration {} for {} not found'
##############

PLANNER_EXE_DOMAIN = "#DOMAIN#"
PLANNER_EXE_INSTANCE = "#INSTANCE#"
PLANNER_EXE_SOLUTION = "#SOLUTION#"

PLANNER_COPIES_FOLDER = "TMP"


PLANNER_DESTINATION = "#PLANNER_DESTINATION#"
PLANNER_SOURCE = "#PLANNER_SOURCE#"
MEMORY_SHELL = "#MEMORY#"
TIME_SHELL = "#TIME#"
PLANNER_EXE_SHELL = "#EXE-PLANNER#"
SHELL_COLLECT_DATA = "#COLLECT_DATA_SCRIPT#"
SHELL_SOL_FILE = "#SOL_FILE#"
SHELL_SOL_INSTANCE = "#SOL_INSTANCE#"
SHELL_SOL_DOMAIN = "#SOL_DOMAIN#"
SHELL_STDO = "#STDO#"
SHELL_STDE = "#STDE#"
SHELL_RESULTS = "#RESULTS#"
SHELL_SYSTEM = "#SYSTEM#"
SHELL_DOMAIN4VAL = "#DOMAIN4VAL#"

RM_CMD = 'rm -r -f {}'

SHELL_TEMPLATE = '''
#!/bin/bash
var=$PWD
ulimit -v #MEMORY#

mkdir #PLANNER_DESTINATION#
cp -r #PLANNER_SOURCE#/* #PLANNER_DESTINATION#

cd #PLANNER_DESTINATION#

/usr/bin/time -f "Total Runtime: %e" timeout --signal=HUP #TIME# #EXE-PLANNER#

rm -r -f #PLANNER_DESTINATION#

#COLLECT_DATA_SCRIPT# #SYSTEM# #RESULTS# #SOL_FILE# #SOL_INSTANCE# #SOL_DOMAIN# #STDO# #STDE# #DOMAIN4VAL#

'''

PPN_QSUB = '#PPN#'
PRIORITY_QSUB = '#PRIORITY#'
SCRIPT_QSUB = '#SCRIPT#'
LOG_QSUB = "#LOG#"
ERR_QSUB = "#ERR#"

QSUB_TEMPLATE  = "qsub -o #LOG# -e #ERR# -p #PRIORITY# -q longbatch -l "
QSUB_TEMPLATE += "nodes=minsky.ing.unibs.it:ppn=#PPN# "
QSUB_TEMPLATE += "#SCRIPT#"

EXPERIMENT_RUN_FOLDER = "RUN_{}"
SOURCE_FOLDER = "SOURCE"
CFG_MAP_PLANNER = "cfg_map.json"

PLANNERS_FOLDER = 'systems'
SCRIPTS_FOLDER = 'scripts'
LOG_FOLDER = 'logs'
RESULTS_FOLDER = 'results'
COLLECT_DATA_FOLDER = 'collect_data'
COLLECT_DATA = "COLLECT"