import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb

def main():
    html_temp="""
    <div style = "background-color:orange;padding:16px">
    <h1 style="color:black;text-align:center;">Car price prediction using machine learning</h1>
    </div>
    
    """
    
    model=xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.write('')
    st.write('')
    
    st.markdown("### Are you planning to sell your car!?\n##### so let's try evaluating the price.")
    
    p1=st.number_input("what is the current ex-showroom price of the car(In lakhs)",2.5,25.0,step=1.0)
    
    p2=st.number_input("what is the distance completed by the car(In Km)",100,50000,step=100)
    
    s1=st.selectbox("what is the fuel type of the car?",('Petrol','Diesel','CNG'))
    
    if s1=='Petrol':
        p3=0
    if s1=='Diesel':
        p3=1
    if s1=='CNG':
        p3=2
        
    s2=st.selectbox("Are you a dealer or Individual?",('Dealer','Individual'))
    
    if s2=='Dealer':
        p4=0
    if s2=='Individual':
        p4=1
    
    s3=st.selectbox("what is the transmission type ?",('Manual','Automatic'))
    
    if s3=='Manual':
        p5=0
    if s3=='Automatic':
        p5=1
    
    p6 = st.slider("Number of the owner the car previous had!?",0.3)
    
    date_time=datetime.datetime.now()
    
    years = st.number_input("In which year you car was purchased!?",1990,date_time.year)
    p7 = date_time.year - years
    
    
    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    
    
    
    try:
        if st.button('Predict'):
             pred = model.predict(data_new)
             if pred>0:
                 st.balloons()
                 st.success("You can sell your car for {} Lakhs".format(pred))
             else:
                 st.Warning("You can't able to sell this car")
                 
    except:
        st.warning("Something Went Wrong please try again")

      












if __name__== '__main__':
    main()
