
from streamlit_func import main_selector
import pandas as pd 
import streamlit as st 
from PIL import Image
import streamlit_func as func
import streamlit_info as info

data = pd.read_csv(info.data_path,sep=';')

st.sidebar.title('MAIN MENU')
st.sidebar.file_uploader(
        label='User Data',
        type='csv'
    )

# func.main_selector()

# func.expander()

# func.echo_data(data)

# func.graph(data)


menu = st.sidebar.selectbox('Selection Menu',('Home','Graph','Filter'))

if menu == 'Home':

    func.main_selector()

    func.expander()

    func.echo_data(data)

if menu == 'Graph':

    func.graph(data)



if menu == 'Filter':

    data = func.filter_options(data)
    func.graph(data)
    # st.write(a)
    # st.write(b)
    # st.write(c)















    
    







# %%
