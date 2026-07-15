import streamlit as st
import pandas as pd
import numpy as np
import cv2

# অ্যাপের শিরোনাম
st.title("অটোমেটেড ওএমআর মূল্যায়ন সিস্টেম")

# ১. সেশন স্টেট ইনিশিয়ালাইজেশন
if 'master_key' not in st.session_state:
    st.session_state.master_key = {}
if 'results' not in st.session_state:
    st.session_state.results = []

# ২. মাস্টার কি সেটআপ ফর্ম (ড্রপডাউন)
with st.expander("মাস্টার উত্তরপত্র সেট করুন"):
    st.write("প্রতিটি প্রশ্নের সঠিক উত্তর নির্বাচন করুন:")
    cols = st.columns(4)
    temp_key = {}
    for i in range(1, 31):
        # প্রশ্নের অপশনগুলো ৪টি কলামে সাজানো
        idx = (i-1) % 4
        temp_key[i] = cols[idx].selectbox(f"প্রশ্ন {i}", ["ক", "খ", "গ", "ঘ"], key=f"m_{i}")
    
    if st.button("সঠিক উত্তর সেভ করুন"):
        st.session_state.master_key = temp_key
        st.success("মাস্টার কি সফলভাবে সেভ হয়েছে!")

# ৩. ছাত্রের ওএমআর শিট মূল্যায়ন
st.divider()
st.subheader("ছাত্রের খাতা মূল্যায়ন করুন")
roll_no = st.text_input("ছাত্রের রোল নম্বর:")
uploaded_file = st.file_uploader("ওএমআর শিটের ছবি আপলোড করুন", type=["jpg", "png", "jpeg"])

def process_omr_image(image_file):
    """
    ছবি থেকে পিক্সেল কাউন্ট করে উত্তর বের করার ফাংশন।
    """
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1) # ছবি লোড করা
    
    # এখানে ভবিষ্যতে আপনার ইমেজ প্রসেসিং কোড যোগ করবেন
    return {i: 'ক' for i in range(1, 31)} # ডামি লজিক

if st.button("মূল্যায়ন শুরু করুন"):
    if not st.session_state.master_key:
        st.error("দয়া করে আগে মাস্টার কি সেট করুন!")
    elif uploaded_file and roll_no:
        student_answers = process_omr_image(uploaded_file)
        
        # স্কোর গণনা
        score = sum(1 for i in range(1, 31) if student_answers[i] == st.session_state.master_key[i])
        
        # রেজাল্ট জমা রাখা
        st.session_state.results.append({'Roll': roll_no, 'Marks': score})
        st.success(f"রোল {roll_no} এর নম্বর {score} জমা হয়েছে!")
    else:
        st.warning("রোল নম্বর এবং ছবি দিন।")

# ৪. রেজাল্ট টেবিল ও ডাউনলোড
if st.session_state.results:
    st.subheader("ফলাফল তালিকা")
    df = pd.DataFrame(st.session_state.results)
    st.table(df)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("ফলাফল ডাউনলোড করুন (CSV)", csv, "results.csv", "text/csv")
