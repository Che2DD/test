# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
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

dff = pro.trade_cal(exchange='', start_date='20000101', end_date=today+'')
dff.to_excel('sssssssssss.xlsx',index=False)
cal_date = dff.cal_date

index0 = dff.shape[0] - 1
print(str(cal_date[index0]))
while (str(cal_date[index0])!=str(lastjiaoyiri)):
    index0 = index0 - 1
index1 = index0 - 1
while (str(dff.is_open[index1])!= '1'):
    index1 = index1 - 1
lastlastjiaoyiri = cal_date[index1]


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
#zhishu.jinrizhangtinggu(df)

#zhenfu(df,0)
num = dff.shape[0] - 1

if (str(dff.is_open[num]) == '1' and int(datetime.datetime.now().hour) > 15 ):
    t = 25
    index10 = index1
    
    while(t >=0):
        while (str(dff.is_open[index10])!= '1'):
            index10 = index10 - 1
        index10 = index10 -1
        t= t -1
    df12 = pro.new_share(start_date=cal_date[index10], end_date=lastlastjiaoyiri)
    df12.to_excel('xingu.xlsx',index=False)
    print(cal_date[index10])





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



#dff12 = ts.pro_bar(ts_code='000039.SZ', adj='qfq', adjfactor='True', start_date='20060101', end_date='20191230',ma=[5, 10, 20,30,60,120,250])
#dff12.to_csv('shuju/000039.SZ.csv',index=False)



def shuangjiaoshuju():
    
    t = 1
    while(t>0):
        if(t == 2):
            
            gengxin.shishijilu(df,1,cal_date[index0])
            shuangjiaojilu()
            turn = shuangjiao.dangriyuceshuangjiao(ts,df,result,1)
            t = t -1
        else :
            start = time.perf_counter()
            t = t -1  
            try:
                gengxin.shishijilu(df,0,cal_date[index0]) 
                turn = shuangjiao.dangriyuceshuangjiao(ts,df,result,0) 
            except BaseException as e: 
                turn = '出现问题'
                print(e)
            else:
                #turn = '出现问题'
                print('')
                     
            end = time.perf_counter()   
            print('%.2f'%(end - start))
            ltime = '%.2f'%(end - start)
            if (float(ltime) < 2):
                time.sleep(15)
    return turn
      


#shuangjiao.shuangjiaohuice(ts,df,resulthuice)
#gengxin.gengxinyiri(df,lastjiaoyiri,lastlastjiaoyiri,pro)

#gengxin.gengxinyiri_yici(df,lastjiaoyiri,lastlastjiaoyiri,pro)

#gengxin.gengxinshuju(ts,df,result)
#gengxin.gengxinshujuweifuquan(ts,df,result)


ridadie_num = 0    
gengxin._ridadie(df,lastjiaoyiri,5,ridadie_num)
gengxin._ridadie(df,lastjiaoyiri,10,ridadie_num)
gengxin._ridadie(df,lastjiaoyiri,20,ridadie_num)
gengxin._ridadie(df,lastjiaoyiri,30,ridadie_num)
gengxin._ridadie(df,lastjiaoyiri,60,ridadie_num)
gengxin._ridadie(df,lastjiaoyiri,120,ridadie_num)
gengxin._ridadie(df,lastjiaoyiri,250,ridadie_num)


'''

gengxin.jinqidadie(df,5)
gengxin.jinqidadie(df,10)
gengxin.jinqidadie(df,20)
gengxin.jinqidadie(df,30)
gengxin.jinqidadie(df,60)
gengxin.jinqidadie(df,120)
gengxin.jinqidadie(df,250)
'''

#df13 = pro.daily(trade_date=lastjiaoyiri)
#df13.to_excel('zhangtingguchi/'+lastjiaoyiri+'.xlsx',index=False)  
#zhishu.selectzhangting(df,lastjiaoyiri)
#zhishu.selectlianban(df,lastjiaoyiri,lastlastjiaoyiri)

'''
a = zhishu.selectlianbanzhishu(df,lastjiaoyiri,lastlastjiaoyiri)

print(a)

a = zhishu.selectzhangtingzhishu(df,lastjiaoyiri,lastlastjiaoyiri)

print(a)

a = zhishu.selectzhabanzhishu(df,lastjiaoyiri,lastlastjiaoyiri)

print(a)

a = zhishu.pingjunzhangfu(lastjiaoyiri)

print(a)

'''

