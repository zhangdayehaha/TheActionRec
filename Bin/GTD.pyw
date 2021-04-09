import os
import time
import win32gui
TheTimeold=0
TheTime=0
TheTime=time.strftime('%M',time.localtime(time.time()))
allTheTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
cnt=allTheTime

NOW=''
old=''
lista=[]
listb=[]

list1=[]
list2=[]
def checkfile():
    path=os.getcwd()[:-3]
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if 'Log' not in dirs: os.mkdir(path+'Log')
    if 'W' not in dirs: os.mkdir(path+'W')
    if 'R' not in dirs: os.mkdir(path+'R')


def RecError(ErrDate):
    try:
        with open ('C:\\Users\\zhangkaifa\\Documents\\TheActtionRec\\Log\\'+allTheTime[:10]+'.txt','a+',encoding="UTF-8") as Log:
            Log.write(str(ErrDate)+'\n')
    except:
        pass
def get_path():
    global NOW
    global old
    global lista
    global listb
    global list1
    global list2
    try:
        
        qtime=time.strftime('%H:%M:%S',time.localtime(time.time()))
        window = win32gui.GetForegroundWindow()
        if (window != 0):
            NOW=win32gui.GetWindowText(window)
        else:
            NOW='锁屏状态'
            
        if NOW =='':
            NOW=old
        #print(NOW)
        if NOW not in lista:
            lista.append(NOW)
            listb.append(0)
            listb[lista.index(NOW)]+=1
        else:
            listb[lista.index(NOW)]+=1
        #print(NOW,listb[lista.index(NOW)])
        #print(win32gui.GetWindowText(window))

        if old != NOW:
            list1.append(qtime)
            list2.append(NOW)
            old = NOW
    except Exception as err :
        RecError(repr(err))
def R_DateWrite():
        global cnt
        global lista
        global listb
        try:
            TheMost=''
            TheMostTime=0
            TheTri=''
            TheTriTime=0
            TheSec=''
            TheSecTime=0

            allTheTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            if(len(listb)>=2):
                print(listb)    
                TheMost=lista[listb.index(max(listb))]
                del lista[listb.index(max(listb))]
                TheMostTime=max(listb)
                del listb[listb.index(max(listb))]

                TheSec=lista[listb.index(max(listb))]
                del lista[listb.index(max(listb))]
                TheSecTime=max(listb)
                del listb[listb.index(max(listb))]

                TheTri=lista[listb.index(max(listb))]
                del lista[listb.index(max(listb))]
                TheTriTime=max(listb)
                del listb[listb.index(max(listb))]
        except Exception as err:
            #print(repr(err))
            RecError(repr(err))

        try:
            with open ('C:\\Users\\zhangkaifa\\Documents\\TheActtionRec\\R\\'+allTheTime[:10]+'.txt','a+',encoding="UTF-8") as f:
                       f.write(cnt+'--'+allTheTime[10:]+'     :'+'    '+'一  ：'+TheMost+'   '+str(TheMostTime)+'/'+str(TheMostTime*5/60)[:4]+'分钟       '\
                               +'二  ：'+TheSec+'   '+str(TheSecTime)+'/'+str(TheSecTime*5/60)[:4]+'分钟     '\
                               +'三  ：'+TheTri+'   '+str(TheTriTime)+'/'+str(TheTriTime*5/60)[:4]+'分钟'+'\n')
                       f.close()
            with open ('C:\\Users\\zhangkaifa\\Documents\\TheActtionRec\\W\\'+allTheTime[:10]+'.txt','a+',encoding="UTF-8") as h:
                for i in list1:
                    h.write(i+':  '+list2[list1.index(i)]+'\n')
                h.close()
        except Exception as err :
            RecError(repr(err))

            try:
                with open ('C:\\Users\\zhangkaifa\\Documents\\TheActtionRec\\R\\'+allTheTime[:10]+'back'+'.txt','a+',encoding="GBK") as f:
                           f.write(cnt+'--'+allTheTime[10:]+'     :'+'    '+'一  ：'+TheMost+'   '+str(TheMostTime)+'/'+str(TheMostTime*5/60)[:4]+'分钟       '\
                                   +'二  ：'+TheSec+'   '+str(TheSecTime)+'/'+str(TheSecTime*5/60)[:4]+'分钟     '\
                                   +'三  ：'+TheTri+'   '+str(TheTriTime)+'/'+str(TheTriTime*5/60)[:4]+'分钟'+'\n')
                           f.close()
            except Exception as err:

                RecError(repr(erW_DateWriter))



        cnt=allTheTime
        lista=[]
        listb=[]

def W_DateWrite():
    global list1
    global list2

    TheDate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    try:
        with open ('C:\\Users\\zhangkaifa\\Documents\\TheActtionRec\\W\\'+TheDate[:10]+'.txt','a+',encoding="UTF-8") as h:
            for i in list1:
                h.write(i+':  '+list2[list1.index(i)]+'\n')
            h.close()
    except Exception as err:
        RecError(repr(err))
    list1=[]
    list2=[]

flag_R=0
flag_W=0
while True:
        time.sleep(5)
        TheTimeold=TheTime
        TheTime=time.strftime('%M',time.localtime(time.time()))
        allTheTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        if TheTimeold!=TheTime:
                flag_R=0
                flag_W=0
        print(TheTime,TheTimeold,flag_R,flag_W)
        get_path()
        try:

            if int(TheTime)%15==0 and flag_R==0:
                    flag_R=1
                    R_DateWrite()
                    err=allTheTime+':  Write R One '
                    print(err)
                    RecError(err)
            if int(TheTime)%2==0 and flag_W==0:
                    flag_W=1
                    
                    W_DateWrite()
                    err=allTheTime+':  Write W One '
                    print(err)
                    RecError(err)
            
        except Exception as err:
            print(repr(err))
            RecError(repr(err))
            continue


