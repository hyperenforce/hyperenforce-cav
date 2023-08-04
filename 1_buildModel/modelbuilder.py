import re
import sys
from copy import deepcopy
import time
import timeit
import json

"""
STEP 1: EXTRACT TRACES from EXPOSE OUTPUT
"""
# HAS TO BE CORRECTLY SET UP BY THE USER
counters = ['i'] # vars simply used as counters
initialization = [] # where the variable initialization happen
EOF='/* END OF PROGRAM */' # a simple mark as ENF of a javascript

# aux global variables
trace = []
traces = []
program = []

"""
Extract infomation that we want in the enforcer from expoSE output.txt
"""
fields = {}
expose_stats = []
temp_concrete=''
temp_concrete_num=''
def extract_expose_info(file):
    global temp_concrete
    global temp_concrete_num
    global traces
    global trace
    global fields
    global expose_stats
    getting_field = False
    field_name = ''
    while file:
        line = file.readline()
        line.replace(';', '')
        if "AssertToolkit" in line:
                    continue;
        elif '[+]' in line:
            expose_stats.append(line)
        elif "Write " in line:
            if "S$" in line:
                if (len(trace)>1):
                    traces.append(trace)
                    trace = []
                continue
            flag = False
            for counter in counters:
                if ("Write " + counter in line):
                    flag = True #ignore counters
                    break;
            if (not flag):
                print_info(line)
        elif "Evaluating symbolic condition" in line:
            line = line.strip()
            print_info(line)
        elif "Initializing fresh" in line:
            name = re.search('symbolic variable (.*) using', line)
            print_info(line)
        elif "Concrete result" in line:
            print_info(line)
        elif ("Unsupported" in line) and ("concretizing" in line):
            v = re.search('concretizing (.*) and', line)
            temp_concrete = v.group(1)
            # print_info(line)
        elif ('Get field' in line) and ('[valueOf]' in line):
            # print(line)
            line=line.replace('\n','')
            v = re.search('Get field (.*)\[valueOf\]', line)
            temp_concrete_num = str(v.group(1))
        elif ('Execution function valueOf'in line):
            print_info(line)
        elif line == "":
            break
        else:
            continue
    traces.append(trace) # add last trace back
    # print(fields)

"""
Print nice-formatted expoSE information
"""
def print_info(line):
    global temp_concrete
    global temp_concrete_num
    global traces
    global trace
    line = line.replace("/Users/tzuhan/+research/hyper_enforce/python/extract_symbolic/mytests/", "")
    match = re.search('js:(\d+):', line)
    if match:
        if (int(match.group(1)) in initialization):
            line=line.replace("?", "init")
        elif ("Initializing" in line):
            line=line.strip()
        elif ('str_' in line):
            line=line.replace("?", match.group(1))
            if(temp_concrete):
                line=line.replace('\n','')
                line=line+' assign_strvar: '+str(temp_concrete)+'\n'
                temp_concrete=''
        elif('num_' in line):
            line=line.replace("?", match.group(1))
            if(temp_concrete_num):
                line=line.replace('\n','')
                line=line+' assign_numvar: '+str(temp_concrete_num)+'\n'
                temp_concrete_num=''
        else:
            line=line.replace("?", match.group(1))

    # print(line, end="") ### DEBUG
    trace += [line]
    # check_surpress(line)

#
# """
# When assigning a controllable variable, a suppressing action could be triggered.
# """
# def check_surpress(line):
#     global trace
#     if "assign" in line:
#         if (" con_") in line:
#             print("---> add surpressing here.")
#             trace += ["---> add surpressing here."]


