import pymupdf

pdf_path = "the-war-of-art-steven-pressfield.pdf"

doc = pymupdf.open(pdf_path)

print("PDF opened successfully!")
print(f"Number of pages: {len(doc)}")

for page_number, page in enumerate(doc):
    text = page.get_text()

    print("\n" + "=" * 60)
    print(f"PAGE {page_number + 1}")
    print("=" * 60)

    print(text[:1000])

doc.close()