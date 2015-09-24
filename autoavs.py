#power by maple
#####################
#双击运行
#修改autoavs模板
#   把要生成的数字部分替换为[num]
#       eg.  bishi[num]bishi
#修改amount为集数
#修改firstname为数字前的字段(只影响生成的avs文件名)
#修改lastname为数字后的字段
#例如对于 动漫01非常好看.MP4
#应设置
#firstname="动漫"
#lastname="非常好看"
#amount=10
#此时会生成"动漫01非常好看.avs"等10个文件
#####################
firstname=""
lastname=""
amount=12
import os
autoavs=open('autoavs.avs','r')
autoedit=autoavs.read()
for number in range(1,amount+1):
    if number < 10:
        number='0'+str(number)
    autoedited=autoedit.replace('[num]',str(number))
    avsname=firstname+str(number)+lastname+'.avs'
    avsout=open(avsname,'w+',encoding='utf-8')
    avsout.write(autoedited)
    avsout.close()
autoedit.close()