'''
t100 = 0
print(index0)
index100 = index0 -1926
d100 ={'20000101':'9999999'}
while(index100 <= 7194):
     while (str(dff.is_open[index100])!= '1'):
         index100 = index100 + 1
     d100[cal_date[index100]] = index0 - index100
     index100 = index100 + 1
'''






flag_d100 = 0
if (flag_d100 == 1):    
    d100 ={'000000.SH':'0.00'}
    d100_1 ={'000000.SH':'0.00'}
    d100_open ={'000000.SH':'0.00'}
    d100_1_open ={'000000.SH':'0.00'}
    t = 0
    print(index0)
    index1 = index0 -4600
    print(cal_date[index0])
    index0 = index1 + 1
    #zhishu =pd.DataFrame(columns=('shangzheng','chuangyeban','lianbanzhishu','zhabanzhishu','zhangtingzhishu','pingjunzhangfu'))
    
    zhishudata =pd.DataFrame(columns=('date','lianbanzhishu_open','lianbanzhishu','lianbanzhishu_num','zhangtingzhishu_open','zhangtingzhishu','zhangtingzhishu_num','zhabanzhishu','zhabanlv','pingjunzhangfu'))
    
    shangzheng50 =pd.read_excel('000016.SH.xlsx',index=False)
    zhongxiaoban =pd.read_excel('399005.SZ.xlsx',index=False)
    chuangyeban =pd.read_excel('399006.SZ.xlsx',index=False)
    
    
    
    while (str(dff.is_open[index1])!= '1'):
            index1 = index1 + 1
    if (os.path.isfile('zhangtingguchi/'+str(cal_date[index1])+'.xlsx')):
        data_1 = pd.read_excel('zhangtingguchi/'+str(cal_date[index1]) + '.xlsx')
    else:
        print(cal_date[index1])
    ts_code_data = data_1.ts_code  
    pct_chg_data = data_1.pct_chg
    open_data = data_1.open
    pre_close_data = data_1.pre_close
    for index in ts_code_data.index:
        d100_1[ts_code_data[index]] = pct_chg_data[index]
        d100_1_open[ts_code_data[index]] =round((open_data[index]-pre_close_data[index])/pre_close_data[index]*100,2)
    while(index0 <= dff.shape[0]-1):
         
         while (str(dff.is_open[index0])!= '1'):
            index0 = index0 + 1
         while (str(dff.is_open[index1])!= '1'):
            index1 = index1 + 1
         print(str(cal_date[index0])+'-------------------------------------------------')        
         lastjiaoyiri = cal_date[index0]
         lastlastjiaoyiri = cal_date[index1]
         
         if (os.path.isfile('zhangtingguchi/'+str(lastjiaoyiri)+'.xlsx')):
             data = pd.read_excel('zhangtingguchi/'+str(lastjiaoyiri) + '.xlsx')
         else:
             print(lastjiaoyiri)
         ts_code_data = data.ts_code  
         pct_chg_data = data.pct_chg
         open_data = data.open
         pre_close_data = data.pre_close
         for index in ts_code_data.index:
             d100[ts_code_data[index]] = pct_chg_data[index]
             d100_open[ts_code_data[index]] =round((open_data[index]-pre_close_data[index])/pre_close_data[index]*100,2)
         
         lianbanzhishu_zu = zhishu.selectlianbanzhishu(df,lastjiaoyiri,lastlastjiaoyiri,d100)
        
         zhabanzhishu_zu = zhishu.selectzhabanzhishu(df,lastjiaoyiri,lastlastjiaoyiri,d100,d100_1)
     
         lianbanzhishu_zu_open = zhishu.selectlianbanzhishu_open(df,lastjiaoyiri,lastlastjiaoyiri,d100_open)
         
         
         d100_1 = d100
         d100_1_open = d100_open
         
         zhangtingzhishu_zu = zhishu.selectzhangtingzhishu(df,lastjiaoyiri,lastlastjiaoyiri,d100)
         zhangtingzhishu_zu_open = zhishu.selectzhangtingzhishu_open(df,lastjiaoyiri,lastlastjiaoyiri,d100_open)
    
         pingjunzhangfu = zhishu.pingjunzhangfu(lastjiaoyiri)
         if (zhabanzhishu_zu == None or zhangtingzhishu_zu == None):
             zhabanlv = None
         else:
             zhabanlv = round(zhabanzhishu_zu[1]/(zhabanzhishu_zu[1]+zhangtingzhishu_zu[1]),2)
         
         if (lianbanzhishu_zu == None):
             lianbanzhishu = None
         else :
             lianbanzhishu = lianbanzhishu_zu[0]
             lianbanzhishu_num = lianbanzhishu_zu[1]
         if (lianbanzhishu_zu_open == None):
             lianbanzhishu_open = None
         else :
             lianbanzhishu_open = lianbanzhishu_zu_open[0]
         
         if (zhangtingzhishu_zu_open == None):
             zhangtingzhishu_open = None
         else :
             zhangtingzhishu_open = zhangtingzhishu_zu_open[0]
         
         if (zhangtingzhishu_zu == None):
             zhangtingzhishu = None
         else :
             zhangtingzhishu = zhangtingzhishu_zu[0]
             zhangtingzhishu_num = zhangtingzhishu_zu[1]
             
         if (zhabanzhishu_zu == None):
             zhabanzhishu = None
         else :
             zhabanzhishu = zhabanzhishu_zu[0]   
            
         zhishudata = zhishudata.append([{'date':lastjiaoyiri,'lianbanzhishu_open':lianbanzhishu_open,'lianbanzhishu':lianbanzhishu,'lianbanzhishu_num':lianbanzhishu_num,'zhangtingzhishu_open':zhangtingzhishu_open,'zhangtingzhishu':zhangtingzhishu,'zhangtingzhishu_num':zhangtingzhishu_num,'zhabanzhishu':zhabanzhishu,'zhabanlv':zhabanlv,'pingjunzhangfu':pingjunzhangfu}])
    
         index1 = index1 + 1
         index0 = index0 + 1
         zhishudata.to_excel('zhangtingguchi/zhishu.xlsx',index=False)







