# coding: utf-8

from __future__ import division
from subprocess import PIPE, Popen 

# import

import psutil
import time
import sys 
import MySQLdb
import string
from random import randrange
 
 
# 接続
connect = MySQLdb.connect(user='user', passwd='password', host='localhost', db='raspi', charset='utf8')
cursor = connect.cursor()

for i in range(0, 100):
 
  def get_cpu_temperature():
    process = Popen(['vcgencmd','measure_temp'],stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")]);

  print get_cpu_temperature(); 
  cpu_temp =  get_cpu_temperature()
  insert_stmt = 'insert into sensor(dev_id,temperature) values("b8:27:eb:f8:68:41","%s")' % cpu_temp
  cursor.execute(insert_stmt)
  connect.commit()
  time.sleep(5)

 # フェッチ
cursor.close()
 # 切断
connect.close()

print('Finish Creating Data') 
