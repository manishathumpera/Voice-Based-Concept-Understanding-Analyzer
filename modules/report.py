from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_report(student_name, topic, semantic_score, audio_metrics, final_score):
    """
    Generate a PDF report.
    """

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{student_name.replace(' ', '_')}_Report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, 760, "Voice Based Concept Analysis")

    c.setFont("Helvetica", 12)

    y = 720

    c.drawString(50, y, f"Student Name: {student_name}")
    y -= 25

    c.drawString(50, y, f"Concept: {topic}")
    y -= 25

    c.drawString(50, y, f"Semantic Score: {semantic_score}")
    y -= 25

    c.drawString(50, y, f"Duration: {audio_metrics['duration']} sec")
    y -= 25

    c.drawString(50, y, f"Energy: {audio_metrics['energy']}")
    y -= 25

    c.drawString(50, y, f"Speech Rate: {audio_metrics['speech_rate']}")
    y -= 25

    c.drawString(50, y, f"Pause Percentage: {audio_metrics['pause_percentage']} %")
    y -= 25

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Final Score: {final_score}/100")

    c.save()

    return filename
