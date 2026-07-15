import streamlit as st
import pandas as pd

st.title("অটোমেটেড ওএমআর মূল্যায়ন সিস্টেম")

# ১. মাস্টার শিট মেমরিতে ধরে রাখার জন্য সেশন স্টেট
if 'master_img' not in st.session_state:
    st.session_state.master_img = None

if 'results' not in st.session_state:
    st.session_state.results = []

# ২. মাস্টার কপি আপলোড সেকশন (এটি একবারই করবেন)
if st.session_state.master_img is None:
    master_file = st.file_uploader("মাস্টার শিট (সঠিক উত্তরের কপি) আপলোড করুন...", type=["jpg", "png"])
    if master_file:
        st.session_state.master_img = master_file
        st.success("মাস্টার শিট সফলভাবে সংরক্ষিত হয়েছে!")
        st.rerun() # অ্যাপটি রিলোড দিয়ে মাস্টার কপিটি লক করে দেবে
else:
    st.info("মাস্টার শিট আপলোড করা আছে।")
    if st.button("মাস্টার শিট পরিবর্তন করুন"):
        st.session_state.master_img = None
        st.rerun()

# ৩. পরবর্তী স্টুডেন্টদের কপি আপলোড
if st.session_state.master_img is not None:
    roll_no = st.text_input("ছাত্রের রোল নম্বর:")
    uploaded_file = st.file_uploader("ছাত্রের ওএমআর শিট আপলোড করুন...", type=["jpg", "png"])

    if st.button("মূল্যায়ন করুন"):
        if uploaded_file and roll_no:
            # এখানে আপনার ইমেজ প্রসেসিং লজিক কাজ করবে
            # st.session_state.master_img এবং uploaded_file এর তুলনা হবে
            marks = 8 # আপনার লজিক থেকে পাওয়া নম্বর
            
            st.session_state.results.append({'Roll': roll_no, 'Marks': marks})
            st.success(f"রোল {roll_no} এর নম্বর {marks} জমা হয়েছে!")
        else:
            st.warning("রোল নম্বর এবং ছবি আপলোড করুন।")

# রেজাল্ট টেবিল ও ডাউনলোড
if st.session_state.results:
    df = pd.DataFrame(st.session_state.results)
    st.table(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("সব রেজাল্ট ডাউনলোড করুন", csv, "results.csv", "text/csv")
