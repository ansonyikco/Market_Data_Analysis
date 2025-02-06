import streamlit as st
import Get_Data
import plotly.express as px
import streamlit as st
import pandas as pd
import LLM_comment
from io import StringIO

def compute_daily_return(df,each:str):
    value_list = df[each].tolist()
    key_date_value = value_list[0]
    
    df[each+'_dc'] = ((df[each] - key_date_value)/key_date_value)
    df['Value of '+each]= (1+df[each+'_dc'])*100
   
    return df

     

def make_pie_chart(df,values,names,col):
    fig = px.pie(df, values=values, names=names)
    fig.update_layout(
    
    title_text='Distribution according to {}'.format(names)
)
    if col is not None:
         
        col.plotly_chart(fig)
    else:
         st.plotly_chart(fig)

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

odf =  pd.DataFrame(
        [
            {"Ticker": "VOO","Type": "Stock,US ETF","Amount":20,"Price":0,"Value":0,"%":0,"Get Price": True,"To HKD": True},
            {"Ticker": "ie00bjxs6p07","Type": "Bond,Company ETF","Amount":20,"Price":0,"Value":0,"%":0,"Get Price": True,"To HKD": True},
            {"Ticker": "TLT","Type": "Bond,Long US Government ETF","Amount":20,"Price":0,"Value":0,"%":0,"Get Price": True,"To HKD": True},
            {"Ticker": "VXUS","Type": "Stock,International ETF","Amount":20,"Price":0,"Value":0,"%":0,"Get Price": True,"To HKD": True}
        ]
    )
if __name__ == "__main__":
    st.set_page_config(page_title=None, page_icon=":chart:", layout="wide", initial_sidebar_state="auto", menu_items=None)
    st.title("Manage Your Profile")
    st.write ("Assess if your profile is good enough")
    st.image("https://media.istockphoto.com/id/1453953453/photo/strategy-of-diversified-investment.jpg?s=612x612&w=0&k=20&c=GdKGA5EuK0QfKm76ExjkK64iPZLuTUOyIDQlXs-ZRQM=", caption="Manage your money")


    import pandas as pd
    import streamlit as st
    state = 'no data'
    
    with st.expander("Data Preparation"):
        with st.form("Upload Previous Profile"):
                st.write('Upload previous data')
                last_update = st.date_input("As at", value="2012-01-01")
                on = st.toggle("Mannual Input")
                uploaded_file = st.file_uploader("Choose a file",type='CSV')
                if uploaded_file is not None:
                    odf = pd.read_csv(uploaded_file, index_col=0)
                if not on:
                    osum= (sum(list((odf['Value']))))
                else:
                    osum = st.number_input("Input Your Value : ")
                submitted = st.form_submit_button("Save")
                if submitted:
                    

                    st.success('Last Fund Size : $'+str(osum), icon="✅")
                    st.success('Last Update Date : '+str(last_update), icon="✅")

        with st.form("Edit"):
                    st.write("Update Current / Create New")
                    update = st.date_input("As at", value="today")
                    edited_df = st.data_editor(
                    odf,num_rows="dynamic",use_container_width=True
                )
                    
                    df=edited_df
                    df[["Main_Type", "Sub_Type"]] = df["Type"].str.split(",", expand=True)
                    odf = df
                    #Ticker_list = edited_df["Ticker"].tolist()
                
                    # Every form must have a submit button.
                    submitted = st.form_submit_button("Save")
                    if submitted: 
                        df=edited_df              
                        st.success('Updated as at '+str(update), icon="✅")
                        state = 'ready'


    if state == 'ready':
        
        Ticker_list =[]
        sum=0
        for i, row in df.iterrows():
            if df.at[i,'Get Price'] ==True:
                Ticker_name = str(row['Ticker'].upper())
                Ticker_list.append(Ticker_name)
              
                Price = Get_Data.Get_Latest_Data(Ticker_name)
         
                df.at[i,'Price'] = Price
                        
                if df.at[i,'To HKD'] ==True:
                    df.at[i,'Value'] = round(Price*(row['Amount'])*7.78)
                else:
                    df.at[i,'Value'] = round(Price*(row['Amount']))
            else:
                if df.at[i,'To HKD'] ==True:
                    df.at[i,'Value'] = round(row['Price']*(row['Amount'])*7.78)
                else:
                    df.at[i,'Value'] = round(row['Amount'])

            sum+=df.at[i,'Value']
        
        for i, row in df.iterrows():
            df.at[i,'%'] = round((row['Value']/sum)*100)
        
        st.dataframe(df,use_container_width=True)
        st.subheader('Report',divider=True)
        with st.expander('Overall Report', expanded=True):
            
            st.write("Measurment from {} to {}: ".format(last_update,update))
            col1, col2 ,col3= st.columns(3,gap='small')
            col11, col12 = st.columns(2)
            container1 = st.container(border=True)


        period = (update-last_update ).days

        return_rate  = round((sum-osum)/osum,3)
        period_count = period/365
                #period_count = 0.5
        annualized_return_rate = round((((1+return_rate)**(1/period_count))-1),3)

        col1.metric("Total Fund Size", '$ '+str(sum.round()), "$ "+str(int(sum.round()-osum)))

        col2.metric("Return", str(return_rate*100) +'%')
        col3.metric("Annualized", str(annualized_return_rate*100) +'%')
        
        make_pie_chart(df,'%','Ticker',col11)
        make_pie_chart(df,'%','Main_Type',col12)
        #for i, row in df.iterrows():
        
        fig = px.bar(df, x="%", y="Main_Type", color='Sub_Type', orientation='h',
                hover_data=["Value"],
                title='Detailed Distribution')
        container1.plotly_chart(fig)
        
        movement = Get_Data.Get_Daily_Data(Ticker_list,last_update,update)
        print (movement)
        line_list = []
        for each in Ticker_list:
            movement =  compute_daily_return(movement,each)
        
            line_list.append('Value of '+each)
        
        fig = px.line((movement), x='Date', y=line_list,title='Asset Growth: $100 Investment Overview')
    
        fig.update_xaxes(minor=dict(ticks="outside", showgrid=True))

        st.plotly_chart(fig)

        with st.spinner('Wait for AI to make comment...'):
            Full_Name_list = Get_Data.Get_Full_Name(Ticker_list)
        
            with st.expander('Comment from AI ', expanded=False):
                st.write(LLM_comment.AI_comment(Full_Name_list))
        
        

    else:
        st.write ("No Data Yet")

