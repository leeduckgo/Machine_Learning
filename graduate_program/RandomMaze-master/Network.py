#-*- coding:utf-8 -*-
from Perceptron import *

class Network:

    '''
    #新任务：输入三个电平，输出格式为[move,turn_left,turn_right]的Boolean List
    def __init__(self):
        self.p11=Perceptron(100,50)
        self.p12=Perceptron(100,100)
        self.p21=Perceptron([50,50],100)
        self.p22=Perceptron([100,-100],100)

    def run(self,in_sensor):
        p11_result=self.p11.activate(in_sensor)
        p12_result=self.p12.activate(in_sensor)
        p21_result=self.p21.activate([p11_result,p12_result])
        p22_result=self.p22.activate([p11_result,p12_result])
        return [p21_result,p22_result]
    '''

    def __init__(self):
        self.only_p11=Perceptron(100,100)
        self.only_p12=Perceptron(-100,0)
        self.only_p13=Perceptron(-100,0)
        self.only_p14=Perceptron(-100,0)
        self.only_p21=Perceptron([20,20,20,20],80)
        self.only_p31=Perceptron([100,100,100,100],100)
    def run(self,in_sensor):
        only_p11_result=self.only_p11.activate(in_sensor[0])
        only_p12_result = self.only_p12.activate(in_sensor[1])
        only_p13_result = self.only_p13.activate(in_sensor[2])
        only_p14_result = self.only_p14.activate(in_sensor[3])
        only_p21_result =self.only_p21.activate([only_p11_result,only_p12_result,only_p13_result,only_p14_result])

        only_p11_result=self.only_p11.activate(in_sensor[1])
        only_p12_result = self.only_p12.activate(in_sensor[0])
        only_p13_result = self.only_p13.activate(in_sensor[2])
        only_p14_result = self.only_p14.activate(in_sensor[3])
        only_p22_result =self.only_p21.activate([only_p11_result,only_p12_result,only_p13_result,only_p14_result])

        only_p11_result=self.only_p11.activate(in_sensor[2])
        only_p12_result = self.only_p12.activate(in_sensor[0])
        only_p13_result = self.only_p13.activate(in_sensor[1])
        only_p14_result = self.only_p14.activate(in_sensor[3])
        only_p23_result =self.only_p21.activate([only_p11_result,only_p12_result,only_p13_result,only_p14_result])

        only_p11_result=self.only_p11.activate(in_sensor[3])
        only_p12_result = self.only_p12.activate(in_sensor[1])
        only_p13_result = self.only_p13.activate(in_sensor[2])
        only_p14_result = self.only_p14.activate(in_sensor[0])
        only_p24_result =self.only_p21.activate([only_p11_result,only_p12_result,only_p13_result,only_p14_result])

        only_p31_result=self.only_p31.activate([only_p21_result,only_p22_result,only_p23_result,only_p24_result])
        return only_p31_result
'''
    def __init__(self):
        self.p1=Perceptron(100,100)
    def run(self,in_sensor):
        out_sensor=self.p1.activate(in_sensor)
        return out_sensor
    
#测试神经网络！
aNetwork=Network()
print aNetwork.run(100)
print aNetwork.run(0)
'''
aNetwork=Network()
print aNetwork.run([0,0,1,0])


