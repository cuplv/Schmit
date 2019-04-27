import math
import time
import sys
from gurobipy import *
Beta = 0.5
M = [64, 64]
T = [3.16215, 1.98841484375]
N = 2
k = 0
for y in T:
   min = y
   i = k
   while i < len(T):
      if(T[i] <= min):
         min = T[i]
         j = i
      i = i + 1
   tmp = M[j]
   M[j] = M[k]
   M[k] = tmp
   tmp = T[j]
   T[j] = T[k]
   T[k] = tmp
   k = k + 1
T = [x for x in T]
M = [x for x in M]

S = 0
for x in M: 
   S += x 
init_p = 0
for x,y in zip(T,M): 
   init_p += x * y 
constant = init_p * (Beta + 1) 
m = Model("Mod_exp_3_2_0.5")
x00 = m.addVar(lb=0.0,ub=1.0,name="x00")
x01 = m.addVar(lb=0.0,ub=1.0,name="x01")
x10 = m.addVar(lb=0.0,ub=0.0,name="x10")
x11 = m.addVar(lb=0.0,ub=1.0,name="x11")
X = m.addVar(lb=0.0,name="X")
D0 = m.addVar(lb=0.0,name="D0")
D1 = m.addVar(lb=0.0,name="D1")
m.addConstr(x00 + x01 == 1)
m.addConstr(x10 + x11 == 1)
m.addConstr(constant >= (M[0])*x00*(T[0]) + (M[0])*x01*(T[1]) + (M[1])*x11*(T[1]))
m.addConstr(M[0]*x01 + M[1]*x11 - D1 == 0)
d1 = m.addVar(vtype=GRB.BINARY, name="d1")
m.addConstr(D1 >= 0.001 - (0.001) * (1 - d1))
m.addConstr(D1 <= (S+1) * d1)
m.addConstr(M[0]*x00 - D0 == 0)
d0 = m.addVar(vtype=GRB.BINARY, name="d0")
m.addConstr(D0 >= 0.001 - (0.001) * (1 - d0))
m.addConstr(D0 <= (S+1) * d0)


m.addConstr(X <= (d0 * D0) + (1 - d0) * (S+1))
m.addConstr(X <= (d1 * D1) + (1 - d1) * (S+1))
m.setObjective(X, GRB.MAXIMIZE)
startTime = int(round(time.time() * 1000))

m.optimize()

endTime = int(round(time.time() * 1000))
rTime = endTime - startTime
print("Time taken to calculate (in milli-seconds):")
print(rTime)
f1 = open("res_Mod_exp_3_2_0.5.txt",'w')
f1.write('\n')
f1.write(str(rTime))
f1.write('\n')
for d in m.getVars():
   name = d.varName
   val = d.x
   f1.write(str(name)+" ")
   f1.write(str(val))
   f1.write('\n')
i = 0 
final_perf = 0 
res = m.getAttr("X", m.getVars())
while i < N:
   j = i 
   while j < N:
      if(res[i*N+j] > 0.0001): 
         final_perf = final_perf + M[i] * res[i*N+j]*T[j] 
      j = j + 1
   i = i + 1
final_perf = final_perf 
print("Final Performance overhead: ")
print(final_perf/init_p - 1)
f1.close()
