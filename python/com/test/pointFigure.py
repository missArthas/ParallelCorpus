# coding=utf-8

import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt


import sys
reload(sys)
sys.setdefaultencoding('utf8')

sampleNo = 1000;
# 一维正态分布
# 下面三种方式是等效的
mu = 0.5
sigma = 0.1
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo )
plt.subplot(111)
plt.xlabel("theta值")
plt.ylabel("出现次数")
plt.title("阈值选择")
plt.hist(s, 30, normed=True)

plt.show()
# np.random.seed(0)
# s = sigma * np.random.randn(sampleNo ) + mu
# plt.subplot(142)
# plt.hist(s, 30, normed=True)
#
# np.random.seed(0)
# s = sigma * np.random.standard_normal(sampleNo ) + mu
# plt.subplot(143)
# plt.hist(s, 30, normed=True)
#
# # 二维正态分布
# mu = np.array([[1, 5]])
# Sigma = np.array([[1, 0.5], [1.5, 3]])
# R = cholesky(Sigma)
# s = np.dot(np.random.randn(sampleNo, 2), R) + mu
# plt.subplot(144)
# # 注意绘制的是散点图，而不是直方图
# plt.plot(s[:,0],s[:,1],'+')
# plt.show()