"""
Read a Javascript program
"""
observable_states=[]
controllable_states=[]
JS_lines=[]
def read_js_program(program_file):
    global observable_states
    global initialization
    c = 0
    while program_file:
        c = c+1
        line = program_file.readline()
        JS_lines.append(line)
        # print(line)
        # if (('=' in line)
        if (('=' in line) and ('var' not in line) and ('==' not in line) and ('//' not in line)):
            observable_states.append(c)
        elif('aux' in line):
            observable_states.append(c)

        if('ucon_' not in line):
            controllable_states.append(c)

        if ("S$.symbol" in line):
            initialization.append(c)
        if (line is not "\n"):
            line = line.strip()
        program.append(line)
        if (EOF in line):
            break
    observable_states = [initialization[0]] + observable_states


"""
A helper to get variable name from expoSE output.txt
"""
def get_var_name(line):
    name = re.search('Write (.*) at', line)
    return name[1]


"""
A helper to get program line number
"""
def get_program_line_num(line):
    match = re.search('js:(\d+):', line)
    return int(match.group(1))-1


"""
A helper to get program seconds
"""
def get_expose_seconds(line):
    match = re.search('(\d+\.\d+)s', line)
    if (match):
        return float(match.group(1))
    else:
        return 0


"""
Build traces from the extracted info
"""
dict_init={}
all_traces = [] # a list of dictionaries
trace_states = []
def build_trace(program, trace):
    global trace_states
    global dict_init
    trace_states=[]
    dict_init={}
    dict_init['is_cont'] = 0
    dict_init['PC']=int(initialization[0])
    states = []
    state_dict = {}
    # init_assignments = []
    for i in range(0, len(trace)):
        # print(trace[i]) # DEBUG
        if ("Initializing" in trace[i]):
            name = re.search('symbolic variable (.*) using', trace[i])
            value = re.search('concrete value (.*)', trace[i])
            dict_init[name.group(1)] = value.group(1)
        elif ("init" in trace[i]):
            continue
            # init_assignments.append(get_concrete_value(trace[i-1], trace[i]))
        elif ("Write" in trace[i]):
            state = trace[i]
            if (len(state_dict) == 0):
                state_dict = deepcopy(dict_init) # keep previous memory
            else:
                state_dict = deepcopy(state_dict)

            line_num = get_program_line_num(state)

            # Two situations: assign a var value, or a concrete value
            if('assign_strvar' in state):
                ### assign a string variable
                name = (re.search('Write (.*) at', state)).group(1)
                value = (re.search('assign_strvar: (.*)', state)).group(1)
                state_dict[name] = value
            elif('assign_numvar' in state):
                ### assign a numeric variable
                name = (re.search('Write (.*) at', state)).group(1)
                value = (re.search('assign_numvar: (.*)', state)).group(1)
                state_dict[name] = value
            else:
                ### assign a concrete value, check what JS is doing
                line = program[line_num]
                info = line.split("=")
                name = info[0].replace('var ','').strip()
                if (name in dict_init.keys()):
                    value = info[1].strip()
                    # if value is another symbolic variables
                    if(value in state_dict.keys()):
                        value = state_dict[value]
                    # if value is a arithmetic operations
                    elif('-' in value):
                        LS = re.search('(.*)(\-)', value)[0].replace(" ", "").replace("-", "")
                        RS = re.search('(\-)(.*)', value)[0].replace(" ", "").replace("-", "").replace(";", "")
                        if (LS.isdigit()):
                            LS = float(LS)
                        else:
                            LS = float(state_dict[LS])
                        if (RS.isdigit()):
                            RS = float(RS)
                        else:
                            RS = float(state_dict[RS])
                        value = LS-RS
                    elif('+' in value):
                        LS = re.search('(.*)(\+)', value)[0].replace(" ", "").replace("+", "")
                        RS = re.search('(\+)(.*)', value)[0].replace(" ", "").replace("+", "").replace(";", "")
                        if (LS.isdigit()):
                            LS = float(LS)
                        else:
                            LS = float(state_dict[LS])
                        if (RS.isdigit()):
                            RS = float(RS)
                        else:
                            RS = float(state_dict[RS])
                        value = LS+RS
                    state_dict[name] = value

            state_dict['PC'] = line_num+1
            # print(state_dict)

            # fix this please
            if ('ucon_' not in state):
                state_dict['is_cont'] = 1
            else:
                state_dict['is_cont'] = 0

            trace_states.append(state_dict)

            # print(trace_states) # DEBUG
    trace_states.insert(0, dict_init)
    all_traces.append(trace_states)




