import streamlit as st
import pandas as pd

st.title("ওএমআর মূল্যায়ন সিস্টেম - মাস্টার কি ইনপুট")

# ১. সঠিক উত্তরগুলো ইনপুট দেওয়ার ব্যবস্থা
st.subheader("সঠিক উত্তরের তালিকা (যেমন: A,C,D,B,...)")
answer_input = st.text_area("এখানে ৩০টি প্রশ্নের উত্তর কমা (,) দিয়ে লিখুন:", 
                           placeholder="A,C,B,D,A,C,B,D,... (মোট ৩০টি)")

# উত্তরগুলোকে লিস্টে রূপান্তর করা
master_answers = [ans.strip().upper() for ans in answer_input.split(',')]

# ২. মূল্যায়নের অংশ
if len(master_answers) == 30:
    st.success("সঠিক উত্তরের তালিকা গৃহীত হয়েছে!")
    
    roll_no = st.text_input("ছাত্রের রোল নম্বর:")
    # ছাত্রের উত্তর ইনপুট (অথবা এখানে আপনার ইমেজ প্রসেসিং কোড বসবে)
    student_answers_input = st.text_area("ছাত্রের ভরাট করা উত্তরগুলো লিখুন (যেমন: A,B,C,D...):")
    
    if st.button("মূল্যায়ন করুন"):
        student_answers = [ans.strip().upper() for ans in student_answers_input.split(',')]
        
        # স্কোর ক্যালকুলেশন
        score = 0
        for i in range(len(master_answers)):
            if i < len(student_answers) and student_answers[i] == master_answers[i]:
                score += 1
        
        st.write(f"রোল: {roll_no} | প্রাপ্ত নম্বর: {score}/30")
        
        # গুগল শিট বা CSV তে পাঠানোর জন্য স্টোর করা (পূর্বের লজিক অনুযায়ী)
        if 'results' not in st.session_state:
            st.session_state.results = []
        st.session_state.results.append({'Roll': roll_no, 'Marks': score})
else:
    st.warning(f"দয়া করে মোট ৩০টি উত্তর দিন। বর্তমান ইনপুট সংখ্যা: {len(master_answers)}")

# রেজাল্ট টেবিল
if 'results' in st.session_state and st.session_state.results:
    df = pd.DataFrame(st.session_state.results)
    st.table(df)
