import PyPDF2
import tkinter as tk
from tkinter import filedialog


def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as f:
            merger.append(f)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"Merged PDF saved as {output_path}")


def select_pdf(prompt):
    # Open file dialog to select a single PDF file
    file = filedialog.askopenfilename(title=prompt, filetypes=[("PDF files", "*.pdf")])
    return file


def save_as():
    # Open file dialog to save the merged file
    file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    return file


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Select the first PDF file
    first_pdf = select_pdf("Select the first PDF file")

    if not first_pdf:
        print("No first file selected.")
        return

    # Select the second PDF file
    second_pdf = select_pdf("Select the second PDF file")

    if not second_pdf:
        print("No second file selected.")
        return

    # List of selected PDF files
    pdf_files = [first_pdf, second_pdf]

    # Choose location to save merged PDF
    output_pdf = save_as()

    if output_pdf:
        # Merge selected PDFs and save the output
        merge_pdfs(pdf_files, output_pdf)
    else:
        print("Save file was not selected.")


if __name__ == "__main__":
    main()
