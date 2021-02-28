"""
Approach 1:

"""
import statistics
import sys
import os
import subprocess
from scipy import stats as s
from random import randint
def read_file(filename):
    time, I, S, V, score = 0, 0, 0, 0, 0
    lame = []
    with open(filename, 'r') as f:
        line = f.readline()
        time, I, S, V, score = int(line.split()[0]), int(line.split()[1]), int(line.split()[2]), int(line.split()[3]), int(line.split()[4])
        while line:
            try:
                line = f.readline()
                lame.append(line.split())
            except:
                continue
    return time, I, score, lame[0:S], lame[S:-1]

def write_file(results : list, filename : str,avail_streets,i1,i2=1,i3=1):
    """
    To be modified
    """
    c={}
    for start,value in results.items():
        c[start]=0
        for i in value:
            if i[1] in avail_streets:
                c[start]+=1

    with open(filename, 'w') as f:
        l=0
        for start,value in results.items():
            if c[start]!=0:
                l+=1
            
        f.write('{}\n'.format(l))

        for start,value in results.items():
            if c[start]==0:
                continue
            f.write(f"{start}\n")

            f.write(f"{c[start]}\n")
            l=[]
            for i in value:
                if i[1] in avail_streets:
                    l.append(avail_streets[i[1]])
            param=statistics.mean(l)
            h=max(l)
            l=min(l)
            for i in value:
                # st=i[1]
                if i[1] in avail_streets:
                    if avail_streets[i[1]]>h-(h-l)/i1:
                        # if randint(1,100)>i1:
                            # f.write(f"{i[1]} {max(int(avail_streets[i[1]]-param),1)}\n")
                        # else:
                            f.write(f"{i[1]} {i2}\n")
                    else:
                        # f.write(f"{i[1]} {i1}\n")
                        f.write(f"{i[1]} {i3}\n")
            # pass

if __name__ == '__main__':
    files=['a.txt','b.txt','c.txt','d.txt','e.txt','f.txt']
    for i3 in range(1,5):
        for i2 in range(1,i3+1):
            i1=2 
            while i1<100:
                # for i2 in range(1,10):
                    for input_file in files:
                        # print('Processing File ', input_file)
                        time, I, score, STREETS, CARS = read_file('input/'+input_file) 
                        # print(time, I, score, STREETS, CARS)
                        # print(CARS[-4:])
                        str_f={}
                        for car in CARS:
                            # print(car[1:])
                            for street in car[1:]:
                                if street not in str_f:
                                    str_f[street]=1
                                else :
                                    str_f[street]+=1
                        d={}
                        for i in STREETS:
                            start,end,name,sec=i[0],i[1],i[2],i[3]
                            if end not in d:
                                d[end]=[(start,name)]
                            else:
                                d[end].append((start,name))

                        write_file(d,input_file+'out.txt',str_f,i1,i2,i3)

                    proc = subprocess.Popen(["./a.exe"])
                    proc.wait()
                    print(i1,i2,i3)
                    i1*=2