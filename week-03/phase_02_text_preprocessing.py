# Phase 02 - NLP: Text Preprocessing
import re


def clean_text(text: str) -> str:
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text


text = "   I NEED HELP!!!   "
print(clean_text(text))

# Added for the checklist item "test using multiple sentences"
# (same clean_text function, extra inputs only)
more_sentences = [
    "  Hello,   World!!  ",
    "WHEN is the   FINAL exam?",
    "I cannot login to the student portal.",
]
for sentence in more_sentences:
    print(clean_text(sentence))
