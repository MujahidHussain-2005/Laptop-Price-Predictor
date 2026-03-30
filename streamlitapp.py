import streamlit as st
import pandas as pd
import numpy as np
import requests
 
path='http://localhost:8001/predict'

st.title('Laptop Price Predictor')
st.write('Enter the details of your Laptop to predict its price')

Company=st.selectbox('Select the company of your laptop',['Apple','Dell','HP','Lenovo','Asus','Acer','MSI','Acer','Toshiba','Samsung','Razer','Mediacon','Microsoft','Vero','Google','Fujitsu','Huawei','LG','Xiaomi','Chuwi'])
TypeName=st.selectbox('select the type of your laptop',['Ultrabook','Notebook','Gaming','2 in 1 Convertible','Netbook','Workstation'])
inches=st.number_input('Enter the screen size in inches',min_value=0.0,step=0.1)
xresolution=st.selectbox('Enter the x resolution of your laptop',[7680, 5120, 3840, 2560, 1920, 1600, 1366, 1280, 1024, 640])
yresolution=st.selectbox('Enter the y resolution of your laptop',[4320, 3840, 2160, 1440, 1080, 900, 768, 720, 600, 480])
Ram=st.selectbox('Enter the RAM of your laptop in GB',[2, 4, 8, 16, 32, 64])
Weight=st.number_input('Enter the weight of your laptop in kg',min_value=0.0,step=0.1)
Touchscreen=st.selectbox('Does your laptop have a touchscreen?',[0,1])
IPS=st.selectbox('Does your laptop have an IPS display?',[0,1])
Processor=st.selectbox('Enter the processor of your laptop',['Intel Core i7','Intel Core i5','Intel Core i3','Other Intel Processor','AMD Processor'])
processor_speed=st.number_input('Enter the processor speed in GHz',min_value=0.0,step=0.1)
HDD=st.selectbox('Enter the HDD capacity of your laptop in GB',[0, 128, 256, 512, 1024, 2048])
SSD=st.selectbox('Enter the SSD capacity of your laptop in GB',[0, 128, 256, 512, 1024, 2048])
Gpu_Brand=st.selectbox('Enter the GPU brand of your laptop',['Intel','Nvidia','AMD','Other'])
OS=st.selectbox('Enter the operating system of your laptop',['Windows','Mac','Linux','Other'])

if st.button('Predict Price'):
    input_data={
        'company':Company,
        'typename':TypeName,
        'inches':inches,
        'xresolution':xresolution,
        'yresolution':yresolution,
        'ram':Ram,
        'weight':Weight,
        'touchscreen':Touchscreen,
        'ips':IPS,
        'processor':Processor,
        'processor_speed':processor_speed,
        'hdd':HDD,
        'ssd':SSD,
        'gpu_brand':Gpu_Brand,
        'os':OS
    }
try:
    response=requests.post(path,json=input_data)
    if response.status_code==200:
        st.success(f'The predicted price of your laptop is: {response.json()}')
    else:
        st.error(f'error in prediction {response.status_code}')
except Exception as e:
    st.error(f'An error occurred: {e}')