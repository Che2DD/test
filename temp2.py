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






#将实时数据记录stock中


def shuangjiaojilu():
    
    df = pd.read_excel('stock.xlsx',index=False)
   
    df['shuangjiao'] = None
    shuangjiao_flag = df.shuangjiao
    
    symbo = df.symbol    
    isst = df.name
    
    for index in tscode.index:
        qwe = tscode[index]
        ldate = listdate[index] 
        name = symbo[index]
        
       
        if ( isst[index].find('ST') < 0  and str(symbo[index]).find('300') < 0 ):
            #print(str(qwe)+':::::::::'+str(ldate)+'------------'+str(index)+'------')
        
            
            if (os.path.isfile('shuju/'+str(qwe)+'.csv')):
                dff = pd.read_csv('shuju/'+str(qwe)+'.csv')
            price = dff.pct_chg
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
                             if ((number2+number4 >= 4 or number4 >=3)):
                                 shuangjiao_flag[index] = 1
                             
                             
    df.to_excel('stock.xlsx',index=False)
    return

def zhenfu(df,flag):
    
    #df = pd.read_excel('stock.xlsx')
    if (flag ==1 ):
       df['zhenfu30'] = None
       df['zhenfu60'] = None
       df['zhenfu250'] = None
       df['zhangfu5'] = None
       df['zhangfu9'] = None
    else :
        df = pd.read_excel('stock.xlsx',index=False)
    
    
    zhenfu30 = df.zhenfu30
    zhenfu60 = df.zhenfu60
    zhenfu250 = df.zhenfu250
    change60_5 = df.zhangfu5
    change60_9 = df.zhangfu9
    isst = df.name
    
    for index in tscode.index:
        tscod = tscode[index]
        
        if (isst[index].find('ST') < 0):
        
            
            print(str(tscod)+'----'+str(isst[index])+'----'+str(index))
            if (os.path.isfile(str(tscod)+'.csv')):
                dff = pd.read_csv(str(tscod)+'.csv')

                low = dff.low
                high = dff.high
                lastprice = dff.pre_close
                change = dff.pct_chg
                
                number = 0
                number2 = 0
                num30 = 0
                num60 = 0
                num250 = 0
                
                
                for index2 in low.index:
                    
                    if (index2 == low.size-1  and low.size-1 <30 ):
                        num30 = num30 /(low.size-1)
                        num60 = num60 /(low.size-1)
                        num250 = num250 /(low.size-1)
                        
                        zhenfu30[index] = num30 *100
                        zhenfu60[index] = num60 *100
                        zhenfu250[index] = num250 *100
                        change60_5[index] = number/index2*100
                        change60_9[index] = number2/index2*100
                        #print(str(num30)+'-----'+str(num60))
                        
                        break
                    
                    if (index2 == low.size-1  and low.size-1 >=30 and low.size-1 <=60):
                        num30 = num30 /30
                        num60 = num60 /(low.size-1)
                        num250 = num250 /(low.size-1)
                        
                        zhenfu30[index] = num30 *100
                        zhenfu60[index] = num60 *100
                        zhenfu250[index] = num250 *100
                        change60_5[index] = number/index2*100
                        change60_9[index] = number2/index2*100
                        
                        break
                    
                        
                    if (index2 == low.size-1  and low.size-1 >=60 ):
                        num30 = num30 /30
                        num60 = num60 /(low.size-1)
                        num250 = num250 /(low.size-1)
                        
                        zhenfu30[index] = num30 *100
                        zhenfu60[index] = num60 *100
                        zhenfu250[index] = num250 *100
                        change60_5[index] = number/index2*100
                        change60_9[index] = number2/index2*100
                        
                        break
                        
                    if (index2 == 250):
                         num30 = num30 /30
                         num60 = num60 /60
                         num250 = num250 /250
                         
                         zhenfu30[index] = num30 *100
                         zhenfu60[index] = num60 *100
                         zhenfu250[index] = num250 *100
                         change60_5[index] = number /index2*100
                         change60_9[index] = number2/index2*100
                         
                    if (index2 > 250):
                        break
                    if(lastprice[0]<=1):
                        break
                    
                    if (change[index2]>5 ):
                        number = number +1
                    
                    if(change[index2]>9):
                        number2 = number2 +1
                    
                    if(index2<=30):
                        num30 = num30 + ((high[index2]-low[index2])/lastprice[index2])
                        num60 = num60 + ((high[index2]-low[index2])/lastprice[index2])
                        num250 = num250 + ((high[index2]-low[index2])/lastprice[index2])
                       
                    elif(index2<=60):
                        num60 = num60 + ((high[index2]-low[index2])/lastprice[index2])
                        num250 = num250 + ((high[index2]-low[index2])/lastprice[index2])
                    else:
                        num250 = num250 + ((high[index2]-low[index2])/lastprice[index2])
                        
                
                
    df.to_excel('stock.xlsx',index=False)    
    
    return



