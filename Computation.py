import pandas as pd
import statistics as s
import random
import math
import numpy as np
def situation_generation(n):
    
    
    
    aa = []
    for each in range(2000):
        init_n= 100
      
        i_list=[]
        for i in range(n-1):
            b= random.randint(0,init_n)
            
            init_n = init_n-b
            i_list.append(b)
           
        
        
        d= max(100-sum(i_list),0)
        
        i_list.append(d)
       
        aa.append(tuple(i_list))
    aaa = set(aa)
    aaaaa=[]
    for each in aaa:
        aaaa= np.array(each)
        aaaaa.append(aaaa/100)

    return (aaaaa)

def compute_Ratio(all_case,VCV,r_list,rf):
    ratio_list = []
    return_list = []
    risk_list=[]
    for w in all_case:
        
        


        risk = math.sqrt(w@VCV@w.transpose())
        
        returning = w@np.array(r_list).transpose()
        return_list.append(returning)
        risk_list.append(risk)
        risk_return_ratio = (returning-rf)/risk
        ratio_list.append(risk_return_ratio)
        
    return ratio_list,return_list,risk_list

def getDelta(df,ticker):
    inflation = 0
    dividend_correction =0
    Return =[]
    last_price = 0.0001
    for this_price in df[ticker].tolist():
        Delta=this_price-last_price
        Return.append(((Delta/last_price)*100)-inflation)
        last_price = this_price
    mean_return = s.mean(Return[1:])+dividend_correction
    sd_return = s.stdev(Return[1:])
    return_ = [Return[1:],mean_return,sd_return]
    return return_
def Computation(ticker_list,df):
    return_list = []
    mean_return_list = []
    return_sd_list = []
    
    for each in ticker_list:
        info = getDelta(df,each)
        mean_return_list.append(info[1])
        print (each +' : '+str(info[1:]))
        return_list.append(info[0])
        return_sd_list.append(info[2])

    data = df.drop(columns=['Date'])
    corr = data.corr(method = 'pearson')
    print (corr)

    import numpy as np

    x = np.array(return_list)
    VCV = np.cov(x)
    print("Shape of array:\n", np.shape(x))

    print("Covariance matrix of x:\n", np.cov(x))

    all_case = situation_generation(len(ticker_list))
        
    ratio_list,E_return_list,E_risk_list = compute_Ratio(all_case,VCV,mean_return_list,0.0)
    string_all_case =[]
    for each in all_case:
        string_all_case.append(str(each))
    print (string_all_case)
        
    result = {

        "Allocation "+str(ticker_list): string_all_case,

        "Expected Return": E_return_list,

        "Risk": E_risk_list,
        
        'Sharpe Ratio':ratio_list

    }

    df = pd.DataFrame(result)


    df.sort_values(by=['Sharpe Ratio'],inplace=True,ascending=False)
  
    dict = {'Name': ticker_list, 'Annual Return': mean_return_list, 'STD': return_sd_list} 
   
    df_basic = pd.DataFrame(dict)
   



    return corr,df,df_basic