'''

t = 0
print(index0)
index1 = index0 -4927
print(cal_date[index0])

while(index0 <= 7230):
     
     while (str(dff.is_open[index1])!= '1'):
        index1 = index1 + 1
     
     index0 = index1 + 1
    
     while (str(dff.is_open[index0])!= '1'):
        index0 = index0 + 1
     zhishu.selectlianban(df,cal_date[index0],cal_date[index1])
     print(str(cal_date[index0])+'-------------------------------------------------')
     
     index1 = index1 + 1
'''

#获取该日股票数据及涨停炸板股
'''
t = 0

while (t < 4600):
    while (str(dff.is_open[index0])!= '1'):
        index0 = index0 - 1
    #if (os.path.isfile('zhangtingguchi/'+cal_date[index0]+'.xlsx')):
     #   break
    if (os.path.isfile('zhangtingguchi/'+cal_date[index0]+'.xlsx')):
        #d11111 = pd.read_excel('zhangtingguchi/'+str(cal_date[index0]) + '.xlsx')
        zhishu.selectzhangting(df,cal_date[index0])
    #df = pro.daily(trade_date=cal_date[index0])
    #df.to_excel('zhangtingguchi/'+cal_date[index0]+'.xlsx',index=False)
    print(str(cal_date[index0])+'------'+str(index0))
    index0 = index0 - 1
'''


#按日期列出各项指数及数据
'''
t = 0

while (t < 3000):
    while (str(dff.is_open[index0])!= '1'):
        index0 = index0 - 1
    #if (os.path.isfile('zhangtingguchi/'+cal_date[index0]+'.xlsx')):
     #   break
    if (os.path.isfile('zhangtingguchi/'+cal_date[index0]+'.xlsx')):
        #d11111 = pd.read_excel('zhangtingguchi/'+str(cal_date[index0]) + '.xlsx')
        zhishu.selectzhangtinggu(df,cal_date[index0])
    #df = pro.daily(trade_date=cal_date[index0])
    #df.to_excel('zhangtingguchi/'+cal_date[index0]+'.xlsx',index=False)
    print(str(cal_date[index0])+'------'+str(index0))
    index0 = index0 - 1

'''






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





