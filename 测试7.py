# 注意的是map在python3里面，需要外挂一个list（）
from functools import reduce


class Perceptron(object):
    def __init__(self, input_num, activator):
        '''初始化感知器，设置输入参数的个数，以及激活函数。
        激活函数的类型为double -> double'''
        # 初始化激活函数，权重和偏置
        self.activator = activator
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0

    def __str__(self):
        '''
        打印学习到的权重、偏置项
        '''
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    def prediction(self, input_vec):
        '''
        输入一个样本，输出一个结果
        '''
        # input_vec[x1,x2,x3...]和weights[w1,w2,w3,...]
        # lamda定义运算规则，map函数计算[x1*w1, x2*w2, x3*w3]
        # reduce实现求和
        return self.activator(
            reduce(lambda a, b: a + b, list(map(lambda x, w: x * w, input_vec, self.weights)), 0.0)
            + self.bias)

    def train(self, input_vecs, labels, iteration, rate):
        '''
        输入训练数据：一组向量、与每个向量对应的label；以及训练轮数、学习率
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        '''
        一次迭代，把所有的训练数据过一遍
        '''
        # 把输入和输出打包在一起，成为样本的列表[(input_vec, label), ...]
        samples = zip(input_vecs, labels)
        # 而每个训练样本是(input_vec, label),感知机对每个样本进行权重更新
        for (input_vec, label) in samples:
            # 计算输出
            output = self.prediction(input_vec)
            # 更新权重
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        '''
        按照感知器规则更新权重
        '''
        # input_vec[x1,x2,x3,...]和weights[w1,w2,w3,...]
        # map实现
        # 然后利用感知器规则更新权重
        delta = label - output
        self.weights = list(map(lambda x, w: w + rate * delta * x, input_vec, self.weights))
        # 更新bias
        self.bias += rate * delta


def f(x):
    '''
    定义激活函数f
    '''
    return 1 if x > 0 else 0


def get_training_dataset():
    '''
    基于and真值表构建训练数据,注意输入集和标签要一一对应
    '''
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    # 创建感知器，输入参数个数为2（因为and是二元函数），激活函数为f
    p = Perceptron(2, f)
    # 获得输入输出
    input_vecs, labels = get_training_dataset()
    # 训练，迭代10轮, 学习速率为0.1
    p.train(input_vecs, labels, 10, 0.1)
    return p