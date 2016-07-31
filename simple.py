# coding: UTF-8
#http://blog.csdn.net/zzukun/article/details/49556715

import numpy as np

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])  

# array([[0, 0, 1],
#        [0, 1, 1],
#        [1, 0, 1],
#        [1, 1, 1]])

y = np.array([[0,1,1,0]]).T  

# array([[0],
#        [1],
#        [1],
#        [0]])

syn0 = 2*np.random.random((3,4)) - 1  

# array([[-0.05420241,  0.7826875 , -0.30437487, -0.1821956 ],
#        [-0.48511084, -0.73458496,  0.14179216,  0.84268426],
#        [ 0.29760462,  0.32772085,  0.71684772,  0.4002421 ]])

syn1 = 2*np.random.random((4,1)) - 1  

# array([[-0.24811914],
#        [ 0.60665022],
#        [-0.75200526],
#        [ 0.74293788]])

# xrange和range相比，不同点就在于xrange生成的不是一个数组，而是一个生成器

for j in xrange(60000):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
	#np.exp(34) e的x次方
    # 矩阵的乘积可以使用dot函数进行计算。对于二维数组，它计算的是矩阵乘积，
    # 对于一维数组，它计算的是其点积。当需要将一维数组当作列矢量或者行矢量
    # 进行矩阵运算时，推荐先使用reshape函数将一维数组转换为二维数组：
    # array([[ 0.5156987 ,  0.71943023,  0.67853259,  0.70289176],
    #    [ 0.43850731,  0.68877166,  0.47343054,  0.68522938],
    #    [ 0.39781179,  0.61514971,  0.76177824,  0.49108918],
    #    [ 0.32637452,  0.57975242,  0.5766507 ,  0.47032393]])
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    # array([[ 0.51699077],
    #    [ 0.91408254],
    #    [ 0.08476091],
    #    [ 0.40437916]])
    l2_delta = (y - l2)*(l2*(1-l2))
    # array([[-0.12909844],
    #    [ 0.00674758],
    #    [ 0.07100105],
    #    [-0.09739741]])
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    # array([[ 0.22465675, -0.18608475,  0.29058527, -0.2119423 ],
    #    [-0.01157593,  0.01032911, -0.01735822,  0.01144121],
    #    [-0.11851176,  0.12003216, -0.13295959,  0.13949553],
    #    [ 0.14920005, -0.16945541,  0.24536014, -0.19074288]])
    syn1 += l1.T.dot(l2_delta)
    # array([[ -7.03481765],
    #    [  7.0399996 ],
    #    [-10.40565405],
    #    [  7.76422497]])
    syn0 += X.T.dot(l1_delta)
    # array([[-0.44671819, -0.52204907,  0.52781768, -0.94800077],
    #    [-0.1724136 , -0.30638044, -0.62541248, -0.26249859],
    #    [ 0.30658456,  0.71645822,  1.13266396,  0.60935794]])















