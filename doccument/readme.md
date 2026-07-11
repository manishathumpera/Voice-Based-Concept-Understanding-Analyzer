                                                 🎤 Voice-Based Concept Understanding Analyzer (VBCUA)

The Voice-Based Concept Understanding Analyzer (VBCUA) is an AI-powered educational application that evaluates a student's conceptual understanding through voice responses. Instead of relying only on traditional written assessments, the system analyzes spoken explanations, converts speech into text using OpenAI Whisper, compares the response with reference concepts using semantic similarity, and generates an overall performance score.

The application also performs audio quality analysis by measuring speech duration, energy, speech rate, and pause percentage. Based on both speech characteristics and semantic understanding, the system calculates a final evaluation score and automatically generates a detailed PDF report for each student. The assessment results are also stored in a local database for future reference.

Features
🎙 Upload student voice recordings (MP3, WAV, M4A)
📝 Automatic Speech-to-Text conversion using Whisper AI
🧠 Semantic similarity evaluation using Sentence-BERT
📊 Audio quality analysis (duration, speech rate, energy, pauses)
⭐ Intelligent scoring based on speech and conceptual understanding
📄 Automatic PDF report generation
💾 SQLite database for storing assessment results
🌐 User-friendly web interface built with Streamlit
Technologies Used
Python
Streamlit
OpenAI Whisper
Sentence-Transformers (Sentence-BERT)
Librosa
NumPy
SQLite
ReportLab
FFmpeg
Applications

This project can be used in:

Educational institutions
Online learning platforms
Viva voce examinations
Concept-based assessments
AI-assisted learning systems
Student performance evaluation
