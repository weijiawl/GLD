import re
import datetime
a = ':::::::::::近期出现异常::::::::::::::::::::::/:/::::::::::::::/:::::/:::::::281小时35分钟::::制裁::::'
if a.find('小时') > -1:
    arr = a.split('小时')
    temp_h = re.sub("\D", "", arr[0])
    d1 = datetime.datetime.now()
    #制裁的小时+1
    #转换成秒加到当前时间
    print(str(int(temp_h)+1) + '小时')
    z_time = (int(temp_h)+1) * 60 * 60
    print(z_time)
    delta = datetime.timedelta(seconds=z_time)
    print(d1+delta)