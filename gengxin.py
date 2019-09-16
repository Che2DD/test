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

def gengxinshuju(ts,df,result):
    tscode = df.ts_code

    listdate = df.list_date
    symbo = df.symbol
    isst = df.name
    
    for index in tscode.index:
        #if (int(symbo[index]) > 300463):
             qwe = tscode[index]
             ldate = listdate[index]
             print(str(qwe)+':::::::::'+str(ldate)+'------------'+str(index)+'------')
                
               
             name = symbo[index]
             dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20060101', end_date='20191230',ma=[5, 10, 20,30,60,120,250])
             dff.to_csv('shuju/'+qwe+'.csv',index=False)
    df1 = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20000101', end_date='20191230')
    df1.to_csv('shangzheng.csv',index=False)
    return

def gengxinshujuweifuquan(ts,df,result):
    tscode = df.ts_code

    listdate = df.list_date
    symbo = df.symbol
    isst = df.name
    
    for index in tscode.index:
        #if (int(symbo[index]) > 603506):
             qwe = tscode[index]
             ldate = listdate[index]
             print(str(qwe)+':::::::::'+str(ldate)+'------------'+str(index)+'------')
                
               
             name = symbo[index]
             dff = ts.pro_bar(ts_code=qwe+'', start_date='20060101', end_date='20191230',ma=[5, 10, 20,30,60,120,250])
             dff.to_csv('shuju/'+qwe+'-None.csv',index=False)
    return

def gengxinyiri(df,lastjiaoyiri,lastlastjiaoyiri,pro):
    tscode = df.ts_code
    #df_dangri =pd.DataFrame(columns=('ts_code','trade_date','open','high','low','close','pre_close','change','pct_chg','vol','amount','ma5','ma_v_5','ma10','ma_v_10','ma20','ma_v_20','ma30','ma_v_30','ma60','ma_v_60','ma120','ma_v_120','ma250','ma_v_250'))
    df1 = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20000101', end_date='20191230')
    trade_date = df1.trade_date
    #if (os.path.isfile('shuju/'+str(trade_date[0])+'.csv')):
       # df_dangri = pd.read_csv('shuju/'+str(trade_date[0])+'.csv')
    listdate = df.list_date
    symbo = df.symbol
    isst = df.name
    
    for index in tscode.index:
        #2826
        ldate = listdate[index]
        if (int(symbo[index]) >= 0 ):
            qwe = tscode[index]
            ldate = listdate[index]
            
            print(str(qwe)+':::::::::'+str(lastjiaoyiri)+'-----'+str(ldate)+'-------'+str(index)+'------')                  
            name = symbo[index]
            #dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20080101', end_date='20191230',ma=[5, 10, 20,30,60,120,250])                
            dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date=lastjiaoyiri, end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])    
            if (dff.empty):
                continue
            
            
            ##print(dff)
            dff_None = dff.drop(columns=['adj_factor'])
           
            #dff_None = pro.daily(ts_code=qwe+'', start_date='20190904', end_date='20190904')
            if (os.path.isfile('shuju/'+str(qwe)+'.csv')):
                dff1 = pd.read_csv('shuju/'+qwe+'.csv')
                dff_None1 = pd.read_csv('shuju/'+qwe+'-None.csv')
            else :
                dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff.to_csv('shuju/'+qwe+'.csv',index=False)
                dff_None = ts.pro_bar(ts_code=qwe+'',  start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff_None.to_csv('shuju/'+qwe+'-None.csv',index=False)
                continue
            
            if (dff.empty == True ):
                    continue
            trade_date = dff.trade_date
            trade_date1 = dff1.trade_date
            
            if(int(trade_date[0]) <= int(trade_date1[0]) ):
                continue
            
            #df_dangri = df_dangri.append(dff_None)
            
            adjfactor = dff.adj_factor
            adjfactor1 = dff1.adj_factor
            
            mid = round(adjfactor1[0],3)
            
            if (str(adjfactor[0]) != str(mid) ):
                dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff.to_csv('shuju/'+qwe+'.csv',index=False)
                dff_None = ts.pro_bar(ts_code=qwe+'',  start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff_None.to_csv('shuju/'+qwe+'-None.csv',index=False)
                with open('a.txt', mode='a') as filename:
                    filename.write('adjfactor1'+str(qwe)+'------'+str(adjfactor[0])+'-------'+str(mid))
                    filename.write('\n')
                continue
            if (dff1.shape[0] == 4 or dff1.shape[0] ==9 or dff1.shape[0] ==19 or dff1.shape[0] ==29 or dff1.shape[0] ==59 or dff1.shape[0] ==119 or dff1.shape[0] ==249):    
                dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff.to_csv('shuju/'+qwe+'.csv',index=False)
                dff_None = ts.pro_bar(ts_code=qwe+'',  start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff_None.to_csv('shuju/'+qwe+'-None.csv',index=False)
                with open('a.txt', mode='a') as filename:
                    filename.write('rixian'+str(qwe))
                    filename.write('\n')
                continue
            else :
                ma5 = dff1.ma5
                ma10 = dff1.ma10
                ma20 = dff1.ma20
                ma30 = dff1.ma30
                ma60 = dff1.ma60
                ma120 = dff1.ma120
                ma250 = dff1.ma250
                
                ma_v_5 = dff1.ma_v_5
                ma_v_10 = dff1.ma_v_10
                ma_v_20 = dff1.ma_v_20
                ma_v_30 = dff1.ma_v_30
                ma_v_60 = dff1.ma_v_60
                ma_v_120 = dff1.ma_v_120
                ma_v_250 = dff1.ma_v_250
                               
                n_ma5 = dff.ma5
                n_ma10 = dff.ma10
                n_ma20 = dff.ma20
                n_ma30 = dff.ma30
                n_ma60 = dff.ma60
                n_ma120 = dff.ma120
                n_ma250 = dff.ma250
                            
                n_ma_v_5 = dff.ma_v_5
                n_ma_v_10 = dff.ma_v_10
                n_ma_v_20 = dff.ma_v_20
                n_ma_v_30 = dff.ma_v_30
                n_ma_v_60 = dff.ma_v_60
                n_ma_v_120 = dff.ma_v_120
                n_ma_v_250 = dff.ma_v_250
                                
              
                    #print(dff)
                
                n_close = dff.close
                n_vol = dff.vol
                
                sda = dff1.iloc[:,5]
                sds = dff1.iloc[:,9]
                
                
                
                if(dff1.shape[0] > 4):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 3):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma5[0] = round((total_n + n_close[0])/5,4)
                    n_ma_v_5[0] = (total_v + n_vol[0])/5
                                       
                if(dff1.shape[0] > 9):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 8):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma10[0] = round((total_n + n_close[0])/10,4)
                    n_ma_v_10[0] = (total_v + n_vol[0])/10
                    
                if(dff1.shape[0] > 19):
                    
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 18):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma20[0] = round((total_n + n_close[0])/20,4)
                    n_ma_v_20[0] = (total_v + n_vol[0])/20
                    
                if(dff1.shape[0] > 29):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 28):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma30[0] = round((total_n + n_close[0])/30,4)
                    n_ma_v_30[0] = (total_v + n_vol[0])/30
                    
                    
                if(dff1.shape[0] > 59):
                    
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 58):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma60[0] = round((total_n + n_close[0])/60,4)
                    n_ma_v_60[0] = (total_v + n_vol[0])/60
                    
                if(dff1.shape[0] > 119):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 118):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma120[0] = round((total_n + n_close[0])/120,4)
                    n_ma_v_120[0] = (total_v + n_vol[0])/120
                if(dff1.shape[0] > 249):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 248):
                        total_n = total_n + sda[num]
                        total_v = total_v = sds[num]
                        num = num + 1
                    n_ma250[0] = round((total_n + n_close[0])/250,4)
                    n_ma_v_250[0] = (total_v + n_vol[0])/250
                dff_None = (dff.drop(columns=['adj_factor'])).append(dff_None1)
                dff = dff.append(dff1)
                #df_dangri.to_csv('shuju/'+str(trade_date[0])+'d.csv',index=False)
                
            dff.to_csv('shuju/'+qwe+'.csv',index=False)
            dff_None.to_csv('shuju/'+qwe+'-None.csv',index=False)
    #zhenfu(df,0)
    #shishijilu(df,1)
    #shuangjiaojilu()
    df1 = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20000101', end_date=lastjiaoyiri)
    
    df1.to_csv('shangzheng.csv',index=False)
    
    df13 = pro.daily(trade_date=lastjiaoyiri)
    df13.to_excel('zhangtingguchi/'+lastjiaoyiri+'.xlsx',index=False)  
    zhishu.selectzhangtinggu(df,lastjiaoyiri)
    zhishu.selectlianban(df,lastjiaoyiri,lastlastjiaoyiri)
    
    return



