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
        if (int(symbo[index]) >= 0):
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
        if (int(symbo[index]) >= 0):
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
        if (int(symbo[index]) >= 2542 ):
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
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma5[0] = round((total_n + n_close[0])/5,4)
                    n_ma_v_5[0] = (total_v + n_vol[0])/5
                                       
                if(dff1.shape[0] > 9):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 8):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma10[0] = round((total_n + n_close[0])/10,4)
                    n_ma_v_10[0] = (total_v + n_vol[0])/10
                    
                if(dff1.shape[0] > 19):
                    
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 18):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma20[0] = round((total_n + n_close[0])/20,4)
                    n_ma_v_20[0] = (total_v + n_vol[0])/20
                    
                if(dff1.shape[0] > 29):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 28):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma30[0] = round((total_n + n_close[0])/30,4)
                    n_ma_v_30[0] = (total_v + n_vol[0])/30
                    
                    
                if(dff1.shape[0] > 59):
                    
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 58):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma60[0] = round((total_n + n_close[0])/60,4)
                    n_ma_v_60[0] = (total_v + n_vol[0])/60
                    
                if(dff1.shape[0] > 119):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 118):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma120[0] = round((total_n + n_close[0])/120,4)
                    n_ma_v_120[0] = (total_v + n_vol[0])/120
                if(dff1.shape[0] > 249):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 248):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
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






