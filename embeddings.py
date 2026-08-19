from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Resistance prevents people from doing creative work.",
    "The author discusses overcoming fear and procrastination.",
    "The weather today is sunny."
]

embeddings = model.encode(texts)

print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))

for i, embedding in enumerate(embeddings):
    print(f"\nText {i + 1}:")
    print(texts[i])
    print("First 10 numbers:")
    print(embedding[:10])