#打印名字及个数   科创板暂未纳入


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('mode.chained_assignment', None)

ts.set_token('a3f5b59633004207469b9cf3a93191241b31bc9e47df07d422e0cc4c')
pro = ts.pro_api()

result =pd.DataFrame(columns=('tradedate','money','name','flag'))

zhangtinggu =pd.DataFrame(columns=('name','amount','code','flag'))
zhabangu =pd.DataFrame(columns=('name','amount','code'))

resulthuice =pd.DataFrame(columns=('tradedate','money','name','pch','high1','high2','high3','low1','low2','low3','open1','open2','open3','close1','close2','close3'))

shishistock =pd.DataFrame(columns=('code','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio','amount','per','pb','mktcap','nmc'))

shangzheng1 = ts.get_hist_data('sh',start='2019-01-05',end='2019-12-30')
date_sh = shangzheng1.index
i = str(date_sh[0])
lastjiaoyiri = i.replace("-","")
print(lastjiaoyiri)



df1 = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
df = pd.read_excel('stock.xlsx')

tscode = df.ts_code
tdcd = df1.ts_code
listdate = df.list_date
symbo = df.symbol

if (tdcd.size != tscode.size):
    df = df1
    print('stock')
    df.to_excel('stock.xlsx',index=False)
    #zhenfu(df,1)


print('当前小时：'+str(int(datetime.datetime.now().hour)))



today = time.strftime("%Y%m%d",time.localtime())

dff = pro.trade_cal(exchange='', start_date='20180101', end_date=today+'')
#dff.to_excel('sssssssssss.xlsx',index=False)
cal_date = dff.cal_date

index0 = dff.shape[0] - 1
print(cal_date[index0])
while (str(cal_date[index0])!=str(lastjiaoyiri)):
    index0 = index0 - 1

while (str(dff.is_open[index0])!= '1'):
        index0 = index0 - 1
index0 = index0 -1
#df = pd.read_excel('stock.xlsx')

#df.to_excel('stock.xlsx')
#  df=df.loc[df.list_status=='L']

#print(df.symbol)


#df = ts.get_today_ticks('002581')
#df = ts.get_tick_data('002581',date='2019-09-06',src='tt')
#print(df.tail(10))

#dff = ts.pro_bar(ts_code='000001.SZ', adj='qfq', adjfactor='True', start_date='20170101', end_date='20191230',ma=[5, 10, 20,30,60,120,250])
#dff.to_csv('000982.SZ.csv',index=False)


#df1 = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20000101', end_date='20191230')

#gengxin.shishijilu(df,1,lastjiaoyiri)
#zhishu.jinrizhangtinggu(df,)


#zhenfu(df,0)

#shuangjiaojilu()
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

'''

dff1 = pd.read_excel( 'zhangtinggu.xlsx',index=False)
date = dff1.date

zhangtinggu =pd.DataFrame(columns=('name','date','amount','flag'))
last = date[0]
zhongjian = None
flag = 0

for index in date.index:
    code = dff1.name
    amount = dff1.amount
    
    
    
    now = date[index]
    if (last == now):
        zhangtinggu = zhangtinggu.append([{'name':code[index],'date':date[index],'amount':amount[index],'flag':0}]) 
    else : 
        zhangtinggu.to_excel('zhangtingguchi/'+ str(last) + 'zhangtinggu.xlsx',index=False)
        
        zhangtinggu1 = pd.read_excel('zhangtingguchi/'+str(last) + 'zhangtinggu.xlsx')

        
        if (flag == 1):     
            lianbangu =pd.DataFrame(columns=('name','amount','code','times','flag'))
            zuori = pd.read_excel('zhangtingguchi/'+str(zhongjian) + 'zhangtinggu.xlsx')
            code1 = zhangtinggu1.name
            code2 = zuori.name
            name = zhangtinggu1.name
            amount2 = zhangtinggu1.amount
            amount1 = zuori.amount
            for index1 in code1.index:
                for index2 in code2.index:                  
                    if (str(code1[index1])==str(code2[index2])):
                       lianbangu = lianbangu.append([{'name':code2[index2],'amount':amount1[index2],'code':code1[index1],'flag':0}]) 
            
            
            if(lianbangu.shape[0]>=1):
                lianbangu.to_excel('zhangtingguchi/'+str(zhongjian)  + 'lianbangu.xlsx',index=False)  
            
        if (flag == 0):
            flag = 1
        
        zhongjian = last
        last = now
        zhangtinggu =pd.DataFrame(columns=('name','date','amount','flag'))
        zhangtinggu = zhangtinggu.append([{'name':code[index],'date':date[index],'amount':amount[index],'flag':0}]) 
        print(str(now))
       

'''




