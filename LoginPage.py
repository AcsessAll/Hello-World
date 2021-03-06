from tkinter import *  
from tkinter.messagebox import *  
from MainP import *  
  
class LoginPage(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root
        self.root.title('成绩管理系统')  
        self.root.geometry('%dx%d' % (300, 200)) #设置窗口大小  
        self.username = StringVar()  #TK库内部定义的字符串变量类型
        self.password = StringVar()  
        self.createPage()  
  
    def createPage(self):
        self.page = Frame(self.root) #创建Frame  
        self.page.pack()  
        Label(self.page).grid(row=0, stick=W)  
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)  
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)  
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, column=0, pady=5)
        Button(self.page, text='注册', command=self.register).grid(row=3, column=1, pady=5)  
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2, pady=5)
        
  
    def loginCheck(self):  
        name = self.username.get()  
        password = self.password.get()
        if self.isLegalUser(name,password):
            self.page.destroy()  #清空界面 
            MainP(self.root)  
        else:  
            showinfo(title='错误', message='账号或密码错误！')
            
    def isLegal(self,string):
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in string:
            if i in alp:
                pass #直接跳出
            else:
                return False
        return True
        
    def isLegalUser(self,name,password):
        f = open('账号密码.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name and  info[1].strip()==password :
                 f.close()
                 return True
        return False

                
    def register(self):
        name = self.username.get()  
        password = self.password.get()
        if len(name)==0 or len(password)==0:
            showinfo(title='错误', message='账号密码不能为空')
            return
        for i in password:
            if i is ',' or i is ' ':
                showinfo(title='错误', message='密码不能含有非法字符')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='错误', message='账号不能含有非法字符')
            return
        
        f = open('账号密码.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name:
                 messagebox.showinfo(title='结果', message ="已存在该用户信息！")
                 f.close()
                 return
        f.close()
        
        f = open('账号密码.csv','a',encoding='utf-8')
        f.write('{},{}\n'.format(name,password))
        f.close()
        messagebox.showinfo(title='提示', message ="注册成功")
