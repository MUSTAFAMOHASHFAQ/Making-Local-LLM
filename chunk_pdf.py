import pymupdf

pdf_path = "the-war-of-art-steven-pressfield.pdf"

doc = pymupdf.open(pdf_path)

# Store all text here
full_text = ""

for page in doc:
    full_text += page.get_text() + "\n"

doc.close()

# Clean up excessive whitespace
full_text = " ".join(full_text.split())

# Chunk settings
chunk_size = 1000
overlap = 200

chunks = []

start = 0

while start < len(full_text):
    end = start + chunk_size

    chunk = full_text[start:end]

    chunks.append(chunk)

    start += chunk_size - overlap

print(f"Total characters: {len(full_text)}")
print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:5]):
    print("\n" + "=" * 70)
    print(f"CHUNK {i + 1}")
    print("=" * 70)
    print(chunk)