zhangtinggu =pd.DataFrame(columns=('name','date','amount','flag'))
zhabangu =pd.DataFrame(columns=('name','date','amount','flag'))
for index in tscode.index:
    qwe = tscode[index]    
    print(str(qwe)+'::::::::------------'+str(index)+'------')
    name = symbo[index]
    isst = df.name
    if ( isst[index].find('ST') < 0 ):
            
        if (os.path.isfile('shuju/'+str(qwe)+'-None.csv')):
             dff = pd.read_csv('shuju/'+str(qwe)+'-None.csv')
             code = dff.ts_code
             date = dff.trade_date
             close = dff.close
             pre_close = dff.pre_close
             amount = dff.amount
             high = dff.high
             if (dff.shape[0] < 15):
                 print('太短')
                 continue
             
             for index2 in date.index:
                 if (index2 >= dff.shape[0]-3):
                    
                     break
                               
                 
                 trade_price = Decimal(close[index2])
                 trade_price = trade_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                    
                 origin_num1 = Decimal(pre_close[index2])
                 shoupan_num = origin_num1.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                 
                 high_num = Decimal(high[index2])
                 high_num = high_num.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

                 if (panduanzhangting(str(trade_price),shoupan_num)):
                     #zhangtinggu = zhangtinggu.append([{'name':code[index2],'date':date[index2],'amount':amount[index2],'flag':0}])
                     continue
                     #print('---------'+str(code[index2]))
                 elif(panduanzhangting(str(high_num),shoupan_num)):
                        zhabangu = zhabangu.append([{'name':code[index2],'date':date[index2],'amount':amount[index2],'flag':0}])
zhabangu.to_excel( 'zhangtinggu.xlsx',index=False)








t = 0
while(t>0):
    if(t == 1000):
        gengxin.shishijilu(df,1,cal_date[index0])
        shuangjiaojilu()
        shuangjiao.dangriyuceshuangjiao(ts,df,result,1)
        t = t -1
    else :
        start = time.perf_counter()
        t = t -1  
        try:
            gengxin.shishijilu(df,0,cal_date[index0])  
        except BaseException:        
            print(' ')
        else:
            print(' ')
        shuangjiao.dangriyuceshuangjiao(ts,df,result,0)          
        end = time.perf_counter()   
        print('%.2f'%(end - start))
        ltime = '%.2f'%(end - start)
        if (float(ltime) < 90):
            time.sleep(90-float(ltime))
      


#shuangjiao.shuangjiaohuice(ts,df,resulthuice)
#gengxin.gengxinyiri(df)
#gengxin.gengxinshuju(ts,df,result)
#gengxin.gengxinshujuweifuquan(ts,df,result)





'''
#连续大涨
for index in tscode.index:
    qwe = tscode[index]
    if (os.path.isfile(str(qwe)+'.csv')):
            dff = pd.read_csv(str(qwe)+'.csv')
            price = dff.pct_chg
            tradedate = dff.trade_date
            money = dff.amount
        #print(tscode[index])
        #print(price)
            name = symbo[index]
            nam = df.name[index]
        #dff.to_csv(qwe+'111111111.csv')
        
            for index2 in price.index:
           # print(index2)
                if (index2 > len(price) - 5 or len(price) < 20 or len(price)-index2 < 15 or index2 > 160) :
                    break
                else : 
                    if (price[index2]+price[index2+1]+price[index2+2]+price[index2+3]+price[index2+4] > 48):
                        print(str(tradedate[index2])+'----------'+str(int((money[index2]+money[index2+1]+money[index2+2]+money[index2+3])/400000))+'-----'+str(nam))
                        #s = pd.Series([tradedate[index2], int((money[index2]+money[index2+1]+money[index2+2]+money[index2+3])/400000), nam])
                       
                        result = result.append([{'tradedate':tradedate[index2],'money':int((money[index2]+money[index2+1]+money[index2+2]+money[index2+3])/400000),'name':nam}], ignore_index=True)
                        
                    
    
result.to_excel('540.xlsx')   

'''





