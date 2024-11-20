import streamlit as st
import pandas as pd
import numpy as np
import Get_Data
import Computation

import plotly.express as px
st.title("Datalysis- Platform for market data analysis")
st.write(
    "Under Constrcution"
)

import pandas as pd
import numpy as np
df = None

with st.expander("Custom Data"):
    
    with st.form("my_form"):
        tickers = st.text_input("Tickers title", "VOO,TLT")
        st.form_submit_button('Submit')
        
tickers_list = tickers.split(",")

df = Get_Data.Get_Data(tickers_list)
st.write ("\nData start from : "+str(df['Date'][0]))
#chart_data = (pd.DataFrame(df), columns='Close/Last')
Result = Computation.Computation(tickers_list,df)



col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.header("Statistic")
    st.dataframe(Result[2])
    st.divider()
    
    
 
        
with col2:
    
    st.header("Correlation Study")
    st.dataframe(Result[0])
    st.divider()
st.title('Portfolio Optimization')






fig = px.scatter(Result[1], x="Risk", y="Expected Return", hover_data="Allocation"+" "+str(tickers_list), log_x=False, size_max=60,color="Sharpe Ratio")

fig.update_traces(textposition='top center')

fig.update_layout(
    height=800,
    title_text='Chart'
)

st.plotly_chart(fig)

st.dataframe(Result[1])
st.title('Raw Data')
st.dataframe(df)