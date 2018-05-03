import os
try:
    f = open('ver', 'r')
    f.close()
except IOError:
    b = os.getcwd()
    print(b)
    if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(b)
    xxoo = b + '/ver'  # 在当前py文件所在路径下的new文件中创建txt
    file = open(xxoo, 'w')
    file.write('1')  # 写入内容信息
    file.close()






