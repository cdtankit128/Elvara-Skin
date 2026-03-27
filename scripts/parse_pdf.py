import fitz  # type: ignore  # PyMuPDF - installed at runtime via uv
import sys

def extract_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        with open('output_utf8.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n\n--- CONTENT FROM: {pdf_path} ---\n\n")
            f.write(text)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

# clear file before writing
with open('output_utf8.txt', 'w', encoding='utf-8') as f:
    f.write("")

extract_text(r'C:\Users\91790\Desktop\Store_Design_Standards_Official.pdf')
extract_text(r'C:\Users\91790\Desktop\Elvara Skin\scripts\2_Days_Intensive_Shopify_Training_Official.pdf')
