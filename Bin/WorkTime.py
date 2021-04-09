import re
import datetime
import matplotlib.pyplot as plt 
import time
def caltime(starttime,endtime):
    startTime2 = datetime.datetime.strptime(starttime, "%H:%M:%S")
    endTime2 = datetime.datetime.strptime(endtime, "%H:%M:%S")
    seconds = (endTime2 - startTime2).seconds
    if seconds>4000:
        print(starttime,endtime)
        seconds=1
    #print(seconds)
    return seconds
def PrintDate(Date):
    for i in range(len(Date)):
        Date[i]=Date[i]/60
   
    #rint("其他:"+str(Date[0])[:8]+'  网页：'+str(Date[1])[:8]+'工作:'+str(Date[2])[:8])
    
def GetDate(ThePath):
    starttime=''
    endtime=''
    findflag=0xff
    Rusle=[0,0,0]
    RuleList=[
            ['Python','文档','txt','py','pyw'],    #BOX1
            ['Chrome'],    #BOX2
             ]
    for line in open(ThePath,'r',encoding='ISO-8859-1'):
        if findflag!=0xff:
            
            
            endtime=line[:8]
            Rusle[findflag]=Rusle[findflag]+caltime(starttime,endtime)
            findflag=0xff
        elif starttime and endtime:
            
            endtime=line[:8]

            Rusle[2]=Rusle[2]+caltime(starttime,endtime)
            findflag=0xff
        for index,TheOne in enumerate(RuleList):
            
            for TheOneRule in TheOne:

                #print(index)
                One=re.compile(TheOneRule)
                
                TheRulse=One.findall(line)
                starttime=line[:8]
                if TheRulse :
                    findflag=index
 


    PrintDate(Rusle)
    x_list = ['other','casino','work']
    y_list = Rusle
    plt.bar(x_list, y_list)
    for i in range(len(x_list)):
        
        plt.text(i, Rusle[i]+0.1 , '%.01f' % Rusle[i], ha='center', va='top', fontsize=10)
    try:
        
        plt.pause(10)  #显示秒数
        plt.close()
        #print('11111')
        return 1
    except Exception as err:
        return repr(err)
        #print('失败')

if __name__ == "__main__":
 pass
