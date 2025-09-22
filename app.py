from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

COMMON_WORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "admin",
    "letmein", "welcome", "iloveyou", "monkey", "dragon", "sunshine"
]

# Helper functions
def char_types(pw):
    types = set()
    if re.search(r"[a-z]", pw): types.add('lower')
    if re.search(r"[A-Z]", pw): types.add('upper')
    if re.search(r"[0-9]", pw): types.add('digit')
    if re.search(r"[^A-Za-z0-9]", pw): types.add('special')
    return types

def has_three_consecutive_identical(pw):
    return re.search(r'(.)\1\1', pw) is not None

def contains_common_word(pw):
    s = pw.lower()
    for w in COMMON_WORDS:
        if w in s:
            return True, w
    return False, None

def has_sequential_pattern(pw, seq_len=3):
    s = pw.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    for i in range(len(s) - seq_len + 1):
        sub = s[i:i+seq_len]
        if not re.match(r'^[a-z0-9]+$', sub):
            continue
        if sub in alpha or sub in digits or sub[::-1] in alpha or sub[::-1] in digits:
            return True
    return False

# Password scoring function
def score_password(pw):
    score = 0
    feedback = []

    length_ok = len(pw) >= 12
    types = char_types(pw)
    types_count = len(types)
    contains_common, which_word = contains_common_word(pw)
    three_consecutive = has_three_consecutive_identical(pw)
    sequential = has_sequential_pattern(pw)

    # Length
    if length_ok:
        score += 2
    else:
        feedback.append('Make the password at least 12 characters long.')

    # Character diversity
    if types_count <= 1:
        feedback.append('Use a mix of character types: uppercase, lowercase, numbers, special characters.')
    else:
        score += 2 * (types_count - 1)

    # Common words
    if not contains_common:
        score += 3
    else:
        feedback.append(f"Avoid common words or sequences like '{which_word}'.")

    # Repeating characters
    if not three_consecutive:
        score += 1
    else:
        feedback.append('Avoid more than two consecutive identical characters (e.g. "aaa").')

    # Sequential patterns
    if sequential:
        score -= 5
        feedback.append('Avoid obvious sequential patterns like "123", "abc", or reversed sequences.')

    # Strength level
    if score >= 10:
        level = 'Very Strong'
    elif 7 <= score <= 9:
        level = 'Strong'
    elif 4 <= score <= 6:
        level = 'Moderate'
    elif 1 <= score <= 3:
        level = 'Weak'
    else:
        level = 'Very Weak'

    if not feedback:
        feedback = ['No obvious problems detected. Consider using a password manager to generate/store long random passphrases.']

    return {
        'score': score,
        'level': level,
        'length_ok': length_ok,
        'types': list(types),
        'contains_common_word': contains_common,
        'three_consecutive': three_consecutive,
        'sequential_pattern': sequential,
        'feedback': feedback
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json() or {}
    pw = data.get('password', '')
    result = score_password(pw)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
