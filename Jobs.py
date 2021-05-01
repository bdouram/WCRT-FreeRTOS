theta_1_first = {
    "name":"theta_1",
    "type":"Interrupt",
    "priority":3,
    "data":{
        "J":0.0000015, 
        "C":0.00133, 
        "B":0, 
        "T":0.005,
    }
}

theta_2_first = {
    "name":"theta_2",
    "type":"Interrupt",
    "priority":2,
    "data":{
        "J":0.0000015, 
        "C":0.003, 
        "B":0, 
        "T":0.015,
    }
}

theta_3_first = {
    "name":"theta_3",
    "type":"Interrupt",
    "priority":1,
    "data":{
        "J":0.0000015,
        "C":0.00534,
        "B":0, 
        "T":0.03,
    }
}

theta_1 = {
    "name":"theta_1",
    "type":"Interrupt",
    "priority":3,
    "data":{
        "J":0, 
        "C":0.00003825, 
        "B":0, 
        "T":0.02,
    }
}

theta_2 = {
    "name":"theta_2",
    "type":"Interrupt",
    "priority":2,
    "data":{
        "J":0, 
        "C":0.00007638, 
        "B":0, 
        "T":0.015,
    }
}

tick = {
    "name":"tick",
    "type":"Interrupt",
    "priority":1,
    "data":{
        "J":0, 
        "C":0.000001357, 
        "B":0, 
        "T":0.001,
    }
}

gamma_1 = {
    "name": "gamma_1", # Task Name
    "type":"Task", # Is the job a Task or Interrupt?
    "priority": 6, # Task Priority
    "data":{
        "J": 0, # release jitter
        "C": 0.000606375, # execution time
        "B": 0, #block time
        "T":0.02, # period
        "b_in": 0, # context switch time for low priority task (if block occurs)
        "b_out": 0,# context switch time from low priority task (if block occurs)
        "w": 0 # context_switch time for high priority task (if block imposed)
    },
    "context_switch":{
        "idle":0.000004733,  # context switch time from idle task to gamma 1.
        "gamma_2":0.00000363, # context switch time for gamma 2
        "gamma_3":0.00000363, # context switch time for gamma 3
        "gamma_4":0.000006, # context switch time for gamma 4
    }
}

gamma_2 = {
    "name": "gamma_2",
    "type":"Task",
    "priority": 5,
    "data":{
        "J": 0, 
        "C": 0.00321, 
        "B": 0.008308, 
        "T":0.022,
        "b_in":0.000002506,
        "b_out":0.000003092,
        "w": 0
    },
    "context_switch":{
        "idle":0.000005674,
        "gamma_1":0.0000025,
        "gamma_3":0.000002506,
        "gamma_4":0.000004758,
    }
}

gamma_3 = {
    "name": "gamma_3",
    "type":"Task",
    "priority": 4,
    "data":{
        "J": 0,
        "C": 0.00922,
        "B": 0,
        "T":0.021,
        "b_in": 0,
        "b_out": 0,
        "w": 0.000003092
    },
    "context_switch":{
        "idle":0.000006253,
        "gamma_1":0.0000025,
        "gamma_2":0.000003092,
        "gamma_4":0.000004372,
    }
}

gamma_4 = {
    "name": "gamma_4",
    "type":"Task",
    "priority": 3,
    "data":{
        "J": 0,
        "C": 0.001288,
        "B": 0,
        "T":0.3,
        "b_in": 0,
        "b_out": 0,
        "w": 0
    },
    "context_switch":{
        "idle":0.0000065,
        "gamma_1":0.00000515,
        "gamma_2":0.000006,
        "gamma_3":0.000006,
    }
}

#jobs = [ theta_1_first, theta_2_first, theta_3_first ]
jobs = [ theta_1, theta_2, tick, gamma_1, gamma_2, gamma_3, gamma_4 ]