def gengxinyiri_yici(df,lastjiaoyiri,lastlastjiaoyiri,pro):
    
    
    
    df13 = pro.daily(trade_date=lastjiaoyiri)
    df13.to_excel('zhangtingguchi/'+lastjiaoyiri+'.xlsx',index=False)  
    ts_code = df13.ts_code
    
    dizhi = 'shuju/'

    for index in ts_code.index:
        df_dangri =pd.DataFrame(columns=('ts_code','trade_date','open','high','low','close','pre_close','change','pct_chg','vol','amount','adj_factor','ma5','ma_v_5','ma10','ma_v_10','ma20','ma_v_20','ma30','ma_v_30','ma60','ma_v_60','ma120','ma_v_120','ma250','ma_v_250'))
        
        qwe = ts_code[index]
        print(qwe)
        if (int(ts_code[index][:-3]) >= 0 ):
            if (os.path.isfile(dizhi+str(ts_code[index])+'.csv')):
                dff1 = pd.read_csv(dizhi+ts_code[index]+'.csv',engine='python')
                dff_None1 = pd.read_csv(dizhi+ts_code[index]+'-None.csv',engine='python')
            else :
                dff = ts.pro_bar(ts_code=ts_code[index]+'', adj='qfq', adjfactor='True', start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff.to_csv(dizhi+ts_code[index]+'.csv',index=False)
                dff_None = ts.pro_bar(ts_code=ts_code[index]+'',  start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff_None.to_csv(dizhi+ts_code[index]+'-None.csv',index=False)
                continue

            
            trade_date = df13.trade_date
            trade_date1 = dff1.trade_date
            
            if(int(trade_date[index]) <= int(trade_date1[0]) ):
                continue
            
            pre_close = df13.pre_close
            close1 = dff1.close
            
            mid1 = round(pre_close[index],2)
            mid2 = round(close1[0],2)
            if (str(mid1) != str(mid2) ):
                
                dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff.to_csv(dizhi+qwe+'.csv',index=False)
                dff_None = ts.pro_bar(ts_code=qwe+'',  start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff_None.to_csv(dizhi+qwe+'-None.csv',index=False)
                with open('a.txt', mode='a') as filename:
                    filename.write('adjfactor1----'+str(mid1)+'-----'+str(mid2)+'-----'+str(qwe)+'------复权')
                    filename.write('\n')
                   
                continue
            if (dff1.shape[0] == 4 or dff1.shape[0] ==9 or dff1.shape[0] ==19 or dff1.shape[0] ==29 or dff1.shape[0] ==59 or dff1.shape[0] ==119 or dff1.shape[0] ==249):    
                
                dff = ts.pro_bar(ts_code=qwe+'', adj='qfq', adjfactor='True', start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff.to_csv(dizhi+qwe+'.csv',index=False)
                dff_None = ts.pro_bar(ts_code=qwe+'',  start_date='20060101', end_date=lastjiaoyiri,ma=[5, 10, 20,30,60,120,250])
                dff_None.to_csv(dizhi+qwe+'-None.csv',index=False)
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
                   
                
                
                n_ma5 = None
                n_ma10 = None
                n_ma20 = None
                n_ma30 = None
                n_ma60 = None
                n_ma120 = None
                n_ma250 = None
                            
                n_ma_v_5 = None
                n_ma_v_10 = None
                n_ma_v_20 = None
                n_ma_v_30 = None
                n_ma_v_60 = None
                n_ma_v_120 = None
                n_ma_v_250 = None
                
                
                sda = dff1.iloc[:,5]
                sds = dff1.iloc[:,9]
                
                
                
                
                
                
                n_close = df13.close
                n_vol = df13.vol
                
                if(dff1.shape[0] > 4):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 3):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma5 = round((total_n + n_close[index])/5,4)
                    n_ma_v_5 = (total_v + n_vol[index])/5
                                       
                if(dff1.shape[0] > 9):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 8):
                        total_n = total_n + sda[num]
                        total_v = total_v +sds[num]
                        num = num + 1
                    n_ma10 = round((total_n + n_close[index])/10,4)
                    n_ma_v_10 = (total_v + n_vol[index])/10
                    
                if(dff1.shape[0] > 19):
                    
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 18):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma20 = round((total_n + n_close[index])/20,4)
                    n_ma_v_20 = (total_v + n_vol[index])/20
                    
                if(dff1.shape[0] > 29):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 28):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma30 = round((total_n + n_close[index])/30,4)
                    n_ma_v_30 = (total_v + n_vol[index])/30
                    
                    
                if(dff1.shape[0] > 59):
                    
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 58):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma60 = round((total_n + n_close[index])/60,4)
                    n_ma_v_60 = (total_v + n_vol[index])/60
                    
                if(dff1.shape[0] > 119):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 118):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma120 = round((total_n + n_close[index])/120,4)
                    n_ma_v_120 = (total_v + n_vol[index])/120
                if(dff1.shape[0] > 249):
                    num = 0
                    total_n = 0
                    total_v = 0
                    while(num <= 248):
                        total_n = total_n + sda[num]
                        total_v = total_v + sds[num]
                        num = num + 1
                    n_ma250 = round((total_n + n_close[index])/250,4)
                    n_ma_v_250 = (total_v + n_vol[index])/250
                
                df_dangri = df_dangri.append([{'ts_code':qwe,'trade_date':df13.trade_date[index],'open':df13.open[index],'high':df13.high[index],'low':df13.low[index],'close':df13.close[index],'pre_close':df13.pre_close[index],'change':df13.change[index],'pct_chg':df13.pct_chg[index],'vol':df13.vol[index],'amount':df13.amount[index],'adj_factor':dff1.adj_factor[0],'ma5':n_ma5,'ma_v_5':n_ma_v_5,'ma10':n_ma10,'ma_v_10':n_ma_v_10,'ma20':n_ma20,'ma_v_20':n_ma_v_20,'ma30':n_ma30,'ma_v_30':n_ma_v_30,'ma60':n_ma60,'ma_v_60':n_ma_v_60,'ma120':n_ma120,'ma_v_120':n_ma_v_120,'ma250':n_ma250,'ma_v_250':n_ma_v_250}])
                df_dangri_None = df_dangri.drop(columns=['adj_factor'])
                
                #dff1.loc[0]=[qwe,df13.trade_date[index],df13.open[index],df13.high[index],df13.low[index],df13.close[index],df13.pre_close[index],df13.change[index],df13.pct_chg[index],df13.vol[index],df13.amount[index],dff1.adj_factor[0],n_ma5,n_ma_v_5,n_ma10,n_ma_v_10,n_ma20,n_ma_v_20,n_ma30,n_ma_v_30,n_ma60,n_ma_v_60,n_ma120,n_ma_v_120,n_ma250,n_ma_v_250]
                #dff_None1.loc[0]=[qwe,df13.trade_date[index],df13.open[index],df13.high[index],df13.low[index],df13.close[index],df13.pre_close[index],df13.change[index],df13.pct_chg[index],df13.vol[index],df13.amount[index],n_ma5,n_ma_v_5,n_ma10,n_ma_v_10,n_ma20,n_ma_v_20,n_ma30,n_ma_v_30,n_ma60,n_ma_v_60,n_ma120,n_ma_v_120,n_ma250,n_ma_v_250]
                
                dff_None1 = df_dangri_None.append(dff_None1)
                dff1 = df_dangri.append(dff1)
                
                dff1.to_csv(dizhi+qwe+'.csv',index=False)
                dff_None1.to_csv(dizhi+qwe+'-None.csv',index=False)
                
                
                
                
                


    #zhenfu(df,0)
    #shishijilu(df,1)
    #shuangjiaojilu()
   
    
    df13 = pro.daily(trade_date=lastjiaoyiri)
    df13.to_excel('zhangtingguchi/'+lastjiaoyiri+'.xlsx',index=False)  
    zhishu.selectzhangting(df,lastjiaoyiri)
    zhishu.selectlianban(df,lastjiaoyiri,lastlastjiaoyiri)
    
    
    dd = '399006.SZ'
    dff = pro.index_daily(ts_code=dd)
    dff.to_excel(dd+'.xlsx',index=False)
    
    dd = '399005.SZ'
    dff = pro.index_daily(ts_code=dd)
    dff.to_excel(dd+'.xlsx',index=False)
    
    dd = '000001.SH'
    dff = pro.index_daily(ts_code=dd)
    dff.to_excel(dd+'.xlsx',index=False)
    
    dddd = '000016.SH'
    dff = pro.index_daily(ts_code=dddd)
    dff.to_excel(dddd+'.xlsx',index=False)
    
    dd = '399678.SZ'
    dff = pro.index_daily(ts_code=dd)
    dff.to_excel(dd+'.xlsx',index=False)
    
    
    return

