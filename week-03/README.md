# Week 03 - Machine Learning, NLP & LLM Foundations

All code in this folder comes from the course file `Week_03.docx`.
The only additions are listed under "Changes made to the doc code".

## Folder structure

```
week-03/
├── phase_01_ml_text_classification.py   # CountVectorizer + Naive Bayes
├── phase_02_text_preprocessing.py       # clean_text()
├── phase_03_tokenization/               # Code 01 - Code 11
├── phase_04_classification/             # TF-IDF classifiers + dataset.csv
├── phase_05_embeddings_similarity.py    # sentence embeddings + cosine similarity
├── phase_06_semantic_search.py          # semantic search over 4 documents
├── outputs/                             # saved console output (evidence)
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`sentence-transformers` installs `transformers` and `torch` automatically.
The first run of tokenizer / embedding scripts downloads models
(`bert-base-uncased`, `gpt2`, `all-MiniLM-L6-v2`), so internet is needed once.

## How to run

```bash
python phase_01_ml_text_classification.py
python phase_02_text_preprocessing.py

cd phase_03_tokenization
python code_01_bert_tokens.py        # ... through code_11_subword.py
cd ..

cd phase_04_classification
python code_01_pipeline_classifier.py
python code_02_sentiment_classifier.py
cd ..

python phase_05_embeddings_similarity.py
python phase_06_semantic_search.py
```

Run the `phase_03` and `phase_04` scripts from inside their own folder
(`code_06` writes `training.txt` / `my_tokenizer.*` and `code_01` reads `dataset.csv` from the current folder).

## Checklist mapping

| Checklist section | Files |
|---|---|
| 1. Text classification | `phase_01_...py`, `phase_04_classification/code_02_...py` |
| 2. Preprocessing | `phase_02_text_preprocessing.py` |
| 3. Tokenization | `phase_03_tokenization/code_01` - `code_11` (decode: code_02, compare tokenizers: code_05, special tokens: code_07) |
| 4. Embeddings & similarity | `phase_05_embeddings_similarity.py` |
| 5. Semantic search | `phase_06_semantic_search.py` (3 queries) |
| 6. Code quality / submission | this README, `outputs/` |

## Changes made to the doc code

The doc code is otherwise unchanged. Only these small additions were needed:

- `phase_02`: added three extra test sentences (checklist asks for multiple sentences).
- `phase_03/code_07`, `code_08`: added the BERT tokenizer loading lines from Code 01, because these snippets use a `tokenizer` variable without defining it.
- `phase_03/code_09`: the doc's text was garbled (`**name**`); restored to `if __name__ == "__main__":` with proper indentation.
- `phase_04/code_01`: the doc only defines functions, so a call `train_classifier("dataset.csv")` was added; `dataset.csv` is the table from the doc.
- `phase_06`: added two more queries (checklist asks for at least three).

## Evidence

`outputs/` holds real console output for the scripts that need no model download
(phase 01, 02, 03 code 03/04/09/10, phase 04). Scripts needing Hugging Face models or
SentencePiece (phase 03 code 01, 02, 05, 06, 07, 08, 11; phase 05; phase 06) must be run
on your machine, and screenshots of their output added to `outputs/`.

Note: the doc's datasets are tiny (4 test rows for `code_01`, 2 for `code_02`), so the
metrics are unstable. `code_02` gives accuracy 0.0 on its 2-row test set, while still
predicting "positive" for "I really love this". This comes from the data size, not an error.

## Short explanations

**Training vs inference.** Training fits the model's parameters to labeled data
(`model.fit`). Inference uses the trained model to predict on new, unseen text
(`model.predict`) without changing it.

**Why preprocessing helps.** It makes text consistent (lowercase, no extra spaces or
punctuation), so "HELP!!!" and "help" become the same input. This reduces noise and
vocabulary size and helps models focus on meaning.

**Special tokens.** Tokens added by the tokenizer for the model's structure, e.g. BERT's
`[CLS]` (start of sequence) and `[SEP]` (end / separator). They appear in the token IDs when
`add_special_tokens=True`.

**Subword tokenization.** Rare words are split into smaller known pieces (e.g. "playing" ->
"playing" or "play" + "##ing"), so the model handles unseen words without a huge vocabulary
or many `<UNK>` tokens.

**Word counts vs embeddings.** Counts (CountVectorizer/TF-IDF) only record which words
appear, so "forgot my password" and "reset my login" share almost nothing. Embeddings are
dense vectors where similar meanings are close, so they match by meaning, not exact words.

**Reading similarity scores.** Cosine similarity ranges up to 1. A high score (e.g. password
question vs "I forgot my password") means similar meaning; a low score (password vs weather)
means unrelated.
