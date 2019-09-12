import tushare as ts
import pandas as pd
import os
import numpy as np
import datetime
import decimal
import time
import shuangjiao
import gengxin
import zhishu
import string
from decimal import Decimal, ROUND_HALF_UP


def panduanzhangting(shoupan,qianshoupan):
    
    pct = Decimal(str(qianshoupan))/Decimal(10)+ Decimal(str(qianshoupan))
    origin_num = Decimal(str(pct))
    answer_num = origin_num.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    
   # print(str(shoupan))
    #print(str(answer_num))
    if (str(shoupan) == str(answer_num)):
        return True
    else:
        return False

#盘后选出今日炸板股及涨停股
def jinrizhangtinggu(df):
    
    zhangtinggu =pd.DataFrame(columns=('name','amount','code','flag'))
    zhabangu =pd.DataFrame(columns=('name','amount','code','flag'))
    
    shangzheng1 = ts.get_hist_data('sh',start='2019-01-05',end='2019-12-30')
    date_sh = shangzheng1.index
    aqwe = str(date_sh[0])
    lastjiaoyiri = aqwe.replace("-","")
    
    

    
    number1 = 0
    number2 = 0
    avg_pct1 = 0
    avg_pct2 = 0
    tscode = df.ts_code
    symbo = df.symbol
    name = df.name
    d = gengxin.shishijilu(df,1,lastjiaoyiri)
    
    for index2 in tscode.index:
        #if (symbo[index2] == 58):
            
            #print(symbo[index2])
            if symbo[index2] in d:
                asd = d[symbo[index2]]
                trade_price = asd[3]
                open_price = asd[4]
                high_price = asd[5]
                low_price = asd[6]
                zuo_price = asd[7]
                
                trade_price = Decimal(trade_price)
                trade_price = trade_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                
                origin_num1 = Decimal(zuo_price)
                shoupan_num = origin_num1.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                    
                origin_num2= Decimal(str(high_price))
                    
                high_num = origin_num2.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                   
                
                
                    
                if (panduanzhangting(str(trade_price),shoupan_num)):
                        zhangtinggu = zhangtinggu.append([{'name':name[index2],'amount':asd[10],'code':symbo[index2],'flag':0}])
                        #print(str(name[index2])+'-----'+str(symbo[index2]))                 
                        number1 = number1 + 1
                        #avg_pct1 =  avg_pct1 + pct[0]
                elif(panduanzhangting(str(high_num),shoupan_num)):
                        zhabangu = zhabangu.append([{'name':name[index2],'amount':asd[10],'code':symbo[index2],'flag':0}])
                        #num1 = (close[1]-high[1])/high[1]*100
                        #num2 = (openp[0]-close[1])/close[1]*100
                        #print(str(name)+'++-+++++-+-+-'+str(symbo[index2]))
                        number2 = number2 + 1
                        #avg_pct2 =  avg_pct2 + pct[0]
    if (os.path.isfile('zhangtingguchi/'+(str(lastjiaoyiri) + 'zhangtinggu.xlsx'))):
        print('无需再次更新当日涨停股池')
        print('无需再次更新当日炸板股池')
    else :
        zhangtinggu.to_excel('zhangtingguchi/'+str(lastjiaoyiri) +  'zhangtinggu.xlsx',index=False)
        zhabangu.to_excel('zhangtingguchi/'+str(lastjiaoyiri)  + 'zhabangu.xlsx',index=False)           
    print(number1)
    print(number2)
   #print(str(number1)+'-----'+str(round(avg_pct1/number1,2)))            
   #print(str(number2)+'-----'+str(round(avg_pct2/number2,2))) 
    return      
            
            
         
    '''
    for index in tscode.index:
            
            sym = symbo[index]
        #if (int(sym) == 2098):
            
            
            listdate = df.list_date
               
            isst = df.name
            
            qwe = tscode[index]
            ldate = listdate[index]                             
            
            name = df.name[index]
            
            if (os.path.isfile(str(qwe)+'-None.csv')):
                dff1 = pd.read_csv(qwe+'-None.csv')   
            else:
                print('no----'+str(qwe))
         
            
            if(dff1.shape[0]<20):
                continue
            
            
            pct = dff1.pct_chg
            close = dff1.close
            high = dff1.high
            openp = dff1.open

            origin_num1 = Decimal(str(close[1]))
            shoupan_num = origin_num1.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                
            origin_num2= Decimal(str(high[1]))
                
            high_num = origin_num2.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                #shoupan_num = shoupan_.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
              
                
            if (panduanzhangting(shoupan_num,str(close[2]))):
                    print(str(name)+'-----'+str(sym)+'  -+++++++++  '+str(pct[0]))                 
                    number1 = number1 + 1
                    avg_pct1 =  avg_pct1 + pct[0]
            elif(panduanzhangting(str(high_num),str(close[2]))):
                    
                    num1 = (close[1]-high[1])/high[1]*100
                    num2 = (openp[0]-close[1])/close[1]*100
                    print(str(name)+'++-+++++-+-+-'+str(sym)+'  -++++++  '+str(round(num1+pct[0],2)) +'++++  '+str(round(num2,2)))
                    number2 = number2 + 1
                    avg_pct2 =  avg_pct2 + pct[0]
                    
     '''          