def jinqidadie(df,num_times):
    result =pd.DataFrame(columns=('tradedate','money','name','flag'))

    tscode = df.ts_code
    symbo = df.symbol
    for index in tscode.index:
        qwe = tscode[index]
        nam = df.name
        if (os.path.isfile('shuju/'+str(qwe)+'.csv')and (nam[index].find('ST') < 0)):
                dff = pd.read_csv('shuju/'+str(qwe)+'.csv')
                price = dff.pct_chg
                tradedate = dff.trade_date
                money = dff.amount
            #print(tscode[index])
            #print(price)
                name = symbo[index]
                nam = df.name[index]
            #dff.to_csv(qwe+'111111111.csv')
                nums = []
                for index2 in price.index:
               # print(index2)                                                          
                    if (index2 > num_times):
                        break
                    nums.append(price[index2])
                  
                sum1 = 0
                num_sum = 1
                num_max = 100 
                minSum = nums[0]
                maxSum = 0
                num_result = 1
                
                num_index = 0
                '''
                for num in nums:
                    sum1 += num
                    num_sum = num_sum*(1+num/100)
                    if sum1 - maxSum < minSum :
                        minSum = sum1 - maxSum
                        num_result = num_sum / num_max
                    if sum1 > maxSum:
                        maxSum = sum1  
                        num_max = num_sum
                        num_index = nums.index(num)
                 '''
                for num in nums:
                     sum1=sum1+num
                     num_sum = num_sum*(1+num/100)
                     if(minSum>sum1):
                       minSum=sum1;
                       num_result = num_sum
                       num_index = nums.index(num)
                     if(sum1>0):
                       sum1=0
                       num_sum = 1
                       
                 
                    
                result = result.append([{'tradedate':tradedate[num_index],'money':round((num_result-1)*100,1),'name':nam}], ignore_index=True)
    
    result.to_excel(str(num_times)+'diefu.xlsx', index=False)             
                        
    
      
    
    
    return
