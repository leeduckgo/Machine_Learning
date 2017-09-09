#-*- coding:utf-8 -*-
from Perceptron import *

class Network:


    def __init__(self):
        self.p1=Perceptron(100,100)
    def run(self,in_sensor):
        out_sensor=self.p1.activate(in_sensor)
        return out_sensor




#测试神经网络！
aNetwork=Network()
print aNetwork.run(100)
print aNetwork.run(0)

