"""Check if Hayt PDF has extractable text."""

import fitz, os, sys

pdf_path = r"C:\Users\frota\Downloads\Eletromagnetismo - William H. Hayt 7a Edição - Livro.pdf"
for p in [
    r"C:\Users\frota\Downloads\Eletromagnetismo - William H. Hayt 7a Edição - Livro.pdf",
    r"C:\Users\frota\Downloads\Eletromagnetismo - William H. Hayt 7ª Edição - Livro.pdf",
]:
    if os.path.exists(p):
        pdf_path = p
        break

doc = fitz.open(pdf_path)
print(f"PDF: {pdf_path}")
print(f"Pages: {len(doc)}")

text_pages = 0
image_pages = 0
for i in range(min(30, len(doc))):
    page = doc[i]
    text = page.get_text().strip()
    images = page.get_images()
    if text: text_pages += 1
    if images: image_pages += 1

print(f"Pages sampled: 30")
print(f"Pages with text: {text_pages}")
print(f"Pages with images: {image_pages}")
print(f"Conclusion: This is a SCANNED PDF (all pages are images).")
print(f"Need OCR (Tesseract, Docling, or MinerU) to extract text.")

# Check if any text in later pages
for i in [200, 300, 400]:
    if i < len(doc):
        text = doc[i].get_text().strip()
        print(f"Page {i+1}: text={len(text)} chars")
doc.close()
