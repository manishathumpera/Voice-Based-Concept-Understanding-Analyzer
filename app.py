import streamlit as st
import tempfile
import whisper
import os
import shutil
from modules.concepts import get_topics, get_reference
from modules.semantic import semantic_similarity
from modules.audio_analysis import analyze_audio
from modules.scoring import calculate_score
from modules.report import generate_report
from modules.database import create_database, save_result
from modules.utils import ensure_directories

# ----------------------------------------
# Streamlit Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyzer",
    page_icon="🎤",
    layout="wide"
)

ensure_directories()
create_database()

st.title("🎤 Voice-Based Concept Understanding Analyzer (VBCUA)")
st.markdown("---")

# ----------------------------------------
# Load Whisper Model (Only Once)
# ----------------------------------------

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

model = load_whisper()

# ----------------------------------------
# Student Details
# ----------------------------------------

student_name = st.text_input("Student Name")

topics = get_topics()

selected_topic = st.selectbox(
    "Select Concept",
    topics
)

uploaded_audio = st.file_uploader(
    "Upload Student Audio",
    type=["wav", "mp3", "m4a"]
)

# ----------------------------------------
# Audio Processing
# ----------------------------------------

if uploaded_audio is not None:

    st.success("Audio uploaded successfully!")

    suffix = "." + uploaded_audio.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_audio.read())
        audio_path = tmp_file.name

    st.audio(audio_path)

    # Audio Analysis
    audio_metrics = analyze_audio(audio_path)

    st.subheader("🎙 Audio Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Duration", f"{audio_metrics['duration']} sec")
        st.metric("Energy", audio_metrics["energy"])

    with col2:
        st.metric("Speech Rate", audio_metrics["speech_rate"])
        st.metric("Pause %", audio_metrics["pause_percentage"])

    # ----------------------------------------
    # Speech-to-Text using Whisper
    # ----------------------------------------


    with st.spinner("Transcribing speech..."):

        st.write("Audio path:", audio_path)
        st.write("File exists:", os.path.exists(audio_path))
        st.write("File size:", os.path.getsize(audio_path))
        
        st.write("Python:", os.sys.executable)
        st.write("FFmpeg found:", shutil.which("ffmpeg"))

        result = model.transcribe(audio_path)

        transcript = result["text"]

    st.subheader("📝 Transcript")
    st.write(transcript)
        # ----------------------------------------
    # Semantic Similarity
    # ----------------------------------------

    reference_text = get_reference(selected_topic)

    with st.spinner("Calculating semantic similarity..."):
        semantic_score = semantic_similarity(
            reference_text,
            transcript
        )

    st.subheader("🧠 Semantic Analysis")

    st.metric(
        "Semantic Similarity",
        f"{semantic_score}%"
    )

    # ----------------------------------------
    # Final Score
    # ----------------------------------------

    final_score = calculate_score(
        semantic_score,
        audio_metrics
    )

    st.subheader("⭐ Final Evaluation")

    st.metric(
        "Final Score",
        f"{final_score}/100"
    )

    # ----------------------------------------
    # PDF Report
    # ----------------------------------------

    report_path = generate_report(
        student_name,
        selected_topic,
        semantic_score,
        audio_metrics,
        final_score
    )

    st.success("PDF Report Generated Successfully!")

    with open(report_path, "rb") as pdf:
        st.download_button(
            label="📄 Download Report",
            data=pdf,
            file_name=os.path.basename(report_path),
            mime="application/pdf"
        )
            # ----------------------------------------
    # Save Result to Database
    # ----------------------------------------

    save_result(
        student_name,
        selected_topic,
        semantic_score,
        final_score
    )

    st.success("✅ Result saved to database successfully!")

    # ----------------------------------------
    # Display Summary
    # ----------------------------------------

    st.markdown("---")
    st.subheader("📊 Analysis Summary")

    st.write(f"**Student Name:** {student_name}")
    st.write(f"**Concept:** {selected_topic}")
    st.write(f"**Semantic Similarity:** {semantic_score}%")
    st.write(f"**Final Score:** {final_score}/100")

    # ----------------------------------------
    # Clean Up Temporary File
    # ----------------------------------------

    try:
        os.remove(audio_path)
    except Exception:
        pass