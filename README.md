Here's a well-structured **README.md** file for your project. It includes a project description, setup instructions, usage guide, and dependencies.

---

# **PDF Operations Tool 📝**

A Python-based CLI tool that allows users to perform various operations on PDF files, such as merging, splitting, rotating, converting, and securing PDFs with passwords.

## 🚀 Features

This tool supports the following operations:

1. **Merge PDFs** – Combines all PDFs in the current folder into one.  
2. **Protect PDF With Password** – Encrypts a PDF with a password.  
3. **Convert PDF to Word** – Converts a PDF file into a Word document.  
4. **Convert PDF to Images** – Extracts pages of a PDF as images.  
5. **Swap Pages in PDF** – Swaps the position of two pages in a PDF.  
6. **Delete Pages in PDF** – Removes specific pages from a PDF.  
7. **Reverse PDF** – Reverses the order of pages in a PDF.  
8. **Rotate PDF** – Rotates pages in a PDF by a specified angle.  
9. **Split PDF Pages** – Splits each page of a PDF into a new file.  

---

## 📌 Prerequisites

Ensure you have **Python 3.x** installed and install the required dependencies using:

```sh
pip install pikepdf pdf2docx pdf2image
```

> **Note:** For `pdf2image`, you need to install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases) and set its path.

---

## 📂 Installation & Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/pdf-operations-tool.git
   cd pdf-operations-tool
   ```

2. **Run the script:**
   ```sh
   python pdf_tool.py
   ```

3. **Follow on-screen instructions** to select the desired operation.

---

## 🔧 How It Works

1. The script welcomes the user and asks for an operation number.
2. Based on selection, it prompts the user for inputs (file path, new file name, page numbers, etc.).
3. The operation is performed, and the modified file is saved.

---

## 🛠 Dependencies

- **pikepdf** – For PDF manipulation (merging, rotating, encrypting, etc.).
- **pdf2docx** – For converting PDFs to Word documents.
- **pdf2image** – For extracting images from PDFs.
- **time** (built-in) – For greeting messages.

Install all dependencies with:

```sh
pip install -r requirements.txt
```

---

## 📝 Example Usage

- **Merge PDFs:**  
  - Place PDFs in the same folder as the script.
  - Run the script and select `1` to merge.
  - Enter the output filename, and it will generate a merged PDF.

- **Protect a PDF with a password:**
  - Select `2`, enter the file path and password.
  - The encrypted PDF will be saved.

- **Convert PDF to Word:**
  - Select `3`, enter the file path and output name.
  - A `.docx` file will be created.

---

## 🏗️ Future Enhancements

- Add a GUI version for better user experience.
- Support batch processing for multiple PDFs.
- Include more advanced features like OCR for scanned PDFs.

---

## 🏆 Contribution

Contributions are welcome! Feel free to fork the repo, make improvements, and submit a PR.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Author

Developed by **[Yash Maske]**  
GitHub: [Your GitHub](https://github.com/yash-maske)

---

