from astroquery.exoplanet_orbit_database import ExoplanetOrbitDatabase
from sklearn.utils import column_or_1d
import streamlit as st
import plotly.express as px

eod_table = ExoplanetOrbitDatabase.get_table()
eod_table[:2]
eod_table = eod_table.to_pandas()
condition = ["BINARY","UR","UMASS"]
eod_table = eod_table[condition]
renamedic={"BINARY":"雙星系統",
            "UR":"星球半徑",
            "UMASS":"星球質量"
}
eod_table = eod_table.rename(columns=renamedic)


st.title("系外行星資料查詢系統")
st.dataframe(eod_table)
st.sidebar.text_input('輸入行星名字',eod_table.index[0])