def selectzhangtinggu(df,lastjiaoyiri):
    
    zhangtinggu =pd.DataFrame(columns=('name','amount','code','flag'))
    zhabangu =pd.DataFrame(columns=('name','amount','code','flag'))
        
    if (os.path.isfile(('zhangtingguchi/'+str(lastjiaoyiri) + '.xlsx'))):
        dangri = pd.read_excel('zhangtingguchi/'+str(lastjiaoyiri) + '.xlsx')
    else :
        print('无数据')
        return
    close = dangri.close
    name = dangri.ts_code
    amount = dangri.amount
    pre_close = dangri.pre_close
    high = dangri.high
    
    for index in close.index:       
       
        
        trade_price = Decimal(close[index])
        trade_price = trade_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        
        origin_num1 = Decimal(pre_close[index])
        shoupan_num = origin_num1.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
            
        origin_num2= Decimal(str(high[index]))
            
        high_num = origin_num2.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        
     
        
        if (panduanzhangting(str(trade_price),shoupan_num)):
            zhangtinggu = zhangtinggu.append([{'name':name[index],'amount':amount[index],'code':name[index],'flag':0}])         
               #print(str(name[index2])+'-----'+str(symbo[index2]))                 
    
                            #avg_pct1 =  avg_pct1 + pct[0]
        elif(panduanzhangting(str(high_num),shoupan_num)):
            zhabangu = zhabangu.append([{'name':name[index],'amount':amount[index],'code':name[index],'flag':0}])
                            #num1 = (close[1]-high[1])/high[1]*100
                            #num2 = (openp[0]-close[1])/close[1]*100
                            #print(str(name)+'++-+++++-+-+-'+str(symbo[index2]))
    '''
    if (os.path.isfile('zhangtingguchi/'+(str(lastjiaoyiri) + 'zhangtinggu.xlsx'))):
        print('无需再次更新当日涨停股池')
        print('无需再次更新当日炸板股池')
    else :
    '''    
    zhangtinggu.to_excel('zhangtingguchi/'+str(lastjiaoyiri) +  'zhangtinggu.xlsx',index=False)
    zhabangu.to_excel('zhangtingguchi/'+str(lastjiaoyiri)  + 'zhabangu.xlsx',index=False)           

        
    
    
    return
    
