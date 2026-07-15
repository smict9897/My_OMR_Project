import streamlit as st
import pandas as pd
import cv2
import numpy as np

# ১. মাস্টার কি ফর্ম (আগের কোড অনুযায়ী)
if 'master_key' not in st.session_state:
    st.session_state.master_key = {}
if 'results' not in st.session_state:
    st.session_state.results = []

st.title("ওএমআর মূল্যায়ন সিস্টেম")

# মাস্টার কি ইনপুট সেকশন
with st.expander("মাস্টার কি সেট করুন"):
    cols = st.columns(3)
    for i in range(1, 31):
        st.session_state.master_key[i] = cols[(i-1)%3].selectbox(f"Q{i}", ["A", "B", "C", "D"], key=f"m_{i}")

# ২. ছাত্রের খাতা মূল্যায়ন সেকশন
st.divider()
roll_no = st.text_input("ছাত্রের রোল নম্বর:")
uploaded_file = st.file_uploader("ছাত্রের ওএমআর শিট আপলোড করুন...", type=["jpg", "png"])

if st.button("মূল্যায়ন ও সেভ করুন"):
    if uploaded_file and roll_no:
        # এখানে ইমেজ প্রসেসিং লজিক বসবে
        # ধরুন প্রসেসিং করে আমরা পেলাম ছাত্রের উত্তরগুলো student_answers (ডিকশনারি)
        # নমুনা উত্তর:
        student_answers = {i: 'A' for i in range(1, 31)} 
        
        # নম্বর গণনা
        score = sum(1 for i in range(1, 31) if student_answers[i] == st.session_state.master_key[i])
        
        # সেভ করা
        st.session_state.results.append({'Roll': roll_no, 'Marks': score})
        st.success(f"রোল {roll_no} এর নম্বর {score} জমা হয়েছে!")
    else:
        st.error("রোল এবং ছবি আপলোড করুন")

# রেজাল্ট টেবিল
if st.session_state.results:
    st.table(pd.DataFrame(st.session_state.results))
  
