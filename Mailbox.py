# -*- coding: utf-8 -*-

#zidianDir = "C:\\Users\\Administrator\\Documents\\WeChat Files\\wxid_9stsiotzshgz22\\FileStorage\\File\\2020-12\\Mailbox\\top100w.txt"


print("*******************************************")
print("*  *       * *               * *  *       *")
print("*  *  * *  *  *             *  *  *  * *  *")
print("*  * *     *   *           *   *  * *     *")
print("*  *       *    *         *    *  *       *")
print("*  *       *     *       *     *  *       *")
print("*  *       *       *   *       *  *       *")
print("*  *       *        * *        *  *       *")
print("*  *       *         *         *  *       *")
print("*******************************************")
name = input("输入你要组合的邮箱后缀(@xxx.com):")

print(name)
emaiHz = name
with open('top100w.txt',"r") as f:
    a = f.readlines()
    for i in a:
        b= i.replace("\n","")
        c = b + emaiHz  
        with open('value.txt','a')as file:
            print(c)
            file.writelines(c+'\n')