"""
STEP 2: BUILD MODEL from EXTRACTED TRACES
"""


def helper_visualize_trace(trace):
    for state in trace:
        print(state)

"""
types for symbolic automata
"""
GLOBAL_TYPES={}
def get_types(props):
    global observable_states
    global GLOBAL_TYPES
    for p in props:
        name = p
        value = props.get(p)
        GLOBAL_TYPES[name] = []
        if (name == 'con_str_output_hex'):
            GLOBAL_TYPES[name] = ['HIGH_a', 'LOW_b']
            for i in range(0,11):
                GLOBAL_TYPES[name].append(str(i))
        elif ('num_' in name):
            bound=99
            GLOBAL_TYPES[name]=[str(x) for x in range(bound)] + [str(x) + '.0' for x in range(bound)]
        elif (name=='con_l_obs'):
            bound=40
            GLOBAL_TYPES[name]=[str(x) for x in range(bound)] + [str(x) + '.0' for x in range(bound)]
        elif (name=='con_debit_amount'):
            bound=40
            GLOBAL_TYPES[name]=[str(x) for x in range(bound)] + [str(x) + '.0' for x in range(bound)]
        elif (name=='con_str_polluted'):
            GLOBAL_TYPES[name]=["'undefined'", "'yes'", "'no'"]
        elif (name == 'con_num_longitude'):
            bound=50
            GLOBAL_TYPES[name]=[str(x) for x in range(bound)] + [str(x) + '.0' for x in range(bound)]
        elif (name == 'con_num_latitude'):
            bound=50
            GLOBAL_TYPES[name]=[str(x) for x in range(bound)] + [str(x) + '.0' for x in range(bound)]
        elif (name == 'con_str_cookie'):
            GLOBAL_TYPES[name] = ['GPS_tracking_enabled']
        elif (name == 'ucon_str_cookie'):
            GLOBAL_TYPES[name] = ['isIntern']
        elif (name == 'con_str_baseUrl'):
            GLOBAL_TYPES[name] = ['mysite.com/intern/login.php', 'mysite.com/login.php', '\'mysite.com/intern/login.php\'', '\'mysite.com/login.php\'']
        elif (name == 'str_test'):
            GLOBAL_TYPES[name] = ['not_string', 'string']
        elif (name == 'con_user'):
            GLOBAL_TYPES[name] = ['user']
        elif (value == ('true' or 'false')):
            GLOBAL_TYPES[name] = ['true', 'false']
        elif(str(value).isdigit()):
            GLOBAL_TYPES[name] = []   #TBD: scope?
            if (name == 'is_cont'):
                for i in range(0, 2):
                    GLOBAL_TYPES[name].append(str(i))
            if (name == 'PC'):
                # for i in observable_states:
                #     GLOBAL_TYPES[name].append(str(i))
                bound=100
                GLOBAL_TYPES[name]=[str(x) for x in range(bound)] + [str(x) + '.0' for x in range(bound)]
            ### cases specific scopes, csf23
            # if (name == 'con_num_longitude'):
            #     for i in range(0,11):
            #         GLOBAL_TYPES[name].append(str(i))
            # if (name == 'con_num_latitude'):
            #     for i in range(0,11):
            #         GLOBAL_TYPES[name].append(str(i))
            # if (name == 'con_baseUrl'):
            #     GLOBAL_TYPES[name] = ['dummy.php', 'page1.php', 'page2.php']
                    # GLOBAL_TYPES[name].append(s)
        else:
            GLOBAL_TYPES[name] = [value] #pure string

        GLOBAL_TYPES[name].append('null') #for a dummy initial state
        GLOBAL_TYPES[name].append('') #for a dummy initial state


