# coding: UTF-8
import copy, numpy as np
np.random.seed(0) #初始化随机因子

# compute sigmoid nonlinearity，正向传播更新权值函数
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative，反向传播获取更新权值大小函数，未sigmoid的导函数
def sigmoid_output_to_derivative(output):
    return output*(1-output)


# training dataset generation
int2binary = {}
binary_dim = 8
#生成10进制对应2进制表,方便校验输出误差
largest_number = pow(2,binary_dim)
binary = np.unpackbits(np.array([range(largest_number)],dtype=np.uint8).T,axis=1)

for i in range(largest_number):
    int2binary[i] = binary[i]


# input variables
alpha = 0.1 #学习速率
input_dim = 2 #输入层 
hidden_dim = 32 #隐藏层，根据收敛速率进行调整，无确定获取规则
output_dim = 1 #输出层


# initialize neural network weights
synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1 #第一层权值矩阵，维度 2，32
synapse_1 = 2*np.random.random((hidden_dim,output_dim)) - 1 #第二层权值矩阵，维度 32，1
synapse_h = 2*np.random.random((hidden_dim,hidden_dim)) - 1 #权值矩阵连接了前一时刻的隐含层与现在时刻的隐含层，维度 32，32
#存储权值更新。在我们积累了一些权值更新以后，我们再去更新权值
synapse_0_update = np.zeros_like(synapse_0) #zeros_like 创建和参数数组的形状和类型相同的数组
synapse_1_update = np.zeros_like(synapse_1)
synapse_h_update = np.zeros_like(synapse_h)
# training logic,迭代训练样例10000次
for j in range(10000):
    
    # generate a simple addition problem (a + b = c)
    a_int = np.random.randint(largest_number/2) # int version，我们要随机生成一个在范围内的加法问题。所以我们生成一个在0到最大值一半之间的整数
    a = int2binary[a_int] # binary encoding，查找a_int对应的二进制表示，然后把它存进a里面

    b_int = np.random.randint(largest_number/2) # int version
    b = int2binary[b_int] # binary encoding

    # true answer，正确结果，用于输出校验
    c_int = a_int + b_int 
    c = int2binary[c_int]
    
    # where we'll store our best guess (binary encoded)，初始化一个空的二进制数组，用来存储神经网络的预测值（便于我们最后输出）
    d = np.zeros_like(c)

    overallError = 0 #重置误差值
    #这两个list会每个时刻不断的记录layer 2的导数值与layer 1的值
    layer_2_deltas = list()
    layer_1_values = list()
    layer_1_values.append(np.zeros(hidden_dim)) #在0时刻是没有之前的隐含层的，所以我们初始化一个全为0的
    
    # moving along the positions in the binary encoding,这个循环是遍历二进制数字,正向传播，并记录误差导数
    for position in range(binary_dim):
        
        # generate input and output
        X = np.array([[a[binary_dim - position - 1],b[binary_dim - position - 1]]])
        y = np.array([[c[binary_dim - position - 1]]]).T

        # hidden layer (input ~+ prev_hidden),当每个都被变量矩阵传播过以后，我们把信息加起来。
        layer_1 = sigmoid(np.dot(X,synapse_0) + np.dot(layer_1_values[-1],synapse_h))

        # output layer (new binary representation)
        layer_2 = sigmoid(np.dot(layer_1,synapse_1))

        # did we miss?... if so by how much?，计算一下预测误差（预测值与真实值的差）
        layer_2_error = y - layer_2
        layer_2_deltas.append((layer_2_error)*sigmoid_output_to_derivative(layer_2)) #即把每个时刻的导数值都保留着
        overallError += np.abs(layer_2_error[0]) #计算误差的绝对值，并把它们加起来，这样我们就得
        #到一个误差的标量（用来衡量传播）。我们最后会得到所有二进制位的误差的总和。
        # decode estimate so we can print it out
        d[binary_dim - position - 1] = np.round(layer_2[0][0])
        
        # store hidden layer so we can use it in the next timestep
        layer_1_values.append(copy.deepcopy(layer_1))
    
    future_layer_1_delta = np.zeros(hidden_dim)
    #反向传播
    for position in range(binary_dim):
        
        X = np.array([[a[position],b[position]]])
        layer_1 = layer_1_values[-position-1]
        prev_layer_1 = layer_1_values[-position-2]
        
        # error at output layer
        layer_2_delta = layer_2_deltas[-position-1]
        # error at hidden layer
        layer_1_delta = (future_layer_1_delta.dot(synapse_h.T) + \
            layer_2_delta.dot(synapse_1.T)) * sigmoid_output_to_derivative(layer_1)
        # let's update all our weights so we can try again
        synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
        synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
        synapse_0_update += X.T.dot(layer_1_delta)
        
        future_layer_1_delta = layer_1_delta
    

    synapse_0 += synapse_0_update * alpha
    synapse_1 += synapse_1_update * alpha
    synapse_h += synapse_h_update * alpha    

    synapse_0_update *= 0
    synapse_1_update *= 0
    synapse_h_update *= 0
    
    # print out progress
    if(j % 1000 == 0):
        print ("Error:" + str(overallError))
        print ("Pred:" + str(d))
        print ("True:" + str(c))
        out = 0
        for index,x in enumerate(reversed(d)):
            out += x*pow(2,index)
        print (str(a_int) + " + " + str(b_int) + " = " + str(out))
        print ("------------")