def selectlianban(df,lastjiaoyiri,lastlastjiaoyiri):
    lianbangu =pd.DataFrame(columns=('name','amount','code','times','flag'))
    if (os.path.isfile('zhangtingguchi/'+str(lastjiaoyiri) + 'zhangtinggu.xlsx') and os.path.isfile('zhangtingguchi/'+str(lastlastjiaoyiri) + 'zhangtinggu.xlsx') and os.path.isfile('zhangtingguchi/'+str(lastlastjiaoyiri) + 'lianbangu.xlsx')):
        dangrizhangting = pd.read_excel('zhangtingguchi/'+str(lastjiaoyiri) + 'zhangtinggu.xlsx')
        qianrizhangting = pd.read_excel('zhangtingguchi/'+str(lastlastjiaoyiri) + 'zhangtinggu.xlsx')
        qianrilianban = pd.read_excel('zhangtingguchi/'+str(lastlastjiaoyiri) + 'lianbangu.xlsx')
    else :
        
        print('无数据')
        return
    name1 = dangrizhangting.name
    amount1 = dangrizhangting.amount
    name2 = qianrizhangting.name
    name3 = qianrilianban.name
    times = qianrilianban.times
    
    for index1 in name1.index:
                
        for index3 in name3.index:
            if (str(name1[index1] == str(name3[index3]))):
                timess = int(times[index3])+1
                lianbangu = lianbangu.append([{'name':name1[index1],'amount':amount1[index1],'code':name1[index1],'times':int(timess),'flag':0}]) 
                break
        
        for index2 in name2.index:
            if (str(name1[index1] == str(name2[index2]))):
                lianbangu = lianbangu.append([{'name':name1[index1],'amount':amount1[index1],'code':name1[index1],'flag':0}]) 
    lianbangu.to_excel('zhangtingguchi/'+str(lastjiaoyiri)  + 'lianbangu.xlsx',index=False)      

    
    return

    
                
    #print(str(number1)+'-----'+str(round(avg_pct1/number1,2)))            
    #print(str(number2)+'-----'+str(round(avg_pct2/number2,2))) 
#选出今日连板股 
def jinrilianban(df):
    
    lianbangu =pd.DataFrame(columns=('name','amount','code','times','flag'))

    
    shangzheng1 = ts.get_hist_data('sh',start='2019-01-05',end='2019-12-30')
    date_sh = shangzheng1.index
    aqwe = str(date_sh[0])
    lastjiaoyiri = aqwe.replace("-","")
    
    today = time.strftime("%Y%m%d",time.localtime())
    
    ts.set_token('a3f5b59633004207469b9cf3a93191241b31bc9e47df07d422e0cc4c')
    pro = ts.pro_api()
    dff = pro.trade_cal(exchange='', start_date='20180101', end_date=today+'')
    #dff.to_excel('sssssssssss.xlsx',index=False)
    cal_date = dff.cal_date
    
    index0 = dff.shape[0] - 1
    
    while (str(cal_date[index0])!=str(lastjiaoyiri)):
        index0 = index0 - 1
    index0 = index0-1
    while (str(dff.is_open[index0])!= '1'):
        index0 = index0 - 1
    print('上个交易日'+cal_date[index0])
    
    
    dangri = None
    if (os.path.isfile(('zhangtingguchi/'+str(lastjiaoyiri) + 'zhangtinggu.xlsx'))):
        dangri = pd.read_excel('zhangtingguchi/'+str(lastjiaoyiri) + 'zhangtinggu.xlsx')
    else :
        jinrizhangtinggu(df)
    
    
    if (os.path.isfile(('zhangtingguchi/'+str(cal_date[index0]) + 'zhangtinggu.xlsx'))):
        zuori = pd.read_excel('zhangtingguchi/'+str(cal_date[index0]) + 'zhangtinggu.xlsx')
    else :
        print('无昨日涨停股数据')
        return
    code1 = dangri.code
    code2 = zuori.code
    name = dangri.code
    amount = dangri.amount
    for index1 in code1.index:
        for index2 in code2.index:
            
            if (int(code1[index1])==int(str(code2[index2]))):
               lianbangu = lianbangu.append([{'name':name[index1],'amount':amount[index1],'code':code1[index1],'flag':0}]) 
            
    
    lianbangu.to_excel('zhangtingguchi/'+str(lastjiaoyiri)  + 'lianbangu.xlsx',index=False)      
   #print(str(number1)+'-----'+str(round(avg_pct1/number1,2)))            
   #print(str(number2)+'-----'+str(round(avg_pct2/number2,2))) 
    return    