def shishijilu(df,flag,lastjiaoyiri):
    
    
    if (int(datetime.datetime.now().hour) > 16):
        if (os.path.isfile(str(lastjiaoyiri)+'.xlsx')):
            asssd = pd.read_excel(lastjiaoyiri+'.xlsx',index=False)
            print('无须再次更新')
        else:
            asssd = ts.get_today_all()    
            asssd.to_excel(lastjiaoyiri+'.xlsx',index=False)
    else :
        asssd = ts.get_today_all() 
        asssd.to_excel('asssd.xlsx',index=False)
        print('获得实时数据')
    
    #asssd = pd.read_excel('asssd.xlsx',index=False)
   
    if (flag ==1 ):
        df['open'] = None
        df['trade'] = None
    else :
        df = pd.read_excel('stock.xlsx',index=False)
        
    changepercent = asssd.changepercent
        
    openop = df.open
    openp = asssd.open
    tradeop = df.trade
    tradep = asssd.trade
    #print(df)
    code1 = asssd.code
    name1 = asssd.name
    d ={'000000':'None'}
    tscode = df.ts_code
    
    
    for index in openp.index:
       
       # if(changepercent[index]<5):
        #    continue
        #print('111111')
        
        
        
        d[int(code1[index])] = asssd.iloc[index]
         
    for index2 in tscode.index:
        code2 = df.symbol
        name2 = df.name
        if int(code2[index2]) in d:
            asd = d[int(code2[index2])]
                                     
            openop[index2] = asd[4]
            tradeop[index2] = asd[3]
                       
    df.to_excel('stock.xlsx',index=False)

    
    return d