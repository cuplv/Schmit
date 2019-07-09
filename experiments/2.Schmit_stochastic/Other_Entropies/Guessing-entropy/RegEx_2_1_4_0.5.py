# Optimization uses Sequential Least SQuares Programming (SLSQP).

from scipy.optimize import minimize
import math
import numpy as np
import time


def f(x): return -1 * (
      (x[0])**2  + 
      (x[1] + x[5])**2  + 
      (x[2] + x[6] + x[10])**2  + 
      (x[3] + x[7] + x[11] + x[15])**2)
Beta = 0.5
M = [10, 5, 5, 5]
T = [27.89572, 53.41616, 78.90792, 104.43676]
N = 4
k = 0
for y in T:
   min = y
   for i in np.arange(k,len(T),1):
      if(T[i] <= min):
         min = T[i]
         j = i
   tmp = M[j]
   M[j] = M[k]
   M[k] = tmp
   tmp = T[j]
   T[j] = T[k]
   T[k] = tmp
   k = k + 1
T = [x for x in T]
M = [x for x in M]

S = np.sum(M)
x0 = np.zeros((4,4))
init_p = np.dot(T,M) 
constant = init_p * (Beta + 1) 
i = 0
while i < N:
   j = i
   degree = N - i
   while j < N:
      x0[i][j] = 1.0/degree
      j = j + 1
   i = i + 1
x0 = np.reshape(x0,(-1,))

b=((0,1),(0,1),(0,1),(0,1),(0,0),(0,1),(0,1),(0,1),(0,0),(0,0),(0,1),(0,1),(0,0),(0,0),(0,0),(0,1))
cons= ({'type': 'eq',
'fun': lambda x: 1 - np.sum(x[0*4:1*4])},)
cons= cons + ({'type': 'eq',
'fun': lambda x: 1 - np.sum(x[1*4:2*4])},)
cons= cons + ({'type': 'eq',
'fun': lambda x: 1 - np.sum(x[2*4:3*4])},)
cons= cons + ({'type': 'eq',
'fun': lambda x: 1 - np.sum(x[3*4:4*4])},)
cons = cons + ({'type': 'ineq',
     'fun': lambda x: 2194.1421 - 
            (M[0])*x[0]*(T[0]) -
            (M[0])*x[1]*(T[1]) -
            (M[0])*x[2]*(T[2]) -
            (M[0])*x[3]*(T[3]) -
            (M[1])*x[5]*(T[1]) -
            (M[1])*x[6]*(T[2]) -
            (M[1])*x[7]*(T[3]) -
            (M[2])*x[10]*(T[2]) -
            (M[2])*x[11]*(T[3]) -
            (M[3])*x[15]*(T[3]) 
             },)

startTime = int(round(time.time() * 1000))

res = minimize(f, x0, method='SLSQP', bounds=b, constraints=cons)

endTime = int(round(time.time() * 1000))
rTime = endTime - startTime
print(res)
print("Time taken to calculate (in milli-seconds):")
print(rTime)
f1 = open("res_RegEx_2_1_4_0.5.txt",'w')
f1.write(str(res))
f1.write('\n')
f1.write(str(rTime))
f1.write('\n')
k = 0
for i in res.x:
   f1.write(str(i))
   f1.write(',')
   if k == N - 1:
      f1.write('\n')
      k = 0
   else:
      k = k + 1
i = 0 
final_perf = 0 
while i < N:
   j = i 
   while j < N:
      if(res.x[i*N+j] > 0.0001): 
         final_perf = final_perf + M[i] * res.x[i*N+j]*T[j] 
      j = j + 1
   i = i + 1
final_perf = final_perf 
print("Final Performance overhead: ")
print(final_perf/init_p - 1)
f1.close()
