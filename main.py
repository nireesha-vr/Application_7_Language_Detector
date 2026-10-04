import re

# Common words for different languages
LANGUAGE_WORDS = {

    "English": {
        "the", "is", "are", "and", "this", "that", "you",
        "have", "with", "for", "from", "hello", "how",
        "what", "good", "morning", "today"
    },

    "French": {
        "le", "la", "les", "est", "et", "une", "un",
        "bonjour", "comment", "vous", "pour", "avec",
        "dans", "sur", "merci", "monde"
    },

    "Spanish": {
        "el", "la", "los", "las", "es", "y", "una", "un",
        "hola", "como", "para", "con", "por", "gracias",
        "mundo", "que"
    },

    "German": {
        "der", "die", "das", "ist", "und", "ein", "eine",
        "hallo", "wie", "danke", "mit", "für", "auf",
        "nicht", "ich", "sie"
    },

    "Italian": {
        "il", "la", "gli", "le", "è", "e", "un", "una",
        "ciao", "come", "grazie", "per", "con", "questo",
        "sono", "che"
    }
}


def detect_language(text):

    # Convert text to lowercase
    text = text.lower()

    # Extract words
    words = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', text)

    scores = {}

    # Compare words with each language
    for language, language_words in LANGUAGE_WORDS.items():

        score = 0

        for word in words:

            if word in language_words:
                score += 1

        scores[language] = score

    # Find language with highest score
    detected_language = max(scores, key=scores.get)

    # Get highest score
    highest_score = scores[detected_language]

    # If no matching words are found
    if highest_score == 0:
        return "Language could not be detected", scores

    return detected_language, scores


# --------------------------------
# MAIN PROGRAM
# --------------------------------

print("=" * 50)
print("             LANGUAGE DETECTOR")
print("=" * 50)

print("\nEnter a sentence or paragraph.\n")

text = input("Enter text: ")

if not text.strip():

    print("\nError: Please enter some text.")

else:

    language, scores = detect_language(text)

    print("\n" + "=" * 50)
    print("             DETECTION RESULT")
    print("=" * 50)

    print("Detected Language :", language)

    print("\nLanguage Scores:")

    for lang, score in scores.items():
        print(f"{lang:<10} : {score}")

    print("=" * 50)