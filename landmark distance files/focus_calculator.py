import numpy as np
import csv
import glob
import math
import matplotlib.pyplot as plt

cos = math.cos
sin = math.sin
pi = math.pi

landmark_heights = [21.9,19.7,21.2,21.5,21.6,21.8]
landmark_pixels = [197,180,188,194,190,195]
landmark_names = ['pg', 'py', 'pb', 'bp', 'gp', 'yp']
landmark_focus = [1132.42009132,1197.96954315,1169.81132075,1190.69767442,1185.18518519,1192.66055046]
 #   W = landmark_heights[landmark_names.index(sign)]
  #  F = landmark_focus[landmark_names.index(sign)]
   # D = (F * W) / P
    #return D

landmarks = list()
for fn in glob.glob('csv landmark detector files/*.csv'):

    with open(fn) as f:
        print fn
        data = [line.split() for line in f]
        d = data[20][0].split(',')
        if len(d) < 6:
            landmarks.append([ d[2], d[4], fn[-9:-7] ])
        else:
            nao = [d[6], d[8]]

print nao
print landmarks

alternative = [0,0,0,0,0,0]

for l in landmarks:
    root = math.sqrt((float(nao[0]) - float(l[0]))**2 + (float(nao[1]) - float(l[1]))**2)
    #print l[2], root, landmark_heights[landmark_names.index(l[2])]
    P = landmark_pixels[landmark_names.index(l[2])]
    D = root
    W = landmark_heights[landmark_names.index(l[2])]
    F = (P * D * 100) / W
    print l[2], F, landmark_focus[landmark_names.index(l[2])]
    alternative[landmark_names.index(l[2])] = str(F)

focus2 = 'focus2 = ['
for a in alternative:
    focus2 = focus2 + a + ', '
focus2 = focus2[:-2] + ']'
print focus2