def _ridadie(df,lastjiaoyiri,times,begin):
    result1 =pd.DataFrame(columns=('tradedate','money','name','flag','len','code'))
    result2 =pd.DataFrame(columns=('tradedate','money','name','flag','len','code'))

    tscode = df.ts_code
    symbo = df.symbol
    
    for index in tscode.index:
        qwe = tscode[index]
        nam = df.name
        if ((os.path.isfile('shuju/'+str(qwe)+'.csv') )and (nam[index].find('ST') < 0)):
                dff = pd.read_csv('shuju/'+str(qwe)+'.csv')
                price = dff.pct_chg
                tradedate = dff.trade_date
                money = dff.amount
            #print(tscode[index])
            #print(price)
                name = symbo[index]
                
            #dff.to_csv(qwe+'111111111.csv')
                nums = []
                
                '''
                len1 = begin + times
                
                index2 = 1
                while(index2 <= len1 and index <=dff.shape[0]-1):
               # print(index2)                                                          
                    
                    nums.append(price[index2])
                    index2 = index2 + 1
                '''
                
                if (dff.shape[0] <= begin):
                    
                
                    
                    continue
                
                
                
                for index2 in price.index:
                    
                    
                    if (index2 < begin):
                        continue
                    
               # print(index2)                                                          
                    if (index2 >= times+begin):
                        break
                    nums.append(price[index2])
                    
                weizhi = str(round(price[0],2))
                minSum = (100+price[0])/100
                maxSum = (100+price[0])/100
                

                Sum =(nums[0]+100)/100
                
                weizhi = str(nums[0])
                weizhi1 = str(nums[0])
                weizhi2 = str(nums[0])
                
                i = 0
                
                for num in nums:
                     
                     if (i == 0):
                         i = 1
                         continue
                        
                     Sum = Sum * (100+num)/100
                     weizhi = weizhi + '|'+str(round(num,2))
                     if (Sum  < minSum):
                         minSum = round(Sum,4) 
                         weizhi1 = weizhi
                     if (Sum > maxSum):
                         maxSum = round(Sum,4) 
                         weizhi2 = weizhi
                    
                
                result1 = result1.append([{'tradedate':weizhi1,'money':round((minSum-1)*100,1),'name':nam[index],'flag':0,'len':dff.shape[0],'code':name}], ignore_index=True)
                result2 = result2.append([{'tradedate':weizhi2,'money':round((maxSum-1)*100,1),'name':nam[index],'flag':0,'len':dff.shape[0],'code':name}], ignore_index=True)
    result1_new = result1.sort_values('money')
    result1_new = result1_new.reset_index(drop=True)
    result1_new = result1_new.loc[(result1_new["len"] <=220+begin) & (result1_new["code"]<=688000)]
    result2_new = result2.sort_values('money')
    result2_new = result2_new.reset_index(drop=True)
    result2_new = result2_new.loc[(result2_new["len"] <=220+begin) & (result2_new["code"]<=688000)]
    result1.to_excel(str(lastjiaoyiri)+str(begin)+'--'+str(times) + 'jinridiefu.xlsx', index=False)           
    result2.to_excel(str(lastjiaoyiri)+str(begin)+'--'+str(times) + 'jinrizhangfu.xlsx', index=False)  
    result1_new.to_excel(str(lastjiaoyiri)+str(begin)+'-new-'+str(times) + 'jinridiefu.xlsx', index=False)           
    result2_new.to_excel(str(lastjiaoyiri)+str(begin)+'--new'+str(times) + 'jinrizhangfu.xlsx', index=False)           
         
                        
    
       
    
    
    return
