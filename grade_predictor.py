# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:36:17 2026

@author: ACER
"""

import streamlit as st


mark = []

st.title("Exam Grade Predictor")


st.write("Predict your future exam grade")

with st.form("Form"):
    
    st.subheader("Classroom Assessment Techniques")
    st.write("Rate it")
    
    
    hw = st.slider("Do you always submit your homework", min_value=0, max_value = 10,step = 1, value = 5)
    
    cw = st.slider("Do you always finish your classwork", min_value=0, max_value = 10,step = 1, value = 5)
    
    pro = st.slider("Do you always submit your projects", min_value=0, max_value = 10,step = 1, value = 5)
    
    behave = st.slider("Do you always well-behave in classroom", min_value=0, max_value = 10,step = 1, value = 5)
    
    
    #%%
    
    st.subheader("Last Exam Marks")
    
    last_exam_mark = st.slider("What is your last exam percentage?", min_value=0, max_value = 100,step = 1, value = 5)
    
    last_exam_mark = last_exam_mark/100 * 10
    mark.append(last_exam_mark)
    
    #%%
    
    revise = st.slider("Do you hours do you revise a day?", min_value=0, max_value = 5,step = 1, value = 5)
    std = st.slider("How many day per week do you study?", min_value=0, max_value = 7,step = 1, value = 5)
    relax = st.slider("Do you have enough rest time?", min_value=0, max_value = 10,step = 1, value = 5)
    sleep = st.slider("Do you have enough sleep time?", min_value=0, max_value = 10,step = 1, value = 5)
    food = st.slider("Do you eat healthy food(that would support your brain)?", min_value=0, max_value = 10,step = 1, value = 5)

    submit = st.form_submit_button("Predict My Grade")

#%%

if submit:
    
    HW = hw/10 * 8
    CW = cw/10 * 8
    PRO = pro/10 * 8
    B = behave/10 * 16
    
    CAT = HW + CW + PRO + B
    mark.append(CAT)
    
    
    revise = revise/5 * 10
    relax = relax/10 * 10
    food = food/10 * 10
    std = std/7 * 10
    sleep = sleep/10 * 10
    
    rn = revise + relax + food + std + sleep
    
    mark.append(rn)
    
    
    
    grade = int(sum(mark))
    
    
        
    if grade > 90:
        st.success(f"With your hard work, you will sure get A+ {grade}%")
            
    elif grade > 80:
        st.success(f"With your effort, an A ({grade}%) is waiting for you. ")
            
    elif grade > 70:
        st.success(f"Look like solid B({grade}%) is coming your way")
            
    elif grade > 60:
        st.success(f"C ({grade}%) is possible if you steadily keep going this way")
            
    else:
        st.error(f"I believe you just need to try a bit harder. Fail ({grade}%)")
        
        
    
    
    
    
