# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

def shuangjiaohuice(ts,df,resulthuice):
    
    resulthuice =pd.DataFrame(columns=('tradedate','money','name','pch','high1','high2','high3','low1','low2','low3','open1','open2','open3','close1','close2','close3'))

    
    tscode = df.ts_code
    listdate = df.list_date
    symbo = df.symbol   
    isst = df.name
    for index in tscode.index:
        qwe = tscode[index]
        ldate = listdate[index]       
       # print(str(qwe)+':::::::::'+str(ldate)+'------------'+str(index)+'------')
        name = symbo[index]
        
        if ( isst[index].find('ST') < 0 ):
            
            if (os.path.isfile('shuju/'+str(qwe)+'.csv')):
                dff = pd.read_csv('shuju/'+str(qwe)+'.csv')
                price = dff.pct_chg
                tradedate = dff.trade_date
                money = dff.amount
                openp = dff.open
                closep = dff.close 
                ma5 = dff.ma5
                ma10 = dff.ma10
                ma20 = dff.ma20
                ma30 = dff.ma30
                ma60 = dff.ma60
                ma120 = dff.ma120
                ma250 = dff.ma250
                mav5 = dff.ma_v_5
                high = dff.high
                low = dff.low
                           
                times = 0    
                times2 = 0
                first = 0
     
                for index2 in price.index:                
                    number = 0
                    number2 = 0
                    if(index2 <= 3):
                        continue
                    if(index2 >= price.size-3):
                        break
                    if (int(price[index2]) < 5 or abs(ma5[index2+2]-closep[index2])/closep[index2] > 0.05) :
                        continue
                    if ( price[index2] == 0 or (ma250[index2] >0 and (ma250[index2]-price[index2])/price[index2] < 0)):
                    
                        continue
                                   
                    if (ma5[index2]>openp[index2]*0.99 and ma5[index2] <closep[index2] ) :
                        number = number + 1
                    if (ma10[index2]>openp[index2]*0.99 and ma10[index2]<closep[index2] ) :
                        number2 = number2 + 1
                    if (ma20[index2]>openp[index2]*0.99 and ma20[index2]<closep[index2] ) :
                        number2 = number2 + 1
                    if (ma30[index2]>openp[index2]*0.99 and ma30[index2]<closep[index2] ) :
                        number2 = number2 + 1
                    if (ma60[index2]>openp[index2]*0.99 and ma60[index2]<closep[index2] ) :
                        number = number + 1
                    if (ma120[index2]>openp[index2]*0.99 and ma120[index2]<closep[index2] ) :
                        number = number + 1
                    if (number+number2 >= 4 or number2>=3 ): 
                        #print(str(number)+'---------'+str(name)+'-----'+str(tradedate[index2]))
                        
                        if(first == 0):
                            first = index2
                            continue
                                                                  
                        if (abs(index2 - first) <=30  and (times+times2 + number+number2 >= 8 or number2 + times2 >=6)and abs(openp[index2]-openp[first])/openp[index2] < 0.20 ):
                            
                            
                            
                            high1 =  int((high[first-1] - closep[first])/closep[first]*1000)/10
                            high2 =  int((max(high[first-1],high[first-2])  - closep[first])/closep[first] *1000    )   /10               
                            high3 = int(( max(high[first-1],high[first-2],high[first-3]) - closep[first])/closep[first]*1000)/10
                            
                            low1 = int( (low[first-1]- closep[first])/closep[first]*1000)/10
                            low2 =  int((min(low[first-1],low[first-2])  - closep[first])/closep[first]   *1000       )      /10       
                            low3 =  int((min(low[first-1],low[first-2],low[first-3])- closep[first])/closep[first]*1000)/10
                            
                            open1 = int((openp[first-1]-closep[first])/closep[first]*1000) /10
                            open2 = int((openp[first-2]-closep[first])/closep[first]*1000) /10
                            open3 = int((openp[first-3]-closep[first])/closep[first]*1000) /10
                            
                            close1 = int((closep[first-1]-closep[first])/closep[first]*1000) /10
                            close2 = int((closep[first-2]-closep[first])/closep[first]*1000) /10
                            close3 = int((closep[first-3]-closep[first])/closep[first]*1000) /10
                            
                            pch1 = price[first]
                            
                            #if (high3<4 or low3 >15 or (high3 != 0 and low3/high3 > 1.5 )):
                            #    continue
                            #if (money[first] > 30000 and mav5[first]*ma5[first] > 20000 ):
                               # if (money[first]*10 < mav5[first]*ma5[first]):
                                    
                            print(str(tradedate[index2])+'---------'+str(name)+'-----'+str(tradedate[first])+'----'+str(high3)+'----'+str(low3))
                            resulthuice = resulthuice.append([{'tradedate':tradedate[first],'money':money[index2],'name':name,'pch':pch1,'high1':high1,'high2':high2,'high3':high3,'low1':low1,'low2':low2,'low3':low3,'open1':open1,'open2':open2,'open3':open3,'close1':close1,'close2':close2,'close3':close3}], ignore_index=True)
                            #print(str(low[first-1])+"-----"+str(closep[first]))                 
                        times = number
                        times2 = number2
                        first = index2
                                 
    resulthuice.to_csv('shuangjiaohuice.csv',index=False)
    
    return




