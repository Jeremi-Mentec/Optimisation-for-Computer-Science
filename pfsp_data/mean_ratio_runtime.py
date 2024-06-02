import matplotlib.pyplot as plt
import re

data = [[0 for j in range(0,11)] for i in range(1,30)]

with open('data_graph.txt', 'r') as file:
    k=0
    for line in file:
        instance, param, time = line.strip().split()
        data[k][int(float(param)*10)] = [instance,float(param),float(time)]
        if float(param)==1:
            k += 1

#calculating ratio runtime
for i in range(0,len(data)):
    min = data[i][0][2]
    for j in range(1,len(data[i])):
        if data[i][j][2] < min:
            min = data[i][j][2]
    for j in range(0,len(data[i])):
        data[i][j] = data[i][j]+[data[i][j][2] / min]

DepthThreshols = []
Means = []
StandardDeviation = []
for j in range(0,len(data[0])):
    sum_score = 0
    s = 0
    for i in range(0,len(data)):
        sum_score += data[i][j][3]
    DepthThreshols.append(data[i][j][1])
    Means.append(sum_score / len(data))
    for i in range(0,len(data)):
        s += (data[i][j][3]-Means[j])**2
    StandardDeviation.append((s/len(data))**(1/2))


plt.figure(figsize=(8, 6))
plt.plot(DepthThreshols, Means, marker='o', linestyle='-', label='LBMix')
plt.axhline(y=Means[-1], color='r', linestyle='--',label='only LB1')
plt.axhline(y=Means[0], color='g', linestyle='--',label='only LB2')
plt.title('Average runtime ratio according to depth threshold')
plt.xlabel('depthThreshold')
plt.ylabel('Average runtime ratio')
plt.grid(True)
plt.legend()
plt.show()
#plt.savefig('avg.png')  
plt.close()
print(Means) 

plt.figure(figsize=(8, 6))
plt.plot(DepthThreshols, StandardDeviation, marker='o', linestyle='-')
plt.axhline(y=StandardDeviation[-1], color='r', linestyle='--',label='only LB1')
plt.axhline(y=StandardDeviation[0], color='g', linestyle='--',label='only LB2')
plt.title('standard deviation runtime ratio according to depth threshold')
plt.xlabel('depth threshold')
plt.ylabel('runtime ratio')
plt.grid(True)
plt.show()
#plt.savefig('std.png')  
plt.close()
print(StandardDeviation)

X = [i for i in range(29)]
LB1 = []
LB2 = []
LBMix = []
for i in range(29):
    LB1.append(data[i][-1][3])
    LB2.append(data[i][0][3])
    LBMix.append(data[i][3][3])
plt.figure(figsize=(8, 6))
plt.plot(X, LB2, marker='o', linestyle='-', label='LB2')
plt.plot(X, LBMix, marker='o', linestyle='-', label='LBMix (depth threshold = 0.3)')
plt.plot(X, LB1, marker='o', linestyle='-', label='LB1')
plt.title('Graph showing runtime ratio as a function of intances')
plt.xlabel('Instance')
plt.ylabel('Runtime Ratio')
plt.grid(True)
plt.legend()
plt.show()
#plt.savefig('e.png')  