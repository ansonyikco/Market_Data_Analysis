import streamlit as st
import pandas as pd
odf =  pd.DataFrame(
        [
            {"Ticker": "VOO","Type": "Stock,US ETF","Amount":20,"Price":0,"Value":0,"%":0,"Get Price": True,"To HKD": True},
            {"Ticker": "ie00bjxs6p07","Type": "Bond,Company ETF","Amount":20,"Price":700000,"Value":0,"%":0,"Get Price": True,"To HKD": True},
            {"Ticker": "TLT","Type": "Bond,Long US Government ETF","Amount":20,"Price":50,"Value":0,"%":0,"Get Price": True,"To HKD": True},
            {"Ticker": "VXUS","Type": "Stock,International ETF","Amount":20,"Price":2300000000,"Value":0,"%":0,"Get Price": True,"To HKD": True}
        ]
    )

def check_quality(edited_df):
    state = True
    # check if number consistent
    checking_main = edited_df.groupby('Main_Type')['Main_Type_allocation'].nunique()
    checking_sub = edited_df.groupby('Sub_Type')['Sub_Type_allocation'].nunique()
    checking_ticker = edited_df.groupby('Ticker')['Ticker_allocation'].nunique()
    a =checking_main.index
    b = checking_sub.index
    c = checking_ticker.index
    i=0
    for each in checking_main:
        
        if each!=1: 
            st.write ('* Allocation of {} is not consistent between records'.format(a[i]))
            state = False
        i+=1
    i=0
    for each in checking_sub:
        if each!=1: 
            st.write ('* Allocation of {} is not consistent between records'.format(b[i]))
            state = False
        i+=1
    i=0
    for each in checking_ticker:
        if each!=1:
            st.write ('* Allocation of {} is not consistent between records'.format(c[i]))
            state = False
        i+=1
    #check if sum = 100
    checking_main = edited_df.groupby('Main_Type')['Main_Type_allocation'].mean()
    print (checking_main)
    checking_sub = edited_df.groupby('Main_Type')['Sub_Type_allocation'].sum()
    checking_ticker = edited_df.groupby('Sub_Type')['Ticker_allocation'].sum()
    print (checking_ticker)
    if (checking_main.sum()!=100):
        st.write ('* Sum of Allocation of {} is not 100'.format('Main_Type'))
        state = False
    for i in range(len(checking_sub)):
        if checking_sub[i] !=100:
            st.write ('* Sum of {} under {} is not 100, is {}'.format('Sub_Type',a[i],checking_sub[i]))
            state = False
    for i in range(len(checking_ticker)):
        if checking_ticker[i] !=100:
            st.write ('* Sum of {} under {} is not 100, is {}'.format('Ticker',b[i],checking_ticker[i]))
            state = False
    return state

df = odf
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    odf = pd.read_csv(uploaded_file) 
df = odf
df[["Main_Type", "Sub_Type"]] = df["Type"].str.split(",", expand=True)
df = df[['Main_Type','Sub_Type','Ticker']]
df[['Main_Type_allocation','Sub_Type_allocation','Ticker_allocation','Target_Amount']] = 0
df = df[['Main_Type','Main_Type_allocation','Sub_Type','Sub_Type_allocation','Ticker','Ticker_allocation','Target_Amount']]


df = st.data_editor(df,num_rows='dynamic')

state = check_quality(df)
st.write(state)
if state ==True:
    current_amount = odf['Value'].sum()
    new_money  = st.number_input("Enter a number:", value=10000)
    input_amount = current_amount+new_money
    df['Target_Amount'] = 0
   
    df['Target_Amount'] = input_amount*(df['Main_Type_allocation']/100)*(df['Sub_Type_allocation']/100)*(df['Ticker_allocation']/100)
    current_df = odf[['Ticker','Value']]
    action_df = df[['Ticker','Target_Amount']]
    
    ndf = pd.merge(current_df, action_df, on='Ticker', how='outer')
    ndf = ndf.fillna(value=0)
    ndf['Delta']=ndf['Target_Amount']-ndf['Value']
    
    sell_df = ndf[ndf['Delta'] < 0]
    sell_df['Sell_Value'] = sell_df['Delta']*-1
  
    sell_df = sell_df[['Ticker','Sell_Value']]
 
   
    buy_df = ndf[ndf['Delta'] > 0]
    buy_df['Buy_Value'] = buy_df['Delta']
    buy_df = buy_df[['Ticker','Buy_Value']]
 
    st.write(current_amount)
    col1, col2= st.columns(2)
    with col1:
        st.write('To sell: ')
        st.dataframe(sell_df)
    with col2:
        st.write('To buy: ')
        st.dataframe(buy_df)

    


