import json

def load_high_scores(file_path="high_scores.json"):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_high_scores(scores, file_path="high_scores.json"):
    with open(file_path, 'w') as file:
        json.dump(scores, file)

def add_score(new_score, scores, max_scores=10):
    scores.append(new_score)
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    return scores[:max_scores]
