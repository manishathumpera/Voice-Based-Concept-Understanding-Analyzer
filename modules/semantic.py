from sentence_transformers import SentenceTransformer, util

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(reference_text, user_text):
    """
    Compute semantic similarity between reference and user explanation.
    Returns a score between 0 and 100.
    """
    emb1 = model.encode(reference_text, convert_to_tensor=True)
    emb2 = model.encode(user_text, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()

    return round(score * 100, 2)