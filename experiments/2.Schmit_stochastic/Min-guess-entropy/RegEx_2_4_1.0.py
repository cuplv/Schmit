import math
import time
import sys
from gurobipy import *
Beta = 1.0
M = [10, 5, 5, 5]
T = [27.89572, 53.41616, 78.90792, 104.43676]
N = 4
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
m = Model("RegEx_2_4_1.0")
x00 = m.addVar(lb=0.0,ub=1.0,name="x00")
x01 = m.addVar(lb=0.0,ub=1.0,name="x01")
x02 = m.addVar(lb=0.0,ub=1.0,name="x02")
x03 = m.addVar(lb=0.0,ub=1.0,name="x03")
x10 = m.addVar(lb=0.0,ub=0.0,name="x10")
x11 = m.addVar(lb=0.0,ub=1.0,name="x11")
x12 = m.addVar(lb=0.0,ub=1.0,name="x12")
x13 = m.addVar(lb=0.0,ub=1.0,name="x13")
x20 = m.addVar(lb=0.0,ub=0.0,name="x20")
x21 = m.addVar(lb=0.0,ub=0.0,name="x21")
x22 = m.addVar(lb=0.0,ub=1.0,name="x22")
x23 = m.addVar(lb=0.0,ub=1.0,name="x23")
x30 = m.addVar(lb=0.0,ub=0.0,name="x30")
x31 = m.addVar(lb=0.0,ub=0.0,name="x31")
x32 = m.addVar(lb=0.0,ub=0.0,name="x32")
x33 = m.addVar(lb=0.0,ub=1.0,name="x33")
X = m.addVar(lb=0.0,name="X")
D0 = m.addVar(lb=0.0,name="D0")
D1 = m.addVar(lb=0.0,name="D1")
D2 = m.addVar(lb=0.0,name="D2")
D3 = m.addVar(lb=0.0,name="D3")
m.addConstr(x00 + x01 + x02 + x03 == 1)
m.addConstr(x10 + x11 + x12 + x13 == 1)
m.addConstr(x20 + x21 + x22 + x23 == 1)
m.addConstr(x30 + x31 + x32 + x33 == 1)
m.addConstr(constant >= (M[0])*x00*(T[0]) + (M[0])*x01*(T[1]) + (M[0])*x02*(T[2]) + (M[0])*x03*(T[3]) + (M[1])*x11*(T[1]) + (M[1])*x12*(T[2]) + (M[1])*x13*(T[3]) + (M[2])*x22*(T[2]) + (M[2])*x23*(T[3]) + (M[3])*x33*(T[3]))
m.addConstr(M[0]*x03 + M[1]*x13 + M[2]*x23 + M[3]*x33 - D3 == 0)
d3 = m.addVar(vtype=GRB.BINARY, name="d3")
m.addConstr(D3 >= 1.0 - 1.0 * (1 - d3))
m.addConstr(D3 <= (S+1) * d3)
m.addConstr(M[0]*x02 + M[1]*x12 + M[2]*x22 - D2 == 0)
d2 = m.addVar(vtype=GRB.BINARY, name="d2")
m.addConstr(D2 >= 1.0 - 1.0 * (1 - d2))
m.addConstr(D2 <= (S+1) * d2)
m.addConstr(M[0]*x01 + M[1]*x11 - D1 == 0)
d1 = m.addVar(vtype=GRB.BINARY, name="d1")
m.addConstr(D1 >= 1.0 - 1.0 * (1 - d1))
m.addConstr(D1 <= (S+1) * d1)
m.addConstr(M[0]*x00 - D0 == 0)
d0 = m.addVar(vtype=GRB.BINARY, name="d0")
m.addConstr(D0 >= 1.0 - 1.0 * (1 - d0))
m.addConstr(D0 <= (S+1) * d0)


m.addConstr(X <= (D0) + (1 - d0) * (S+1))
m.addConstr(X <= (D1) + (1 - d1) * (S+1))
m.addConstr(X <= (D2) + (1 - d2) * (S+1))
m.addConstr(X <= (D3) + (1 - d3) * (S+1))
m.setObjective(X, GRB.MAXIMIZE)
startTime = int(round(time.time() * 1000))

m.Params.MIPFocus=2
m.Params.SubMIPNodes=50000
m.Params.MIPGap=0.000001
m.Params.PreSsolve=0
m.Params.MIRCuts=0
m.Params.Cuts=0
m.optimize()

endTime = int(round(time.time() * 1000))
rTime = endTime - startTime
print("Time taken to calculate (in milli-seconds):")
print(rTime)
f1 = open("res_RegEx_2_4_1.0.txt",'w')
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
