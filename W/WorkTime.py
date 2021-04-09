import re
import datetime
import matplotlib.pyplot as plt 
import time

def caltime(starttime,endtime):
    startTime2 = datetime.datetime.strptime(starttime, "%H:%M:%S")
    endTime2 = datetime.datetime.strptime(endtime, "%H:%M:%S")
    seconds = (endTime2 - startTime2).seconds
    if seconds>4000:
        seconds=1
        #print(starttime,endtime)
    #print(seconds)
    return seconds
def PrintDate(Date):
    for i in range(len(Date)):
        Date[i]=Date[i]/60
   
    print("其他:"+str(Date[0])[:8]+'  网页：'+str(Date[1])[:8]+'工作:'+str(Date[2])[:8])
    
def GetDate(ThePath):
    starttime=''
    endtime=''
    findflag=0xff
    Rusle=[0,0,0,0]
    RuleList=[
            ['Python','文档','txt','py','pyw'],    #BOX1
            ['Chrome',"rasp","PuTTY"],    #BOX2
            ["Sublime","uvprojx","TextAnalysisTool","调测工具","CRS","DRB","Excel","钞","Explorer"]
             ]
    for line in open(ThePath,'r',encoding='UTF-8'):
        if findflag!=0xff:
            
            
            endtime=line[:8]
            Rusle[findflag]=Rusle[findflag]+caltime(starttime,endtime)
            findflag=0xff
        elif starttime and endtime:
            #print(line)
            endtime=line[:8]
            #print(findflag)
            Rusle[3]=Rusle[3]+caltime(starttime,endtime)
            findflag=0xff
        for index,TheOne in enumerate(RuleList):
            
            for TheOneRule in TheOne:

                #print(TheOneRule)
                One=re.compile(TheOneRule)
                
                TheRulse=One.findall(line)
                starttime=line[:8]
                if TheRulse:
                    findflag=index
        if findflag ==0xff:
            pass
            #print(line)
                    


    PrintDate(Rusle)
    x_list = ['other','casino','work','no name']
    y_list = Rusle
    plt.bar(x_list, y_list)
    for i in range(len(x_list)):
        
        plt.text(i, Rusle[i]+0.1 , '%.01f' % Rusle[i], ha='center', va='bottom', fontsize=10)
    try:
        
        plt.pause(5)  #显示秒数
    except:
        print('手动关闭')
    return 2
if __name__ == "__main__":
    allTheTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    GetDate(allTheTime[:10]+".txt")
 
