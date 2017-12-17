#coding=utf-8
import numpy as np
import sys
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf8')

x = [1,2,3,4,5,6,7,8,9,10]
y = [0.1,0.2,0.3,0.4,0.5,0.8,0.9,0.7,0.6,0.6]
plt.figure()
plt.plot(x, y)
plt.xlabel("k值")
plt.ylabel("准确率")
plt.title("k值选择")
plt.show()
#plt.savefig("easyplot.jpg")