#!/usr/bin/python

import sys
import numpy as np
import csv

Name = sys.argv[1]      # name of experiment
N = int(sys.argv[2])    # number of clusters
Beta = float(sys.argv[3])    # performance penalty
distFile = sys.argv[4]      # distance file
labelFile = sys.argv[5]     # label file

f = open(Name+"_"+str(sys.argv[2])+"_"+str(sys.argv[3])+".py",'w')

T = []
with open(distFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for line in csvreader:
        T.append(float(line[1]))

M = []
with open(labelFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for line in csvreader:
        if(len(M) < int(line[1])):
            M.append(1)
        else:
            M[int(line[1])-1] = M[int(line[1])-1] + 1

f.write("import math\n")
# f.write("import numpy as np\n")
f.write("import time\n")
f.write("import sys\n")
f.write("from gurobipy import *\n")

f.write("Beta = "+str(Beta)+"\n")
f.write("M = "+str(M)+"\n")
f.write("T = "+str(T)+"\n")
f.write("N = "+str(N)+"\n")

f.write("k = 0\n")
f.write("for y in T:\n")
f.write("   min = y\n")
f.write("   i = k\n")
f.write("   while i < len(T):\n")
f.write("      if(T[i] <= min):\n")
f.write("         min = T[i]\n")
f.write("         j = i\n")
f.write("      i = i + 1\n")
f.write("   tmp = M[j]\n")
f.write("   M[j] = M[k]\n")
f.write("   M[k] = tmp\n")
f.write("   tmp = T[j]\n")
f.write("   T[j] = T[k]\n")
f.write("   T[k] = tmp\n")
f.write("   k = k + 1\n")
f.write("T = [x for x in T]\n")
f.write("M = [x for x in M]\n\n")

f.write("S = 0\n")
f.write("for x in M: \n")
f.write("   S += x \n")
# f.write("min_M = np.max(M)\n")

init_p = np.dot(T,M)
constant = init_p * (Beta + 1)

# f.write("init_p = np.dot(T,M) \n")
f.write("init_p = 0.0\n")
f.write("for x,y in zip(T,M): \n")
f.write("   init_p += x * y \n")
f.write("constant = init_p * (Beta + 1.0) \n")
f.write("m = Model(\""+Name+"_"+str(sys.argv[2])+"_"+str(sys.argv[3])+"\")\n")

i = 0
k = 0
flag = 0
while i < N:
    j = 0
    while j < N:
        if j >= i:
            f.write("x"+str(i)+str(j)+" = "+"m.addVar(lb=0.0,ub=1.0,name=\"x"+str(i)+str(j)+"\")\n")
        else:
            f.write("x"+str(i)+str(j)+" = "+"m.addVar(lb=0.0,ub=0.0,name=\"x"+str(i)+str(j)+"\")\n")
        j = j + 1
    i = i + 1
f.write("X = "+"m.addVar(lb=0.0,ub=S,name=\"X\")\n")

i = 0
while i < N:
    f.write("D"+str(i)+" = "+"m.addVar(lb=0.0,ub=S,name=\"D"+str(i)+"\")\n")
    i = i + 1

i = 0
while i < N:
	j = 0
	f.write("m.addConstr(")
	while j < N:
	    if j < N - 1:
	        f.write("x"+str(i)+str(j)+" + ")
	    else:
	        f.write("x"+str(i)+str(j))
	    j = j + 1
	f.write(" == 1)\n")   
	i = i + 1

i = 0
k = 0
f.write("m.addConstr(constant >= ")
while i < N:
    j = i
    while j < N:
        if j < N - 1 or i < N - 1:
            f.write("("+"M["+str(i)+"])*x"+str(i)+str(j)+"*(T["+str(j)+"]) + ")
        else:
            f.write("("+"M["+str(i)+"])*x"+str(i)+str(j)+"*(T["+str(j)+"])")
        j = j + 1
    i = i + 1
f.write(")\n")

i = N - 1
k = 0
while i >= 0:
    f.write("m.addConstr(")
    j = N - i - 1
    while j < N:
        tmp = i+((j-k)*N)
        if j != N - 1:
            f.write("M["+str(j-k)+"]"+"*x"+str(j-k)+str(i)+" + ")
        else:
            f.write("M["+str(j-k)+"]"+"*x"+str(j-k)+str(i))
        j = j + 1
    f.write(" - D"+str(i)+" == 0)\n")
    f.write("d"+str(i)+" = m.addVar(vtype=GRB.BINARY, name=\"d"+str(i)+"\")\n")
    f.write("m.addConstr(D"+str(i)+" >= d"+str(i)+")\n")
    f.write("m.addConstr(D"+str(i)+" <= S * d"+str(i)+")\n")
    k = k + 1
    i = i - 1
f.write("\n\n")
# f.write("m.addConstr(D9 == 0)\n")

i = 0
while i < N:
    f.write("m.addConstr(X <= (D"+str(i)+") + (1 - d"+str(i)+") * S)\n")
    i = i + 1
f.write("m.setObjective(X, GRB.MAXIMIZE)\n")

f.write("startTime = int(round(time.time() * 1000))\n\n")
# f.write("m.Params.MIPFocus=2\n")
# f.write("m.Params.SubMIPNodes=500000000\n")
# f.write("m.Params.MIPGap=0.00000000001\n")
f.write("m.Params.IntFeasTol=0.1\n")
f.write("m.optimize()\n\n")
f.write("endTime = int(round(time.time() * 1000))\n")
f.write("rTime = endTime - startTime\n")
f.write("print(\"Time taken to calculate (in milli-seconds):\")\n")
f.write("print(rTime)\n")
f.write("f1 = open(\"res_"+Name+"_"+str(sys.argv[2])+"_"+str(sys.argv[3])+".txt\",\'w\')\n")
f.write("f1.write(\'\\n\')\n")
f.write("f1.write(str(rTime))\n")
f.write("f1.write(\'\\n\')\n")
f.write("for d in m.getVars():\n")
f.write("   name = d.varName\n")
f.write("   val = d.x\n")
# f.write("   print(str(name) + \" --> \" + str(val))\n")
f.write("   f1.write(str(name)+\" \")\n")
f.write("   f1.write(str(val))\n")
f.write("   f1.write(\'\\n\')\n")
f.write("i = 0 \n")
f.write("final_perf = 0 \n")
f.write("res = m.getAttr(\"X\", m.getVars())\n")
f.write("while i < N:\n")
f.write("   j = i \n")
f.write("   while j < N:\n")
f.write("      if(res[i*N+j] > 0.0001): \n")
f.write("         final_perf = final_perf + M[i] * res[i*N+j]*T[j] \n")
f.write("      j = j + 1\n")
f.write("   i = i + 1\n")
f.write("final_perf = final_perf \n")
f.write("print(\"Final Performance overhead: \")\n")
f.write("print(final_perf/init_p - 1)\n")
f.write("f1.close()\n")

f.close()
