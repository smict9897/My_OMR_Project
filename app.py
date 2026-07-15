
import streamlit as st
import pandas as pd

st.title("অটোমেটেড ওএমআর মূল্যায়ন সিস্টেম")

# মেমরিতে রেজাল্ট জমা রাখার জন্য সেশন স্টেট তৈরি
if 'results' not in st.session_state:
st.session_state.results = []

# ইনপুট ফিল্ড
roll_no = st.text_input("ছাত্রের রোল নম্বর:")
uploaded_file = st.file_uploader("ওএমআর শিটের ছবি:", type=["jpg", "png"])

if st.button("মূল্যায়ন করুন"):
if uploaded_file and roll_no:
# এখানে আপনার মূল্যায়নের লজিক বসবে (আমি আপাতত র‍্যান্ডম একটি নম্বর দিচ্ছি)
# ধরি ছাত্রটি ১০ এর মধ্যে ৮ পেয়েছে
marks = 8

# সেশন স্টেটে রেজাল্ট জমা রাখা
st.session_state.results.append({'Roll': roll_no, 'Marks': marks})
st.success(f"রোল {roll_no} এর নম্বর {marks} জমা হয়েছে!")
else:
st.warning("রোল নম্বর এবং ছবি আপলোড করুন।")

# বর্তমান রেজাল্ট টেবিল দেখানো
if st.session_state.results:
df = pd.DataFrame(st.session_state.results)
st.table(df)

# CSV ডাউনলোড করার বাটন
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
label="সব রেজাল্ট CSV হিসেবে ডাউনলোড করুন",
data=csv,
file_name='all_results.csv',
mime='text/csv',
)

if st.button("তালিকা পরিষ্কার করুন (Reset)"):
st.session_state.results = []
st.rerun()
