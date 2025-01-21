import os
# pip install PyPDF2
import PyPDF2
# pip install pdfplumber
import pdfplumber
# pip install markdownify
from markdownify import markdownify as md
# pip install pdf2image pytesseract
from pdf2image import convert_from_path
import pytesseract

from bs4 import BeautifulSoup

def pdf_to_text2(input_pdf_path, output_text_path):
	try:
		# Open the PDF file in binary mode
		with open(input_pdf_path, 'rb') as pdf_file:
			# Create a PDF reader object
			pdf_reader = PyPDF2.PdfFileReader(pdf_file)

			# Get the number of pages in the PDF
			num_pages = pdf_reader.numPages

			# Initialize an empty string to store the text
			text = ""

			# Iterate through all pages and extract text
			for page_num in range(num_pages):
				page = pdf_reader.getPage(page_num)
				text += page.extractText()

			# Write the extracted text to the output text file
			with open(output_text_path, 'w', encoding='utf-8') as text_file:
				text_file.write(text)

			print(f"Conversion successful. Text saved to {output_text_path}")

	except Exception as e:
		print(f"Error: {e}")

def test_pdf_to_text2():
	pdf_to_text2("example.pdf", "output.txt")


def pdf_to_text(input_pdf_path, output_text_path):
    try:
        # Open the PDF file in binary mode
        with open(input_pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Get the number of pages in the PDF
            num_pages = len(pdf_reader.pages)

            # Initialize an empty string to store the text
            text = ""

            # Iterate through all pages and extract text
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Write the extracted text to the output text file
            with open(output_text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            print(f"Conversion successful. Text saved to {output_text_path}")

    except Exception as e:
        print(f"Error: {e}")

def test_pdf_to_text():
	pdf_to_text("example.pdf", "output.txt")


def pdf_to_markdown(input_pdf_path, output_md_path):
	try:
		# Open the PDF file
		with pdfplumber.open(input_pdf_path) as pdf:
			# Initialize an empty string to store the Markdown content
			markdown_content = ""

			# Iterate through all pages and extract text
			for page in pdf.pages:
				text = page.extract_text()
				markdown_content += md(text)  # Convert plain text to Markdown

			# Write the converted Markdown to the output file
			with open(output_md_path, 'w', encoding='utf-8') as md_file:
				md_file.write(markdown_content)

			print(f"Conversion successful. Markdown saved to {output_md_path}")

	except Exception as e:
		print(f"Error: {e}")

def test_pdf_to_markdown():
	pdf_to_markdown("example.pdf", "output.md")

def pdf_to_html(input_pdf_path, output_html_path):
	try:
		# Convert PDF pages to images using pdf2image
		images = convert_from_path(input_pdf_path)

		# Initialize an empty string to store the HTML content
		html_content = ""

		# Process each image and extract text using pytesseract
		for i, image in enumerate(images):
			text = pytesseract.image_to_string(image, lang='eng')
			html_content += f"<div class='pdf-page' id='page-{i+1}'>{text}</div>"

		# Wrap the HTML content in a basic HTML structure
		html_content = f"<html><head></head><body>{html_content}</body></html>"

		# Write the HTML content to the output file
		with open(output_html_path, 'w', encoding='utf-8') as html_file:
			html_file.write(html_content)

		print(f"Conversion successful. HTML saved to {output_html_path}")

	except Exception as e:
		print(f"Error: {e}")

def test_pdf_to_html():
	pdf_to_html("example.pdf", "output.html")


# import sys
# from schnell.app.inpututils import give_me
from schnell.app.promptutils import combobox_listbox		

def select_file_with_extension_filter(extension_filter=['.pdf']):
	current_directory = os.getcwd()
	files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

	if extension_filter:
		files = [f for f in files if f.endswith(tuple(extension_filter))]

	if not files:
		print("No files found.")
		return

	print("Select a file:")
	for i, file in enumerate(files, start=1):
		print(f"{i}. {file}")

	selected_file = combobox_listbox(files, return_index=False)
	selected_file = os.path.join(current_directory, selected_file)
	return selected_file

	# while True:
	# 	try:
	# 		# sys.stdin.flush()
	# 		user_choice = int(input(f"Enter the number of your choice (1-{len(files)}): "))
			
	# 		# masukkan = give_me('1')
	# 		# user_choice = int(masukkan)

	# 		if 1 <= user_choice <= len(files):
	# 			selected_file = os.path.join(current_directory, files[user_choice - 1])
	# 			print(f"Selected file: {selected_file}")
	# 			return selected_file
	# 		else:
	# 			print(f"Invalid choice. Please enter a number between 1 and {len(files)}.")
	# 	except ValueError:
	# 		print("Invalid input. Please enter a valid number.")

def test_select_file_with_extension_filter():
	selected_file = select_file_with_extension_filter([".txt", ".csv"])

