import os
from math import ceil
from Jobs import jobs

L = 12 * (1 / 84000000)
pseudo_task = 0.000005907

def Interrupt(interrupt):
    high_prio = []
    for job in jobs:
        if (interrupt != job and
            job["type"] == "Interrupt" and 
            job["priority"] > interrupt["priority"]):
            high_prio.append(job)

    Wi = 0 
    Wi_1 = interrupt["data"]["C"] 
    aux = 0
    ceil_operation = 0
    iteration = 0

    member_eq = L + interrupt["data"]["C"]

    while(Wi_1 != Wi) and (Wi_1 < interrupt["data"]["T"]):
        Wi = Wi_1
        aux = 0
        for job in high_prio:
            ceil_operation = ceil((Wi_1 + job["data"]["J"]) / job["data"]["T"]) * (L + job["data"]["C"]) 
            aux = aux + ceil_operation
        Wi_1 = member_eq + aux
        iteration = iteration + 1
    if(Wi_1 < interrupt["data"]["T"]):
        R = interrupt["data"]["J"] + Wi
        print("R[" + str(interrupt["name"]) + "] = " + str(R))
        print("     Loops: " + str(iteration))
        for job in high_prio:
            print("     Interference by: " + job["name"])       
    else:
        print("R[" + str(interrupt["name"]) + "] =  LOST DEADLINE")


def Task(task):

    high_prio = []
    for job in jobs:
        if(task != job and 
          (job["priority"] > task["priority"] or 
          job["type"] == "Interrupt")):
            high_prio.append(job)
   
    Wi = 0 
    Wi_1 = task["data"]["C"] 
    aux = 0
    ceil_operation = 0
    iteration = 0

    member_eq = task["context_switch"]["idle"]
    member_eq = member_eq + (pseudo_task * len(high_prio))
    member_eq  = member_eq + (L + task["data"]["C"])
    member_eq = member_eq + 2 * (task["data"]["b_in"]) + task["data"]["B"] + task["data"]["b_out"]
    member_eq = member_eq + task["data"]["w"]
    
    while(Wi_1 != Wi) and (Wi_1 < task["data"]["T"]):
        Wi = Wi_1
        aux = 0
        for job in high_prio:
            if job["type"] == "Interrupt":
                ceil_operation = ceil((Wi_1 + job["data"]["J"]) / job["data"]["T"]) * (L + job["data"]["C"]) 
            elif job["type"] == "Task":
                ceil_operation = ceil((Wi_1 + job["data"]["J"]) / job["data"]["T"]) * (L + task["context_switch"][job["name"]]) + job["data"]["C"] + (L + job["context_switch"][task["name"]])
            aux = aux + ceil_operation
        Wi_1 = member_eq + aux
        iteration = iteration + 1
    
    if(Wi_1 < task["data"]["T"]):
        R = task["data"]["J"] + Wi
        print("R[" + str(task["name"]) + "] = " + str(R))
        print("     Loops: " + str(iteration))
        for job in high_prio:
            print("     Interference by: " + job["name"])       
    else:
        print("R[" + str(interrupt["name"]) + "] =  LOST DEADLINE")

def WCRT(list):
    index = 0
    for job in list:
        if jobs[index]["type"] == "Interrupt":
            Interrupt(jobs[index])
        elif jobs[index]["type"] == "Task":
            Task(jobs[index])
        index = index + 1


clear = lambda: os.system('clear')
clear()
WCRT(jobs)