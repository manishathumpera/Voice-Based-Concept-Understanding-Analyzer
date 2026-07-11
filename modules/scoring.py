"""
scoring.py
Calculates the overall evaluation score.
"""

def calculate_score(semantic_score, audio_metrics):
    """
    Calculate final score based on semantic similarity
    and speech quality.
    """

    score = semantic_score

    # Penalty for too many pauses
    if audio_metrics["pause_percentage"] > 25:
        score -= 10

    # Bonus for good speech energy
    if audio_metrics["energy"] > 0.03:
        score += 5

    # Clamp score to 0–100
    score = max(0, min(100, score))

    return round(score, 2)