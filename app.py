import streamlit as st
from agent import analyze_claim, extract_score
st.set_page_config(page_title="Fake News Verification Agent",layout="centered")
st.markdown("""
<style>
    .title {text-align: center;font-size: 34px;font-weight: 700;margin-bottom: 5px;}
    .subtitle {text-align: center;color: #8a8a8a;margin-bottom: 25px;}
    .card {background-color: #0f1116;border: 1px solid #2a2f3a;padding: 20px;border-radius: 12px;margin-top: 20px;}
    .stTextArea textarea {background-color: #0b0d12;color: white;border-radius: 10px;}
    .stButton button {width: 100%;border-radius: 8px;font-weight: 600;background-color: #4a7dff;color: white;}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="title">Fake News Verification Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Goal-Based Intelligent Agent using Gemini AI</div>', unsafe_allow_html=True)
claim = st.text_area("Enter News / Claim",height=150,placeholder="Example: Scientists confirmed that drinking hot water cures cancer")
if st.button("Analyze Claim"):
    if not claim.strip():
        st.warning("Please enter a claim.")
    else:
        with st.spinner("Agent is analyzing the claim..."):
            result = analyze_claim(claim)
            score = extract_score(result)
        st.markdown("### Credibility Score")
        st.progress(score / 100)
        st.write(f"Score: {score}/100")
        st.markdown("### Analysis Report")
        st.markdown(f"""
        <div class="card">
            {result}
        </div>
        """, unsafe_allow_html=True)