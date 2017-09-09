#-*-coding:utf-8-*-

#Cross_style记录交叉口的情况，是基本的储蓄单元！
#任务：传入[0, 0, 0, 1, 1, 0.2, 0, 0]格式数据，得到结果
class Cross_style:
    def __init__(self,info):
        self.info=self.trans(info)

    #初始转换
    def trans(self,info):
        #info=[up,right,down,left,face_fact]
        if info[4]==0.2:
            #up->down=2
            info[2]=2
        elif info[4]==0.4:
            info[3]=2
        elif info[4]==0.6:
            info[0]=2
        elif info[4]==0.8:
            info[1]=2
        return info

    #之后的转换
    def change(self,face_fact):
        if face_fact==0.2:
            self.info[2]=2
        elif face_fact==0.4:
            self.info[3]=2
        elif face_fact==0.6:
            self.info[0] = 2
        elif face_fact==0.8:
            self.info[1]=2



        '''
        if style_num[0]==2:
            if style_num[1]==1:
                self.style_shape=[1,1,0,0]
                #shape:
                
                0,1,0
                0,1,1
                0,0,0
                
            elif style_num[1]==2:
                self.style_shape=[0,1,1,0]
            elif style_num[1]==3:
                self.style_shape=[0,0,1,1]
            elif style_num[1]==4:
                self.style_shape=[0,0,0,1]
        

        if style_num[0]==3:
            if style_num[1]==1:
                self.style_shape=[1,1,1,0]
                #shape:
                
                0,1,0
                0,1,1
                0,1,0
                
            elif style_num[1]==2:
                self.style_shape=[0,1,1,1]
            elif style_num[1]==3:
                self.style_shape=[1,0,1,1]
            elif style_num[1]==4:
                self.style_shape=[1,1,0,1]
        elif style_num[0]==4:
            self.style_shape=[1,1,1,1]
        
        
        #走过之路
        if style_num[2]=="up":
            self.style_shape[2]=2
        elif style_num[2]=="down":
            self.style_shape[0] = 2
        elif style_num[2]=="left":
            self.style_shape[1] = 2
        elif style_num[2]=="right":
            self.style_shape[3] = 2

    #传入的是传感器参数，需要转换为程序语言
    def trans_fact(self,sensor):
        if sensor==[0,0]:
            return "up"
        elif sensor==[0,1]:
            return "right"
        elif sensor==[1,0]:
            return "down"
        elif sensor==[1,1]:
            return "left"
        
        
        

    def walk(self,direction):
        if direction=="up":
            self.style_shape[0]=2
        if direction=="right":
            self.style_shape[1] = 2
        if direction=="down":
            self.style_shape[2] = 2
        if direction=="left":
            self.style_shape[3] = 2

    def zero_exist(self):
        count=0
        for i in self.style_shape:
            if i==0:
                count+=1
        if count==0:
            return True
        else:
            return False
'''

#名叫Memory的栈
class Memory:


    #常规function
    def __init__(self):
        self.items = []
        # 0为pop，1为push
        self.pop_or_push = 1

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    #mul function通过输入进行记忆管理。
    def mul(self,cross_style):
        if cross_style[0]==1:

            if self.pop_or_push==1:
                self.the_cross=Cross_style(cross_style[1:5])
                self.push(self.the_cross)

            else:
                self.the_cross=self.items.pop()

            if cross_style[6]==1:
                self.pop_or_push=0




'''
a_memory=Memory()
tmp=Cross_style([3,1,'up'])
a_memory.push(tmp)
tmp=Cross_style([3,2,'up'])
a_memory.push(tmp)
print a_memory.pop().style_shape
print a_memory.pop().style_shape
'''
