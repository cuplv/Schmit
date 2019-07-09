import math
import time
import sys
from gurobipy import *
Beta = 0.5
M = [10, 5, 5, 10, 5, 5, 5, 5]
T = [27.9106001, 53.41499822, 78.92733184, 104.4581684, 129.95481568, 155.44325986, 180.93822278, 206.47250354]
N = 8
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
m = Model("B_L_2_8_0.5")
x00 = m.addVar(lb=0.0,ub=1.0,name="x00")
x01 = m.addVar(lb=0.0,ub=1.0,name="x01")
x02 = m.addVar(lb=0.0,ub=1.0,name="x02")
x03 = m.addVar(lb=0.0,ub=1.0,name="x03")
x04 = m.addVar(lb=0.0,ub=1.0,name="x04")
x05 = m.addVar(lb=0.0,ub=1.0,name="x05")
x06 = m.addVar(lb=0.0,ub=1.0,name="x06")
x07 = m.addVar(lb=0.0,ub=1.0,name="x07")
x10 = m.addVar(lb=0.0,ub=0.0,name="x10")
x11 = m.addVar(lb=0.0,ub=1.0,name="x11")
x12 = m.addVar(lb=0.0,ub=1.0,name="x12")
x13 = m.addVar(lb=0.0,ub=1.0,name="x13")
x14 = m.addVar(lb=0.0,ub=1.0,name="x14")
x15 = m.addVar(lb=0.0,ub=1.0,name="x15")
x16 = m.addVar(lb=0.0,ub=1.0,name="x16")
x17 = m.addVar(lb=0.0,ub=1.0,name="x17")
x20 = m.addVar(lb=0.0,ub=0.0,name="x20")
x21 = m.addVar(lb=0.0,ub=0.0,name="x21")
x22 = m.addVar(lb=0.0,ub=1.0,name="x22")
x23 = m.addVar(lb=0.0,ub=1.0,name="x23")
x24 = m.addVar(lb=0.0,ub=1.0,name="x24")
x25 = m.addVar(lb=0.0,ub=1.0,name="x25")
x26 = m.addVar(lb=0.0,ub=1.0,name="x26")
x27 = m.addVar(lb=0.0,ub=1.0,name="x27")
x30 = m.addVar(lb=0.0,ub=0.0,name="x30")
x31 = m.addVar(lb=0.0,ub=0.0,name="x31")
x32 = m.addVar(lb=0.0,ub=0.0,name="x32")
x33 = m.addVar(lb=0.0,ub=1.0,name="x33")
x34 = m.addVar(lb=0.0,ub=1.0,name="x34")
x35 = m.addVar(lb=0.0,ub=1.0,name="x35")
x36 = m.addVar(lb=0.0,ub=1.0,name="x36")
x37 = m.addVar(lb=0.0,ub=1.0,name="x37")
x40 = m.addVar(lb=0.0,ub=0.0,name="x40")
x41 = m.addVar(lb=0.0,ub=0.0,name="x41")
x42 = m.addVar(lb=0.0,ub=0.0,name="x42")
x43 = m.addVar(lb=0.0,ub=0.0,name="x43")
x44 = m.addVar(lb=0.0,ub=1.0,name="x44")
x45 = m.addVar(lb=0.0,ub=1.0,name="x45")
x46 = m.addVar(lb=0.0,ub=1.0,name="x46")
x47 = m.addVar(lb=0.0,ub=1.0,name="x47")
x50 = m.addVar(lb=0.0,ub=0.0,name="x50")
x51 = m.addVar(lb=0.0,ub=0.0,name="x51")
x52 = m.addVar(lb=0.0,ub=0.0,name="x52")
x53 = m.addVar(lb=0.0,ub=0.0,name="x53")
x54 = m.addVar(lb=0.0,ub=0.0,name="x54")
x55 = m.addVar(lb=0.0,ub=1.0,name="x55")
x56 = m.addVar(lb=0.0,ub=1.0,name="x56")
x57 = m.addVar(lb=0.0,ub=1.0,name="x57")
x60 = m.addVar(lb=0.0,ub=0.0,name="x60")
x61 = m.addVar(lb=0.0,ub=0.0,name="x61")
x62 = m.addVar(lb=0.0,ub=0.0,name="x62")
x63 = m.addVar(lb=0.0,ub=0.0,name="x63")
x64 = m.addVar(lb=0.0,ub=0.0,name="x64")
x65 = m.addVar(lb=0.0,ub=0.0,name="x65")
x66 = m.addVar(lb=0.0,ub=1.0,name="x66")
x67 = m.addVar(lb=0.0,ub=1.0,name="x67")
x70 = m.addVar(lb=0.0,ub=0.0,name="x70")
x71 = m.addVar(lb=0.0,ub=0.0,name="x71")
x72 = m.addVar(lb=0.0,ub=0.0,name="x72")
x73 = m.addVar(lb=0.0,ub=0.0,name="x73")
x74 = m.addVar(lb=0.0,ub=0.0,name="x74")
x75 = m.addVar(lb=0.0,ub=0.0,name="x75")
x76 = m.addVar(lb=0.0,ub=0.0,name="x76")
x77 = m.addVar(lb=0.0,ub=1.0,name="x77")
X = m.addVar(lb=0.0,name="X")
D0 = m.addVar(lb=0.0,name="D0")
D1 = m.addVar(lb=0.0,name="D1")
D2 = m.addVar(lb=0.0,name="D2")
D3 = m.addVar(lb=0.0,name="D3")
D4 = m.addVar(lb=0.0,name="D4")
D5 = m.addVar(lb=0.0,name="D5")
D6 = m.addVar(lb=0.0,name="D6")
D7 = m.addVar(lb=0.0,name="D7")
m.addConstr(x00 + x01 + x02 + x03 + x04 + x05 + x06 + x07 == 1)
m.addConstr(x10 + x11 + x12 + x13 + x14 + x15 + x16 + x17 == 1)
m.addConstr(x20 + x21 + x22 + x23 + x24 + x25 + x26 + x27 == 1)
m.addConstr(x30 + x31 + x32 + x33 + x34 + x35 + x36 + x37 == 1)
m.addConstr(x40 + x41 + x42 + x43 + x44 + x45 + x46 + x47 == 1)
m.addConstr(x50 + x51 + x52 + x53 + x54 + x55 + x56 + x57 == 1)
m.addConstr(x60 + x61 + x62 + x63 + x64 + x65 + x66 + x67 == 1)
m.addConstr(x70 + x71 + x72 + x73 + x74 + x75 + x76 + x77 == 1)
m.addConstr(constant >= (M[0])*x00*(T[0]) + (M[0])*x01*(T[1]) + (M[0])*x02*(T[2]) + (M[0])*x03*(T[3]) + (M[0])*x04*(T[4]) + (M[0])*x05*(T[5]) + (M[0])*x06*(T[6]) + (M[0])*x07*(T[7]) + (M[1])*x11*(T[1]) + (M[1])*x12*(T[2]) + (M[1])*x13*(T[3]) + (M[1])*x14*(T[4]) + (M[1])*x15*(T[5]) + (M[1])*x16*(T[6]) + (M[1])*x17*(T[7]) + (M[2])*x22*(T[2]) + (M[2])*x23*(T[3]) + (M[2])*x24*(T[4]) + (M[2])*x25*(T[5]) + (M[2])*x26*(T[6]) + (M[2])*x27*(T[7]) + (M[3])*x33*(T[3]) + (M[3])*x34*(T[4]) + (M[3])*x35*(T[5]) + (M[3])*x36*(T[6]) + (M[3])*x37*(T[7]) + (M[4])*x44*(T[4]) + (M[4])*x45*(T[5]) + (M[4])*x46*(T[6]) + (M[4])*x47*(T[7]) + (M[5])*x55*(T[5]) + (M[5])*x56*(T[6]) + (M[5])*x57*(T[7]) + (M[6])*x66*(T[6]) + (M[6])*x67*(T[7]) + (M[7])*x77*(T[7]))
m.addConstr(M[0]*x07 + M[1]*x17 + M[2]*x27 + M[3]*x37 + M[4]*x47 + M[5]*x57 + M[6]*x67 + M[7]*x77 - D7 == 0)
d7 = m.addVar(vtype=GRB.BINARY, name="d7")
m.addConstr(D7 >= d7)
m.addConstr(D7 <= S * d7)
m.addConstr(M[0]*x06 + M[1]*x16 + M[2]*x26 + M[3]*x36 + M[4]*x46 + M[5]*x56 + M[6]*x66 - D6 == 0)
d6 = m.addVar(vtype=GRB.BINARY, name="d6")
m.addConstr(D6 >= d6)
m.addConstr(D6 <= S * d6)
m.addConstr(M[0]*x05 + M[1]*x15 + M[2]*x25 + M[3]*x35 + M[4]*x45 + M[5]*x55 - D5 == 0)
d5 = m.addVar(vtype=GRB.BINARY, name="d5")
m.addConstr(D5 >= d5)
m.addConstr(D5 <= S * d5)
m.addConstr(M[0]*x04 + M[1]*x14 + M[2]*x24 + M[3]*x34 + M[4]*x44 - D4 == 0)
d4 = m.addVar(vtype=GRB.BINARY, name="d4")
m.addConstr(D4 >= d4)
m.addConstr(D4 <= S * d4)
m.addConstr(M[0]*x03 + M[1]*x13 + M[2]*x23 + M[3]*x33 - D3 == 0)
d3 = m.addVar(vtype=GRB.BINARY, name="d3")
m.addConstr(D3 >= d3)
m.addConstr(D3 <= S * d3)
m.addConstr(M[0]*x02 + M[1]*x12 + M[2]*x22 - D2 == 0)
d2 = m.addVar(vtype=GRB.BINARY, name="d2")
m.addConstr(D2 >= d2)
m.addConstr(D2 <= S * d2)
m.addConstr(M[0]*x01 + M[1]*x11 - D1 == 0)
d1 = m.addVar(vtype=GRB.BINARY, name="d1")
m.addConstr(D1 >= d1)
m.addConstr(D1 <= S * d1)
m.addConstr(M[0]*x00 - D0 == 0)
d0 = m.addVar(vtype=GRB.BINARY, name="d0")
m.addConstr(D0 >= d0)
m.addConstr(D0 <= S * d0)


m.addConstr(X <= (D0) + (1 - d0) * S)
m.addConstr(X <= (D1) + (1 - d1) * S)
m.addConstr(X <= (D2) + (1 - d2) * S)
m.addConstr(X <= (D3) + (1 - d3) * S)
m.addConstr(X <= (D4) + (1 - d4) * S)
m.addConstr(X <= (D5) + (1 - d5) * S)
m.addConstr(X <= (D6) + (1 - d6) * S)
m.addConstr(X <= (D7) + (1 - d7) * S)
m.setObjective(X, GRB.MAXIMIZE)
startTime = int(round(time.time() * 1000))

m.Params.IntFeasTol=1e-1
m.optimize()

endTime = int(round(time.time() * 1000))
rTime = endTime - startTime
print("Time taken to calculate (in milli-seconds):")
print(rTime)
f1 = open("res_B_L_2_8_0.5.txt",'w')
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