index_counter = 1
def add_new_vertex(props):
    global index_counter
    code = 'plant.add_vertex(label=pt('
    for name in props:
        value = str(props[name])
        value = value.replace(';', '') #it's a quick patch to rmove ';'
        code += name + "=\"" + str(value) + "\", "
    code = code[:-2]
    code += ')) # index:' + str(index_counter) + '\n'
    index_counter = index_counter + 1
    code.replace('\"', '\'')
    return code


added_cont_edges=[]
def add_new_cont_edge(pre, post):
    global added_cont_edges
    if ((pre,post) in added_cont_edges) or (pre == post):
        # print(pre, post, '\n')
        string =  '# repeating controllable edge: (' + str(pre) + ',' + str(post) + '), ignore \n'
        return string
    else:
        added_cont_edges.append((pre, post))
    # code += str(pre) + ", "
    # code += str(post) + ")\n"
    # [(0, 3)], weight=[3]
    # ([(0, 3)], weight=[3]
    code = "plant.add_cont_edges([("
    code += str(pre) + ", "
    code += str(post) + ")], "
    code += 'weight=[1])\n'
    # code += 'weight=1' + ")\n"
    return code

added_uncon_edges=[]
def add_new_uncont_edge(pre, post):
    global added_uncon_edges
    if ((pre, post) in added_uncon_edges) or (pre == post):
        # print(pre, post, '\n')
        string = '# repeating uncontrollable edge: (' + str(pre) + ',' + str(post) + '), ignore \n'
        return string
    else:
        added_uncon_edges.append((pre,post))

    code = "plant.add_uncont_edges([("
    code += str(pre) + ", "
    code += str(post) + ")], "
    code += 'weight=[1])\n'
    # code += 'weight=1'
    return code


