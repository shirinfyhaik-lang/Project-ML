import streamlit as st
st.title("Resume Screening")
st.header("Data Analysis")
skill_match_ratio=st.number_input("Enter your Skill match ratio:")
experience_gap=st.number_input("Enter your Experience gap:")
keyword_overlap=st.number_input("Enter your Keyword overlap:")
resume_length=st.number_input("Enter your Resume_length	:")
certification_score=st.number_input("Enter your Certification score:")
education_level=st.selectbox("Select education_level :",['Masters','Bachelors','Diploma','PhD'])
job_domain=st.selectbox("Select job_domain:",['Healthcare','Finance','Education','Marketing','IT'])

import joblib
classi=joblib.load(r'C:\Users\hp\Resume Screening.pkl')
label1=joblib.load(r'C:\Users\hp\le1.pkl')
label2=joblib.load(r'C:\Users\hp\le2.pkl')
stand=joblib.load(r'C:\Users\hp\sd.pkl')
education_level=label1.transform([education_level])[0]
job_domain=label2.transform([job_domain])[0]
if st.button('predict'):
    result=classi.predict(stand.transform([[skill_match_ratio,experience_gap,keyword_overlap,resume_length,certification_score,education_level,job_domain]]))[0]
    st.success(result)