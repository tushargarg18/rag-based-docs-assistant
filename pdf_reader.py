import pdfplumber

def extract_text_from_pdf(pdf_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
    return all_text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap  # move start with overlap
    return chunks

if __name__ == "__main__":
    pdf_path = "D:\Projects\RAG_Doc_Assistance\Data\script_07a_joint_distributions.pdf"  # Put your PDF here
    text = extract_text_from_pdf(pdf_path)
    print(f"Total characters extracted: {len(text)}")

    chunks = chunk_text(text)
    print(f"Total chunks created: {len(chunks)}")
    print("\nSample chunk:\n", chunks[0])
