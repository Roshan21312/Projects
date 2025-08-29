import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import numpy as np
import Backtest as bt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from st_aggrid import AgGrid,GridOptionsBuilder

L = np.arange(1,31,1)
L = L.tolist()

peri = [str(i)+"y" for i in L]
periods = peri+['max']

wiki = "https://en.wikipedia.org/wiki/"
SP500 = pd.read_html(wiki+'List_of_S%26P_500_companies')[0]
DJI = pd.read_html(wiki+'Dow_Jones_Industrial_Average#Components')[2]
NASDAQ = pd.read_html(wiki+"Nasdaq-100#Components")[4]


assets = pd.concat([SP500.iloc[:,0],DJI.iloc[:,2],NASDAQ.iloc[:,0]],ignore_index=True)
assets.drop_duplicates(inplace=True)

assets = [None] + assets.tolist()
indicators = ['RSI','Stochastic Indicator']
operators = ['Greater than','Less than']

st.title("AlphaForge — No-Code Backtesting Framework")

asset=None
with st.sidebar:
    st.write("# Data Parameters")
    asset = st.selectbox("Select Asset",assets)

    per = st.select_slider("Select Period",periods,'5y')
    end_date =st.date_input('End Date',datetime.date.today().strftime('%Y-%m-%d'))

    st.write("# Indicator paramters")
    no_of_indi = st.number_input("No.of Indicators" ,min_value = 1,max_value = 3)

    params={}
    for i in range(no_of_indi):
        with st.expander(f"# Indicator {i+1} settings:",expanded = True):
            indi = st.selectbox("Select indicator",indicators, key = f'indi {i+1}')
            
            st.markdown("### lookback window ")
            lookback = st.number_input("Lookback Window",min_value = 1,max_value = 1000 , key=f'lkbk {i+1}')

            st.markdown("### Thresholds")
            st.write("Keep 0 if you do not want to keep entry or exit threshold.")

            st.write("#### We assume opposite operator for exit threshold")
            col1,col2,col3 = st.columns(3)
            with col1:
                compare1 = st.selectbox("Close Comparison with entry threshold",operators ,key=f'lo_op{i}') 
            with col2:
                lo_en = st.number_input(f"Long Entry threshold",key = f"lo_en_{i}")
            with col3:
                lo_ex = st.number_input(f"Long Exit threshold",key = f"lo_ex_{i}")

            col4,col5,col6 = st.columns(3)
            with col4:
                compare2 = st.selectbox("",operators ,key=f'so_op{i}') 
            with col5:
                so_en = st.number_input(f"Short Entry threshold",key = f"so_en_{i}")
            with col6:
                so_ex = st.number_input(f"Short Exit threshold",key = f"so_ex_{i}")
            params[indi]=[lookback,compare1,lo_en,lo_ex,compare2,so_en,so_ex]

    run = st.button("Run Backtest")

    st.sidebar.markdown("---")
    st.sidebar.caption("© 2025 AlphaForge. All rights reserved.")


if 'run_backtest' not in st.session_state:
    st.session_state['run_backtest'] = False

if run:
    st.session_state['run_backtest'] = True
    st.session_state['results'] = None



if 'results' not in st.session_state:
    st.session_state['results']=None


if st.session_state['run_backtest']: 
    st.session_state['results']=None

    if asset !=None:
        data = bt.get_data(asset,per,end_date)

        data = bt.indicator_computing(data,params)

        data = data.dropna()


        data , trade_log = bt.signals(data,params)

        fig1,fig2,fig3 = bt.plot_returns(data)

        metric = bt.statistics(data,trade_log)

        st.session_state['results']={
            'data':data,
            'trade_log':trade_log,
            'fig1':fig1,
            'fig2':fig2,
            'fig3':fig3,
            'metric':metric
        }
    else:
        st.write("select asset to plot graph.")

if st.session_state['results'] is not None:
        metric = st.session_state['results']['metric']
        fig1 = st.session_state['results']['fig1']
        fig2 = st.session_state['results']['fig2']
        fig3 = st.session_state['results']['fig3']
        trade_log = st.session_state['results']['trade_log']
        data = st.session_state['results']['data']

        st.write("### Metrics")
        col7,col8,col9 = st.columns(3)
        col7.metric('Sharpe',metric['Sharpe'])
        col8.metric("CAGR (%)",metric['CAGR'])
        col9.metric("Max Drawdown (%)",metric['Max Drawdown'])

        col10,col11,col12 = st.columns(3)
        col10.metric("Sortino",metric['Sortino'])
        col11.metric("Win rate (%)",metric['Win Rate'])
        col12.metric("Calmer",metric['Calmer'])

        st.metric("Profit Factor",metric['Profit Factor'])

        st.write("### Price Chart")
        st.plotly_chart(fig1,use_container_width=True)

        st.write("### Results")
        tab1,tab2,tab3 = st.tabs(['Equtiy Growth','Drawdown','Trade log'])
        
        with tab1:
            st.plotly_chart(fig2,use_container_width=True)
        with tab2:
            st.plotly_chart(fig3,use_container_width=True)
        with tab3:
            gd = GridOptionsBuilder.from_dataframe(trade_log)
            gd.configure_pagination(paginationAutoPageSize=True)
            gd.configure_side_bar()
            gd.configure_default_column(editable=False ,sortable=True,filter=True ,groupable=True)
            grid_options = gd.build()
            AgGrid(trade_log, gridOptions=grid_options, theme='balham',update_mode='NO_UPDATE')