added_vertices=[]
trace_counter=0
def build_Kripke_structure(writer):
    global observable_states
    global all_traces
    global GLOBAL_TYPES
    global trace_counter

    trace_counter = 1

    ### get typing
    get_types(all_traces[0][0])
    to_delete = []
    for name in GLOBAL_TYPES:
        if (('supp' in name) or ('ucon_' in name)):
            to_delete.append(name)
    for n in to_delete:
        GLOBAL_TYPES.pop(n)

    writer.write('pt = DataType(')
    writer.write(str(GLOBAL_TYPES))
    writer.write(')\n')

    ### constructor
    writer.write('plant = Plant(label_type=pt)\n')

    ### add a dummy init state
    init_state={}
    for prop in dict_init:
        if (('supp' not in prop) and ('ucon_' not in prop)):
            init_state[prop] = deepcopy(dict_init[prop])

    init_state.update( (prop,'null') for prop in init_state )
    added_vertices.append(init_state)
    writer.write('# add an empty init state\n')
    # writer.write(add_new_vertex(init_state))
    writer.write('plant.add_vertex(label=pt.default_value)\n')

    writer.write('# make it initial state\n')
    writer.write('plant.initial_state_index = 0\n')

    # tracking the indices of pre- and post-states
    pre = 0
    post = 0
    decision_vars = []
    for trace in all_traces:
        writer.write('\n# trace ' + str(trace_counter) + '\n')
        trace_counter = trace_counter + 1
        # extract the decision variables

        remove_it = []
        for p in (trace[0]):
            if (('supp' in p) or ('ucon_' in p)):
                remove_it.append(p)
                writer.write('# ' + str(p) + ' = ' + str(trace[0][p]) + '\n')


        # add a counter to make sure all observable states appear in a trace
        count_obs_states = 0
        # start building the Kripke structure
        pre = 0

        for s in trace:
            # (option 1): perform path merging by removing supp vars as AP
            for to_delete in remove_it:
                del s[to_delete] #?

            while (count_obs_states != (len(observable_states))):
                curr_PC = s['PC']
                if(curr_PC == observable_states[count_obs_states]):
                    break
                new_state = deepcopy(s);
                new_state['PC'] = observable_states[count_obs_states]
                if (new_state['PC'] in controllable_states):
                    new_state['is_cont'] = 1
                else:
                    new_state['is_cont'] = 0
                if (new_state not in added_vertices):
                    added_vertices.append(new_state)
                    writer.write(add_new_vertex(new_state))
                    index = added_vertices.index(new_state)
                else:
                    index = added_vertices.index(new_state)
                    info = '# repeating state at PC=' + str(s['PC']) + ', goes back to index:' + str(index) + '\n'
                    writer.write(info)
                    post = index

                count_obs_states = count_obs_states + 1

                # writer.write(add_new_uncont_edge(pre, post))
                if (new_state['is_cont'] == 1):
                    writer.write(add_new_cont_edge(pre, post))
                else:
                    writer.write(add_new_uncont_edge(pre, post))
                pre = post

            count_obs_states = count_obs_states + 1

            # check if it's a new state
            if (s not in added_vertices):
                post = len(added_vertices)
                added_vertices.append(s)
                writer.write(add_new_vertex(s))
            else:
                index = added_vertices.index(s)
                info = '# repeating state at PC=' + str(s['PC']) + ', goes back to index:' + str(index) + '\n'
                writer.write(info)
                post = index

            if (s['PC'] in controllable_states):
                s['is_cont'] = 1
            else:
                s['is_cont'] = 0
            # check if it's a is_cont state
            if (s['is_cont'] == 1):
                writer.write(add_new_cont_edge(pre, post))
            else:
                writer.write(add_new_uncont_edge(pre, post))

            # update pre-state index
            pre = post

        for i in range(count_obs_states, len(observable_states)):
            # writer.write('----> fill another state here\n')
            new_state = deepcopy(s);
            new_state['PC'] = observable_states[i]

            if (new_state['PC'] in controllable_states):
                new_state['is_cont'] = 1
            else:
                new_state['is_cont'] = 0

            if (new_state not in added_vertices):
                post = len(added_vertices)
                added_vertices.append(new_state)
                writer.write(add_new_vertex(new_state))
                # writer.write('/////')
            else:
                index = added_vertices.index(new_state)
                info = '# repeating state at PC=' + str(new_state['PC']) + ', goes back to index:' + str(index) + '\n'
                writer.write(info)
                post = index

            if (new_state['is_cont'] == 1):
                writer.write(add_new_cont_edge(pre, post))
            else:
                writer.write(add_new_uncont_edge(pre, post))
            pre = post

        # print(added_vertices, len(added_vertices))


    # writer.write('\nreturn plant')



### MAIN ###
programname = sys.argv[1]
exposefilename = sys.argv[2]
tracesfilename = sys.argv[3]



time0_start = time.perf_counter()

read_program = open(programname, "r")
read_js_program(read_program)

time1_read_js = time.perf_counter()
# print(time1_read_js)

read_exposefile = open(exposefilename, "r")
extract_expose_info(read_exposefile)
time2_read_expose_out = time.perf_counter()


for trace in traces:
    build_trace(program, trace)
write_trace = open(tracesfilename, "w")
time3_building_traces = time.perf_counter()

for s in all_traces:
    for state in s:
        write_trace.write(str(state) + " ---> ")
    write_trace.write("(END)")
    write_trace.write("\n")
time4_writing_traces = time.perf_counter()

read_program.close()
read_exposefile.close()
write_trace.close()

### BUILD MODELS ###
modelfilename = sys.argv[4]
write_model = open(modelfilename, "w")
build_Kripke_structure(write_model)
write_model.close()
time5_build_model = time.perf_counter()

hyperautofilename = sys.argv[5]

statsfilename = sys.argv[6]
write_stats = open(statsfilename, "w")

