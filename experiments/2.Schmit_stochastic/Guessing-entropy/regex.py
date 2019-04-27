#!/usr/bin/python

import sys
import numpy as np
import csv

Name = sys.argv[1]      # name of experiment
N = int(sys.argv[2])    # number of clusters
Beta = float(sys.argv[3])    # performance penalty
distFile = sys.argv[4]
labelFile = sys.argv[5]

f = open(Name+"_"+sys.argv[2]+"_"+sys.argv[3]+".py",'w')

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

f.write("# Optimization uses Sequential Least SQuares Programming (SLSQP).\n\n")
f.write("from scipy.optimize import minimize\n")
f.write("import math\n")
f.write("import numpy as np\n")
f.write("import time\n")
# f.write("from numba import jit, float64, int64\n")

f.write("\n\n")
# f.write("@jit(float64(float64[:]), nopython=True, parallel=True)\n")
f.write("def f(x): return -1 * (\n")
i = 0
while i < N:
    if i == N - 1:
        j = 0
        f.write("      (")
        while j <= i:
            if j < i:
                f.write("x["+str(j*N+i)+"] + ")
            else:
                f.write("x["+str(j*N+i)+"])**2)\n")
            j = j + 1
    else:
        j = 0
        f.write("      (")
        while j <= i:
            if j < i:
                f.write("x["+str(j*N+i)+"] + ")
            else:
                f.write("x["+str(j*N+i)+"])**2  + \n")
            j = j + 1
    i = i + 1

#f.write("def constrain1(x):\n")
#f.write("   return [s for s in x]\n")
#f.write("def constrain2(x):\n")
#f.write("   return [1 - s for s in x]\n\n\n")

f.write("Beta = "+str(Beta)+"\n")
f.write("M = "+str(M)+"\n")
f.write("T = "+str(T)+"\n")
f.write("N = "+str(N)+"\n")
#f.write("M_min = np.min(M)\n")
#f.write("M_max = np.max(M)\n")
#f.write("M = [(x - M_min)/(M_max-M_min) for x in M]\n")
f.write("k = 0\n")
f.write("for y in T:\n")
f.write("   min = y\n")
f.write("   for i in np.arange(k,len(T),1):\n")
f.write("      if(T[i] <= min):\n")
f.write("         min = T[i]\n")
f.write("         j = i\n")
f.write("   tmp = M[j]\n")
f.write("   M[j] = M[k]\n")
f.write("   M[k] = tmp\n")
f.write("   tmp = T[j]\n")
f.write("   T[j] = T[k]\n")
f.write("   T[k] = tmp\n")
f.write("   k = k + 1\n")
f.write("T = [x for x in T]\n")
f.write("M = [x for x in M]\n\n")

f.write("S = np.sum(M)\n")
f.write("x0 = np.zeros(("+str(N)+","+str(N)+"))\n")
init_p = np.dot(T,M)
constant = init_p * (Beta + 1)
f.write("init_p = np.dot(T,M) \n")
f.write("constant = init_p * (Beta + 1) \n")
f.write("i = 0\n")
f.write("while i < N:\n")
f.write("   j = i\n")
f.write("   degree = N - i\n")
f.write("   while j < N:\n")
f.write("      x0[i][j] = 1.0/degree\n")
f.write("      j = j + 1\n")
f.write("   i = i + 1\n")


f.write("x0 = np.reshape(x0,(-1,))\n\n")

i = 0
f.write("b=(")
while i < N:
    j = 0
    while j < N:
        if j >= i and i*N+j < N * N - 1:
            f.write("(0,1),")
        elif j >= i:
            f.write("(0,1)")
        else:
            f.write("(0,0),")
        j = j + 1
    i = i + 1
f.write(")\n")

#f.write("cons=({\'type\': \'ineq\',\n")
#f.write("     \'fun\': constrain1},\n")
#f.write("     {\'type\': \'ineq\',\n")
#f.write("     \'fun\': constrain2})\n\n")

#f.write("cons= ({\'type\': \'ineq\',\n")
#f.write("\'fun\': lambda x: x},)\n")
#
#f.write("cons= cons + ({\'type\': \'ineq\',\n")
#f.write("\'fun\': lambda x: 1 - x},)\n")

i = 0
while i < N:
    if i == 0:
        f.write("cons= ({\'type\': \'eq\',\n")
        f.write("\'fun\': lambda x: 1 - np.sum(x["+str(i)+"*"+str(N)+":"+str(i+1)+"*"+str(N)+"])},)\n")
    else:
        f.write("cons= cons + ({\'type\': \'eq\',\n")
        f.write("\'fun\': lambda x: 1 - np.sum(x["+str(i)+"*"+str(N)+":"+str(i+1)+"*"+str(N)+"])},)\n")
    i = i + 1

f.write("cons = cons + ({\'type\': \'ineq\',\n")
f.write("     \'fun\': lambda x: "+str(constant)+" - \n")

i = 0
while i < N:
    j = i
    while j < N:
        if i < N - 1:
            f.write("            ("+"M["+str(i)+"])*x["+str(i*N+j)+"]*(T["+str(j)+"]) -\n")
        else:
            f.write("            ("+"M["+str(i)+"])*x["+str(i*N+j)+"]*(T["+str(j)+"]) \n")
        j = j + 1
    i = i + 1

f.write("             },)\n\n")

# i = N - 1
# k = 0
# while i >= 0:
#     j = N - i - 1
#     f.write("cons = cons + ({\'type\': \'ineq\',\n")
#     f.write("     \'fun\': lambda x: \n")
#     f.write("          (")
#     while j < N:
#         tmp = i+((j-k)*N)
#         if j != N - 1:
#             f.write("M["+str(j-k)+"]"+"*x["+str(tmp)+"] + ")
#         else:
#             f.write("M["+str(j-k)+"]"+"*x["+str(tmp)+"]")
#         j = j + 1
#     f.write(" - x[N*N])},)\n")
#     k = k + 1
#     i = i - 1
# f.write("\n\n")


f.write("startTime = int(round(time.time() * 1000))\n\n")
f.write("res = minimize(f, x0, method=\'SLSQP\', bounds=b, constraints=cons)\n\n")
f.write("endTime = int(round(time.time() * 1000))\n")
f.write("rTime = endTime - startTime\n")
f.write("print(res)\n")
f.write("print(\"Time taken to calculate (in milli-seconds):\")\n")
f.write("print(rTime)\n")
f.write("f1 = open(\"res_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".txt\",\'w\')\n")
f.write("f1.write(str(res))\n")
f.write("f1.write(\'\\n\')\n")
f.write("f1.write(str(rTime))\n")
f.write("f1.write(\'\\n\')\n")
f.write("k = 0\n")
f.write("for i in res.x:\n")
f.write("   f1.write(str(i))\n")
f.write("   f1.write(\',\')\n")
f.write("   if k == N - 1:\n")
f.write("      f1.write(\'\\n\')\n")
f.write("      k = 0\n")
f.write("   else:\n")
f.write("      k = k + 1\n")
f.write("i = 0 \n")
f.write("final_perf = 0 \n")
f.write("while i < N:\n")
f.write("   j = i \n")
f.write("   while j < N:\n")
f.write("      if(res.x[i*N+j] > 0.0001): \n")
f.write("         final_perf = final_perf + M[i] * res.x[i*N+j]*T[j] \n")
f.write("      j = j + 1\n")
f.write("   i = i + 1\n")
f.write("final_perf = final_perf \n")
f.write("print(\"Final Performance overhead: \")\n")
f.write("print(final_perf/init_p - 1)\n")
f.write("f1.close()\n")

f.close()
