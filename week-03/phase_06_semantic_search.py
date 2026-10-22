# Phase 06 - Semantic Search
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    "Students can register courses through the student portal.",
    "The examination office publishes examination schedules.",
    "The finance office handles tuition fee issues.",
    "The library provides digital research resources.",
]


# The doc has one query; the checklist asks for at least three, so two
# more were added to this list. The search code below is unchanged.
queries = [
    "Where can I register my courses?",
    "When will the exam dates be announced?",
    "Where can I find research books and journals?",
]


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


document_embeddings = model.encode(
    documents
)

for query in queries:

    query_embedding = model.encode(
        [query]
    )

    scores = cosine_similarity(
        query_embedding,
        document_embeddings
    )[0]

    results = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True,
    )

    print("\nQuery:", query)

    for document, score in results:
        print(
            f"{score:.4f} -> {document}"
        )