adj = 20
write_stats.write("=== ExpoSE Statistical Report === \n")
expose_time = float(0)
keywords = ['Symbolic Values', 'Symbolic Primitives', 'General Function Call', 'Total Lines Of Code']
for s in expose_stats:
    for word in keywords:
        if (word in s):
            s = s.replace('[+] ', '')
            # print(s)
            s = s.split(':')
            if (len(s) > 1):
                s[0] = s[0] + ":"
                write_stats.write(s[0].ljust(adj) + s[1])
            else:
                write_stats.write(s[0])

            # write_stats.write('\n')

    if ('took' in s):
        expose_time = expose_time + get_expose_seconds(s)
write_stats.write('ExpoSE total time: '.ljust(adj) + '{0:.3f}'.format(expose_time) + ' s\n')

write_stats.write('\n')


### Start building Hyperenforce script


adj = 38
write_stats.write("=== HyperEnforce Statistical Report === \n")
write_stats.write('JS File name:'.ljust(adj) + str(programname) + '\n')
write_stats.write('Number of concrete traces: '.ljust(adj) + str(trace_counter-1) +'\n')
write_stats.write('Number of states: '.ljust(adj) + str(index_counter) + '\n')
write_stats.write('Number of observable states: '.ljust(adj) + str(len(observable_states)) + '\n')
write_stats.write('List of observable states: '.ljust(adj) + str(observable_states) + '\n')
# write_stats.write('Time took for reading ExpoSE info:'.ljust(adj) + f'{time2_read_expose_out - time1_read_js:0.6f} \n')
write_stats.write('Time took for extracting ExpoSE info:'.ljust(adj) + f'{time4_writing_traces - time1_read_js:0.6f} \n')
write_stats.write('Time took for building Kripke struct:'.ljust(adj) + f'{time5_build_model - time4_writing_traces:0.6f} \n')
write_stats.write('Total time:'.ljust(adj) + f'{time5_build_model - time0_start:0.6f} \n')

write_stats.close()




read_model = open(modelfilename, "r")
read_hyperauto = open(hyperautofilename, "r")

# writepyname = programname.replace('.js', '.py')
outpylocation = sys.argv[7]
# print(outlocation)
# writepyname = writepyname.replace('mytests', 'hyperenforce_out')
# writepyname = 'myoutputs/synth_' + writepyname

# print(writepyname)
with open(outpylocation, 'w') as write_python:
    # write_python.write('Create a new text file!')
    header = open('1_buildModel/modelbuilder_temp/header.txt', 'r')
    synth = open('1_buildModel/modelbuilder_temp/synth.txt', 'r')
    # header = open('myoutputs/header.txt', 'r')
    # synth = open('myoutputs/synth.txt', 'r')
    write_python.write("import logging\n")
    write_python.write("import sys\n")
    write_python.write("logging.basicConfig(stream=sys.stdout, level=logging.INFO)\n")

    for line in header:
        write_python.write(line)

    for line in read_model:
        write_python.write(line)

    for line in read_hyperauto:
        write_python.write(line)

    for line in synth:
        write_python.write(line)



### Final Endorcement
temp_c = 0
print('(states of extended plant:)')
for v in added_vertices:
    print(str(temp_c), ": ", v)
    temp_c += 1
print('size of ectended plant: ', temp_c)

# print('(uncontrollable edges: )')
# for e in added_uncon_edges:
#     print(e)
#
# print('(controllable edges: )')
# for e in added_cont_edges:
#     print(e)


# # Serializing json
# json_object = json.dumps(added_vertices, indent=4)
# # Writing to sample.json
# with open("enforce_vertices.json", "w") as outfile:
#     outfile.write(json_object)
#
# json_object = json.dumps(JS_lines, indent=0)
# # Writing to sample.json
# with open("enforce_program.json", "w") as outfile:
#     outfile.write(json_object)