#µ±ÈÕÔ¤²âË«½¿
def dangriyuceshuangjiao(ts,df,result,flag):
    df = pd.read_excel('stock.xlsx',index=False)
    tscode = df.ts_code
    listdate = df.list_date
    symbo = df.symbol    
    isst = df.name
    openpp = df.open
    tradedd = df.trade
    if (flag == 0):
        shuangjiao_flag = df.shuangjiao
    asd = 0
    zxc = 0
    
    numb_low = 0
    
    
    for index in tscode.index:
        qwe = tscode[index]
        ldate = listdate[index] 
        name = symbo[index]
        
        
        
        if ( isst[index].find('ST') < 0  and str(symbo[index]).find('300') < 0 and (flag == 1 or shuangjiao_flag[index] == 1)):
            #print(str(qwe)+':::::::::'+str(ldate)+'------------'+str(index)+'------')
        
            
            if (os.path.isfile('shuju/'+str(qwe)+'.csv')):
                dff = pd.read_csv('shuju/'+str(qwe)+'.csv')
                price = dff.pct_chg
                tradedate = dff.trade_date
                money = dff.amount
                openp = dff.open
                closep = dff.close 
                
                ma5 = dff.ma5
                ma10 = dff.ma10
                ma20 = dff.ma20
                ma30 = dff.ma30
                ma60 = dff.ma60
                ma120 = dff.ma120
                ma250 = dff.ma250        
                mav5 = dff.ma_v_5        
                first = 0
     
                #for index2 in price.index:
                index2 = 0              
                number1 = 0              
                number3 = 0
                
                
                #ÅÌÇ°¡¢ÅÌºó
                """
                if (dff.empty == True ):
                    continue
                open1 = openp[index2]*0.99
                close1 = closep[index2]
                ma55= ma5[index2]
                ma1010 =ma10[index2]
                """
                #
                #ÅÌÖÐ
                '''
                if (dff.empty == True or tradedd[index] == np.nan):
                    zxc = zxc +1
                    print('000')
                    continue
                '''
                
                open1 = openpp[index]*0.99               
                #close1 = closep[index2]*1.05
                close1 = tradedd[index]          
                ma55= ma5[index2]*1.008
                ma1010 =ma10[index2]*1.005 
                
                if((close1-closep[index2])/closep[index2] < 0.05):
                    numb_low = numb_low +1
                    continue
                
                #if ( open1 == 0 or (ma250[index2] >0 and (ma250[index2]-open1)/open1 < 0)):
                    #print(str(ma250[index2])+'-----'+str(open1)+'-----'+str(qwe))
                    #continue
                
                
                if (ma55>open1 and ma5[index2] <close1 ) :
                    number1 = number1 + 1
                if (ma1010>open1 and ma10[index2]<close1 ) :
                    number3 = number3 + 1
                if (ma20[index2]>open1 and ma20[index2]<close1 ) :
                    number3 = number3 + 1
                if (ma30[index2]>open1 and ma30[index2]<close1 ) :
                    number3 = number3 + 1
                if (ma60[index2]>open1 and ma60[index2]<close1 ) :
                    number1 = number1 + 1
                if (ma120[index2]>open1 and ma120[index2]<close1 ) :
                    number1 = number1 + 1
                if (number1+number3 >= 4 or number3>=3 ):
                    
                     if(shuangjiao_flag[index] == 1):
                        print(str(name))
                        continue
                    
                    
                     for index3 in price.index:
                         
                        
                         number2 = 0
                         number4 = 0
                         if(index3 == 0  ):
                             continue
                         
                         if(index3>= 30):
                             break
                         if (price[index3] < 5) :
                             continue 
                         
                         if (ma5[index3]>openp[index3] and ma5[index3] <closep[index3] ) :
                             number2 = number2 + 1
                         if (ma10[index3]>openp[index3] and ma10[index3]<closep[index3] ) :
                             number4 = number4 + 1
                         if (ma20[index3]>openp[index3] and ma20[index3]<closep[index3] ) :
                             number4 = number4 + 1
                         if (ma30[index3]>openp[index3] and ma30[index3]<closep[index3] ) :
                             number4 = number4 + 1
                         if (ma60[index3]>openp[index3] and ma60[index3]<closep[index3] ) :
                             number2 = number2 + 1
                         if (ma120[index3]>openp[index3] and ma120[index3]<closep[index3] ) :
                             number2 = number2 + 1
                         if ((number2+number1+number3+number4 >= 8 and number2+number4 >=4)or number3 + number4 >=6  and abs(openp[index3]-openp[index2])/openp[index2] < 0.20):
                        #print(str(number)+'---------'+str(name)+'-----'+str(tradedate[index2]))
                                                                                                             
                             #if (money[index3] > 30000 and mav5[index3]*ma5[index3] > 20000 ):
                                 print(str(tradedate[index3])+'---------'+str(name)+'-----'+str(number1+number3)+'----'+str(number2+number4))
                                 
                                 result = result.append([{'tradedate':tradedate[index3],'money':money[index3],'name':name}], ignore_index=True)
                                              
                            
                           
    print('双娇结束'+ '-----'+str(numb_low))        
    result.to_csv('yuceshuangjiao.csv',index=False)
    #print(zxc)
    return

