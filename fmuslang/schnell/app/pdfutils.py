# berbagai teknik manipulasi pdf yg banyak digunakan di upwork

"""
https://www.thepythoncode.com/article/redact-and-highlight-text-in-pdf-with-python
https://www.thepythoncode.com/article/extract-pdf-tables-in-python-camelot
https://www.thepythoncode.com/article/compress-pdf-files-in-python
https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
https://www.thepythoncode.com/article/extract-text-from-images-or-scanned-pdf-python
https://www.thepythoncode.com/article/extract-text-from-pdf-in-python
https://www.thepythoncode.com/article/encrypt-pdf-files-in-python
"""

import pytesseract
from pytesseract import Output
import argparse
import cv2
import filetype
import fitz
import numpy as np
import os
import pandas as pd
import re
import sys
from io import BytesIO
from PIL import Image
from typing import Tuple
from pprint import pprint

# fitz butuh pymupdf utk frontend
# pip install pytesseract PyMuPDF fitz filetype pyAesCrypt

# pip install Filetype==1.0.7 numpy==1.19.4 opencv-python==4.4.0.46 pandas==1.1.4 Pillow==8.0.1 PyMuPDF==1.18.9 pytesseract==0.3.7
# pip install PyPDF4==1.27.0 pyAesCrypt==6.0.0

from .imageutils import (
    calculate_ss_confidence,
    convert_img2bin,
    display_img,
    generate_ss_text,
    pix2np,
    save_file_content,
    save_page_content,
)


# COMMON
def is_valid_path(path):
    """
    Validates the path inputted and checks whether it is a file path or a folder path
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path):
        return path
    elif os.path.isdir(path):
        return path
    else:
        raise ValueError(f"Invalid Path {path}")

# HIGHLIGHT PDF
def extract_info(input_file: str):
    r"""
    https://www.thepythoncode.com/article/redact-and-highlight-text-in-pdf-with-python
    Extracts file info

    ## File Information ##################################################
    File:C:\Users\usef\Downloads\rkuhp30nov2022.pdf
    Encrypted:False
    format:PDF 1.7
    title:
    author:Microsoft Office User
    subject:
    keywords:
    creator:Microsoft« Word 2019
    producer:Microsoft« Word 2019
    creationDate:D:20221130141128+07'00'
    modDate:D:20221130141128+07'00'
    trapped:
    encryption:None
    ######################################################################
    """
    # Open the PDF
    pdfDoc = fitz.open(input_file)
    output = {
        "File": input_file,
        "Encrypted": ("True" if pdfDoc.isEncrypted else "False")
    }
    # If PDF is encrypted the file metadata cannot be extracted
    if not pdfDoc.isEncrypted:
        for key, value in pdfDoc.metadata.items():
            output[key] = value
    # To Display File Info
    print("## File Information ##################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in output.items()))
    print("######################################################################")
    return True, output

def search_for_text(lines, search_str):
    """
    Search for the search string within the document lines
    This function searches for a string within the document lines using the re.findall() function,
    re.IGNORECASE is to ignore the case while searching.
    """
    for line in lines:
        # Find all matches within one line
        results = re.findall(search_str, line, re.IGNORECASE)
        # In case multiple matches within one line
        for result in results:
            yield result

def redact_matching_data(page, matched_values):
    """
    Redacts matching values
    This function performs the following:
        Loop throughout the matching values of the search string we are searching for.
        Redact the matching values.
        Apply the redaction on the selected page.
    """
    matches_found = 0
    # Loop throughout matching values
    for val in matched_values:
        matches_found += 1
        matching_val_area = page.searchFor(val)
        # Redact matching values
        # You can change the color of the redaction using the fill argument on the page.addRedactAnnot() method, 
        # setting it to (0, 0, 0) will result in a black redaction. 
        # These are RGB values ranging from 0 to 1. For example, (1, 0, 0) will result in a red redaction, and so on.
        [page.addRedactAnnot(area, text=" ", fill=(0, 0, 0))
            for area in matching_val_area]
    # Apply the redaction
    page.apply_redactions()
    return matches_found

def frame_matching_data(page, matched_values):
    """
    frames matching values
    The frame_matching_data() function draws a red rectangle (frame) around the matching values.
    """
    matches_found = 0
    # Loop throughout matching values
    for val in matched_values:
        matches_found += 1
        matching_val_area = page.searchFor(val)
        for area in matching_val_area:
            if isinstance(area, fitz.fitz.Rect):
                # Draw a rectangle around matched values
                annot = page.addRectAnnot(area)
                # , fill = fitz.utils.getColor('black')
                annot.setColors(stroke=fitz.utils.getColor('red'))
                # If you want to remove matched data
                #page.addFreetextAnnot(area, ' ')
                annot.update()
    return matches_found

def highlight_matching_data(page, matched_values, type):
    """
    Highlight matching values
    define a function to highlight text
    The above function applies the adequate highlighting mode on the matching values depending on the type of highlight inputted as a parameter.
    """
    matches_found = 0
    # Loop throughout matching values
    for val in matched_values:
        matches_found += 1
        matching_val_area = page.searchFor(val)
        # print("matching_val_area",matching_val_area)
        highlight = None
        if type == 'Highlight':
            highlight = page.addHighlightAnnot(matching_val_area)
        elif type == 'Squiggly':
            highlight = page.addSquigglyAnnot(matching_val_area)
        elif type == 'Underline':
            highlight = page.addUnderlineAnnot(matching_val_area)
        elif type == 'Strikeout':
            highlight = page.addStrikeoutAnnot(matching_val_area)
        else:
            highlight = page.addHighlightAnnot(matching_val_area)
        # To change the highlight colar
        # highlight.setColors({"stroke":(0,0,1),"fill":(0.75,0.8,0.95) })
        # highlight.setColors(stroke = fitz.utils.getColor('white'), fill = fitz.utils.getColor('red'))
        # highlight.setColors(colors= fitz.utils.getColor('red'))
        highlight.update()
    return matches_found

def process_data(input_file: str, output_file: str, search_str: str, pages: Tuple = None, action: str = 'Highlight'):
    """
    Process the pages of the PDF File

    accepts several parameters:

    input_file: The path of the PDF file to process.
    output_file: The path of the PDF file to generate after processing.
    search_str: The string to search for.
    pages: The pages to consider while processing the PDF file.
    action: The action to perform on the PDF file.

    purpose of the process_data() function is the following:

    Open the input file.
    Create a memory buffer for storing temporarily the output file.
    Initialize a variable for storing the total number of matches of the string we were searching for.
    Iterate throughout the selected pages of the input file and split the current page into lines.
    Search for the string within the page.
    Apply the corresponding action (i.e "Redact", "Frame", "Highlight", etc.)
    Display a message signaling the status of the search process.
    Save and close the input file.
    Save the memory buffer to the output file.

    """
    # Open the PDF
    pdfDoc = fitz.open(input_file)
    # Save the generated PDF to memory buffer
    output_buffer = BytesIO()
    total_matches = 0
    # Iterate through pages
    for pg in range(pdfDoc.pageCount):
        # If required for specific pages
        if pages:
            if str(pg) not in pages:
                continue
        # Select the page
        page = pdfDoc[pg]
        # Get Matching Data
        # Split page by lines
        page_lines = page.getText("text").split('\n')
        matched_values = search_for_text(page_lines, search_str)
        if matched_values:
            if action == 'Redact':
                matches_found = redact_matching_data(page, matched_values)
            elif action == 'Frame':
                matches_found = frame_matching_data(page, matched_values)
            elif action in ('Highlight', 'Squiggly', 'Underline', 'Strikeout'):
                matches_found = highlight_matching_data(
                    page, matched_values, action)
            else:
                matches_found = highlight_matching_data(
                    page, matched_values, 'Highlight')
            total_matches += matches_found
    print(f"{total_matches} Match(es) Found of Search String {search_str} In Input File: {input_file}")
    # Save to output
    pdfDoc.save(output_buffer)
    pdfDoc.close()
    # Save the output buffer to the output file
    with open(output_file, mode='wb') as f:
        f.write(output_buffer.getbuffer())

def remove_highlght(input_file: str, output_file: str, pages: Tuple = None):
    """
    purpose of the remove_highlight() function is to remove the highlights (not the redactions) from a PDF file. It performs the following:

    Open the input file.
    Create a memory buffer for storing temporarily the output file.
    Iterate throughout the pages of the input file and checks if annotations are found.
    Delete these annotations.
    Display a message signaling the status of this process.
    Close the input file.
    Save the memory buffer to the output file.
    """
    # Open the PDF
    pdfDoc = fitz.open(input_file)
    # Save the generated PDF to memory buffer
    output_buffer = BytesIO()
    # Initialize a counter for annotations
    annot_found = 0
    # Iterate through pages
    for pg in range(pdfDoc.pageCount):
        # If required for specific pages
        if pages:
            if str(pg) not in pages:
                continue
        # Select the page
        page = pdfDoc[pg]
        annot = page.firstAnnot
        while annot:
            annot_found += 1
            page.deleteAnnot(annot)
            annot = annot.next
    if annot_found >= 0:
        print(f"Annotation(s) Found In The Input File: {input_file}")
    # Save to output
    pdfDoc.save(output_buffer)
    pdfDoc.close()
    # Save the output buffer to the output file
    with open(output_file, mode='wb') as f:
        f.write(output_buffer.getbuffer())

def process_file(**kwargs):
    """
    a wrapper function that uses previous functions to call the appropriate function depending on the action
    The action can be "Redact", "Frame", "Highlight", "Squiggly", "Underline", "Strikeout", and "Remove".

    To process one single file:
    Redact, Frame, Highlight... one PDF File
    Remove Highlights from a single PDF File
    """
    input_file = kwargs.get('input_file')
    output_file = kwargs.get('output_file')
    if output_file is None:
        output_file = input_file
    search_str = kwargs.get('search_str')
    pages = kwargs.get('pages')
    # Redact, Frame, Highlight, Squiggly, Underline, Strikeout, Remove
    action = kwargs.get('action')
    if action == "Remove":
        # Remove the Highlights except Redactions
        remove_highlght(input_file=input_file,
                        output_file=output_file, pages=pages)
    else:
        process_data(input_file=input_file, output_file=output_file,
                     search_str=search_str, pages=pages, action=action)

def process_folder(**kwargs):
    """
    This function is intended to process the PDF files included within a specific folder.
    It loops throughout the files of the specified folder either recursively or not depending on the value of the parameter recursive and process these files one by one.

    accepts the following parameters:

    input_folder: The path of the folder containing the PDF files to process.
    search_str: The text to search for in order to manipulate.
    recursive: whether to run this process recursively by looping across the subfolders or not.
    action: the action to perform among the list previously mentioned.
    pages: the pages to consider.

    Redact, Frame, Highlight... all PDF Files within a specified path
    Remove Highlights from all PDF Files within a specified path
    """
    input_folder = kwargs.get('input_folder')
    search_str = kwargs.get('search_str')
    # Run in recursive mode
    recursive = kwargs.get('recursive')
    #Redact, Frame, Highlight, Squiggly, Underline, Strikeout, Remove
    action = kwargs.get('action')
    pages = kwargs.get('pages')
    # Loop though the files within the input folder.
    for foldername, dirs, filenames in os.walk(input_folder):
        for filename in filenames:
            # Check if pdf file
            if not filename.endswith('.pdf'):
                continue
             # PDF File found
            inp_pdf_file = os.path.join(foldername, filename)
            print("Processing file =", inp_pdf_file)
            process_file(input_file=inp_pdf_file, output_file=None,
                         search_str=search_str, action=action, pages=pages)
        if not recursive:
            break

def parse_args_pdf_highlighter():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input_path', dest='input_path', type=is_valid_path,
                        required=True, help="Enter the path of the file or the folder to process")
    parser.add_argument('-a', '--action', dest='action', choices=['Redact', 'Frame', 'Highlight', 'Squiggly', 'Underline', 'Strikeout', 'Remove'], type=str,
                        default='Highlight', help="Choose whether to Redact or to Frame or to Highlight or to Squiggly or to Underline or to Strikeout or to Remove")
    parser.add_argument('-p', '--pages', dest='pages', type=tuple,
                        help="Enter the pages to consider e.g.: [2,4]")
    action = parser.parse_known_args()[0].action
    if action != 'Remove':
        parser.add_argument('-s', '--search_str', dest='search_str'                            # lambda x: os.path.has_valid_dir_syntax(x)
                            , type=str, required=True, help="Enter a valid search string")
    path = parser.parse_known_args()[0].input_path
    if os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file', type=str  # lambda x: os.path.has_valid_dir_syntax(x)
                            , help="Enter a valid output file")
    if os.path.isdir(path):
        parser.add_argument('-r', '--recursive', dest='recursive', default=False, type=lambda x: (
            str(x).lower() in ['true', '1', 'yes']), help="Process Recursively or Non-Recursively")
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

def pdf_highlighter():
    """
    $ python pdf_highlighter.py --help
    usage: pdf_highlighter.py [-h] -i INPUT_PATH [-a {Redact,Frame,Highlight,Squiggly,Underline,Strikeout,Remove}] [-p PAGES]

    Available Options

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_PATH, --input_path INPUT_PATH
                            Enter the path of the file or the folder to process
    -a {Redact,Frame,Highlight,Squiggly,Underline,Strikeout,Remove}, --action {Redact,Frame,Highlight,Squiggly,Underline,Strikeout,Remove}
                            Choose whether to Redact or to Frame or to Highlight or to Squiggly or to Underline or to Strikeout or to Remove
    -p PAGES, --pages PAGES
                            Enter the pages to consider e.g.: [2,4]

    Before exploring our test scenarios, let me clarify few points:

        To avoid encountering the PermissionError, please close the input PDF file before running this utility.
        The input PDF file to process must not be a scanned PDF file.
        The search string complies with the rules of regular expressions using Python's built-in re module. For example, setting the search string to "organi[sz]e" match both "organise" and "organize".

    As a demonstration example, let’s highlight the word "BERT" in the BERT paper:

    $ python pdf_highlighter.py -i bert-paper.pdf -a Highlight -s "BERT"

    $ python pdf_highlighter.py -i bert-paper.pdf -a Remove
    """
    # Parsing command line arguments entered by user
    args = parse_args_pdf_highlighter()
    # If File Path
    if os.path.isfile(args['input_path']):
        # Extracting File Info
        extract_info(input_file=args['input_path'])
        # Process a file
        process_file(
            input_file=args['input_path'], output_file=args['output_file'], 
            search_str=args['search_str'] if 'search_str' in (args.keys()) else None, 
            pages=args['pages'], action=args['action']
        )
    # If Folder Path
    elif os.path.isdir(args['input_path']):
        # Process a folder
        process_folder(
            input_folder=args['input_path'], 
            search_str=args['search_str'] if 'search_str' in (args.keys()) else None, 
            action=args['action'],
            pages=args['pages'],
            recursive=args['recursive']
        )

# PDF/IMAGE OCR
def ocr_img(
        img: np.array, input_file: str, search_str: str, 
        highlight_readable_text: bool = False, action: str = 'Highlight', 
        show_comparison: bool = False, generate_output: bool = True):
    """Scans an image buffer or an image file.
    Pre-processes the image.
    Calls the Tesseract engine with pre-defined parameters.
    Calculates the confidence score of the image grabbed content.
    Draws a green rectangle around readable text items having a confidence score > 30.
    Searches for a specific text.
    Highlight or redact found matches of the searched text.
    Displays a window showing readable text fields or the highlighted or redacted text.
    Generates the text content of the image.
    Prints a summary to the console.
    
    The above performs the following:

        Scans an image buffer or an image file.
        Pre-processes the image.
        Runs the Tesseract engine with pre-defined parameters.
        Calculates the confidence score of the grabbed content of the image.
        Draws a green rectangle around the readable text items having a confidence score greater than 30.
        Searches for a specific text within the image grabbed content.
        Highlights or redacts the found matches of the searched text.
        Displays a window showing readable text fields or the highlighted text or the redacted text.
        Generates the text content of the image.
        Prints a summary to the console.

    """
    # If image source file is inputted as a parameter
    if input_file:
        # Reading image using opencv
        img = cv2.imread(input_file)
    # Preserve a copy of this image for comparison purposes
    initial_img = img.copy()
    highlighted_img = img.copy()
    # Convert image to binary
    bin_img = convert_img2bin(img)
    # Calling Tesseract
    # Tesseract Configuration parameters
    # oem --> OCR engine mode = 3 >> Legacy + LSTM mode only (LSTM neutral net mode works the best)
    # psm --> page segmentation mode = 6 >> Assume as single uniform block of text (How a page of text can be analyzed)
    config_param = r'--oem 3 --psm 6'
    # Feeding image to tesseract
    details = pytesseract.image_to_data(
        bin_img, output_type=Output.DICT, config=config_param, lang='eng')
    # The details dictionary contains the information of the input image
    # such as detected text, region, position, information, height, width, confidence score.
    ss_confidence = calculate_ss_confidence(details)
    boxed_img = None
    # Total readable items
    ss_readable_items = 0
    # Total matches found
    ss_matches = 0
    for seq in range(len(details['text'])):
        # Consider only text fields with confidence score > 30 (text is readable)
        if float(details['conf'][seq]) > 30.0:
            ss_readable_items += 1
            # Draws a green rectangle around readable text items having a confidence score > 30
            if highlight_readable_text:
                (x, y, w, h) = (details['left'][seq], details['top']
                                [seq], details['width'][seq], details['height'][seq])
                boxed_img = cv2.rectangle(
                    img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Searches for the string
            if search_str:
                results = re.findall(
                    search_str, details['text'][seq], re.IGNORECASE)
                for result in results:
                    ss_matches += 1
                    if action:
                        # Draw a red rectangle around the searchable text
                        (x, y, w, h) = (details['left'][seq], details['top']
                                        [seq], details['width'][seq], details['height'][seq])
                        # Details of the rectangle
                        # Starting coordinate representing the top left corner of the rectangle
                        start_point = (x, y)
                        # Ending coordinate representing the botton right corner of the rectangle
                        end_point = (x + w, y + h)
                        #Color in BGR -- Blue, Green, Red
                        if action == "Highlight":
                            color = (0, 255, 255)  # Yellow
                        elif action == "Redact":
                            color = (0, 0, 0)  # Black
                        # Thickness in px (-1 will fill the entire shape)
                        thickness = -1
                        boxed_img = cv2.rectangle(
                            img, start_point, end_point, color, thickness)
                            
    if ss_readable_items > 0 and highlight_readable_text and not (ss_matches > 0 and action in ("Highlight", "Redact")):
        highlighted_img = boxed_img.copy()
    # Highlight found matches of the search string
    if ss_matches > 0 and action == "Highlight":
        cv2.addWeighted(boxed_img, 0.4, highlighted_img,
                        1 - 0.4, 0, highlighted_img)
    # Redact found matches of the search string
    elif ss_matches > 0 and action == "Redact":
        highlighted_img = boxed_img.copy()
        #cv2.addWeighted(boxed_img, 1, highlighted_img, 0, 0, highlighted_img)
    # save the image
    cv2.imwrite("highlighted-text-image.jpg", highlighted_img)  
    # Displays window showing readable text fields or the highlighted or redacted data
    if show_comparison and (highlight_readable_text or action):
        title = input_file if input_file else 'Compare'
        conc_img = cv2.hconcat([initial_img, highlighted_img])
        display_img(title, conc_img)
    # Generates the text content of the image
    output_data = None
    if generate_output and details:
        output_data = generate_ss_text(details)
    # Prints a summary to the console
    if input_file:
        summary = {
            "File": input_file, "Total readable words": ss_readable_items, "Total matches": ss_matches, "Confidence score": ss_confidence
        }
        # Printing Summary
        print("## Summary ########################################################")
        print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
        print("###################################################################")
    return highlighted_img, ss_readable_items, ss_matches, ss_confidence, output_data
    # pass image into pytesseract module
    # pytesseract is trained in many languages
    #config_param = r'--oem 3 --psm 6'
    #details = pytesseract.image_to_data(img,config=config_param,lang='eng')
    # print(details)
    # return details

def image_to_byte_array(image: Image):
    """
    Converts an image into a byte array
    """
    imgByteArr = BytesIO()
    image.save(imgByteArr, format=image.format if image.format else 'JPEG')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

def ocr_file(**kwargs):
    """Opens the input PDF File.
    Opens a memory buffer for storing the output PDF file.
    Creates a DataFrame for storing pages statistics
    Iterates throughout the chosen pages of the input PDF file
    Grabs a screen-shot of the selected PDF page.
    Converts the screen-shot pix to a numpy array
    Scans the grabbed screen-shot.
    Collects the statistics of the screen-shot(page).
    Saves the content of the screen-shot(page).
    Adds the updated screen-shot (Highlighted, Redacted) to the output file.
    Saves the whole content of the PDF file.
    Saves the output PDF file if required.
    Prints a summary to the console.

    The ocr_file() function does the following:

        Opens the input PDF file.
        Opens a memory buffer for storing the output PDF file.
        Creates a pandas dataframe for storing the page's statistics.
        Iterates through the chosen pages of the input PDF file.
        Grabs a screenshot (image) of the selected page of the input PDF file.
        Converts the screenshot (pix) to a NumPy array.
        Scans the grabbed screen-shot.
        Collects the statistics of the screen-shot (page).
        Saves the content of the screenshot.
        Adds the updated screenshot to the output file.
        Saves the whole content of the input PDF file to a CSV file.
        Saves the output PDF file if required.
        Prints a summary to the console.
    """
    input_file = kwargs.get('input_file')
    output_file = kwargs.get('output_file')
    search_str = kwargs.get('search_str')
    pages = kwargs.get('pages')
    highlight_readable_text = kwargs.get('highlight_readable_text')
    action = kwargs.get('action')
    show_comparison = kwargs.get('show_comparison')
    generate_output = kwargs.get('generate_output')
    # Opens the input PDF file
    pdfIn = fitz.open(input_file)
    # Opens a memory buffer for storing the output PDF file.
    pdfOut = fitz.open()
    # Creates an empty DataFrame for storing pages statistics
    dfResult = pd.DataFrame(
        columns=['page', 'page_readable_items', 'page_matches', 'page_total_confidence'])
    # Creates an empty DataFrame for storing file content
    if generate_output:
        pdfContent = pd.DataFrame(columns=['page', 'line_id', 'line'])
    # Iterate throughout the pages of the input file
    for pg in range(pdfIn.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        # Select a page
        page = pdfIn[pg]
        # Rotation angle
        rotate = int(0)
        # PDF Page is converted into a whole picture 1056*816 and then for each picture a screenshot is taken.
        # zoom = 1.33333333 -----> Image size = 1056*816
        # zoom = 2 ---> 2 * Default Resolution (text is clear, image text is hard to read)    = filesize small / Image size = 1584*1224
        # zoom = 4 ---> 4 * Default Resolution (text is clear, image text is barely readable) = filesize large
        # zoom = 8 ---> 8 * Default Resolution (text is clear, image text is readable) = filesize large
        zoom_x = 2
        zoom_y = 2
        # The zoom factor is equal to 2 in order to make text clear
        # Pre-rotate is to rotate if needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        # To captue a specific part of the PDF page
        # rect = page.rect #page size
        # mp = rect.tl + (rect.bl - (0.75)/zoom_x) #rectangular area 56 = 75/1.3333
        # clip = fitz.Rect(mp,rect.br) #The area to capture
        # pix = page.getPixmap(matrix=mat, alpha=False,clip=clip)
        # Get a screen-shot of the PDF page
        # Colorspace -> represents the color space of the pixmap (csRGB, csGRAY, csCMYK)
        # alpha -> Transparancy indicator
        pix = page.getPixmap(matrix=mat, alpha=False, colorspace="csGRAY")
        # convert the screen-shot pix to numpy array
        img = pix2np(pix)
        # Erode image to omit or thin the boundaries of the bright area of the image
        # We apply Erosion on binary images.
        #kernel = np.ones((2,2) , np.uint8)
        #img = cv2.erode(img,kernel,iterations=1)
        upd_np_array, pg_readable_items, pg_matches, pg_total_confidence, pg_output_data \
            = ocr_img(img=img, input_file=None, search_str=search_str, highlight_readable_text=highlight_readable_text  # False
                      , action=action  # 'Redact'
                      , show_comparison=show_comparison  # True
                      , generate_output=generate_output  # False
                      )
        # Collects the statistics of the page
        dfResult = dfResult.append({'page': (pg+1), 'page_readable_items': pg_readable_items,
                                   'page_matches': pg_matches, 'page_total_confidence': pg_total_confidence}, ignore_index=True)
        if generate_output:
            pdfContent = save_page_content(
                pdfContent=pdfContent, page_id=(pg+1), page_data=pg_output_data)
        # Convert the numpy array to image object with mode = RGB
        #upd_img = Image.fromarray(np.uint8(upd_np_array)).convert('RGB')
        upd_img = Image.fromarray(upd_np_array[..., ::-1])
        # Convert the image to byte array
        upd_array = image_to_byte_array(upd_img)
        # Get Page Size
        """
        #To check whether initial page is portrait or landscape
        if page.rect.width > page.rect.height:
            fmt = fitz.PaperRect("a4-1")
        else:
            fmt = fitz.PaperRect("a4")

        #pno = -1 -> Insert after last page
        pageo = pdfOut.newPage(pno = -1, width = fmt.width, height = fmt.height)
        """
        pageo = pdfOut.newPage(
            pno=-1, width=page.rect.width, height=page.rect.height)
        pageo.insertImage(page.rect, stream=upd_array)
        #pageo.insertImage(page.rect, stream=upd_img.tobytes())
        #pageo.showPDFpage(pageo.rect, pdfDoc, page.number)
    content_file = None
    if generate_output:
        content_file = save_file_content(
            pdfContent=pdfContent, input_file=input_file)
    summary = {
        "File": input_file, "Total pages": pdfIn.pageCount, 
        "Processed pages": dfResult['page'].count(), "Total readable words": dfResult['page_readable_items'].sum(), 
        "Total matches": dfResult['page_matches'].sum(), "Confidence score": dfResult['page_total_confidence'].mean(), 
        "Output file": output_file, "Content file": content_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("\nPages Statistics:")
    print(dfResult, sep='\n')
    print("###################################################################")
    pdfIn.close()
    if output_file:
        pdfOut.save(output_file)
    pdfOut.close()

def ocr_folder(**kwargs):
    """Scans all PDF Files within a specified path
    
    function for processing a folder that contains multiple PDF files

    This function is intended to scan the PDF files included within a specific folder. It loops throughout the files of the specified folder either recursively or not depending on the value of the parameter recursive and processes these files one by one.

    It accepts the following parameters:

        input_folder: The path of the folder containing the PDF files to process.
        search_str: The text to search for to manipulate.
        recursive: whether to run this process recursively by looping across the subfolders or not.
        action: the action to perform among the following: Highlight, Redact.
        pages: the pages to consider.
        generate_output: select whether to save the content of the input PDF file to a CSV file or not

    """
    input_folder = kwargs.get('input_folder')
    # Run in recursive mode
    recursive = kwargs.get('recursive')
    search_str = kwargs.get('search_str')
    pages = kwargs.get('pages')
    action = kwargs.get('action')
    generate_output = kwargs.get('generate_output')
    # Loop though the files within the input folder.
    for foldername, dirs, filenames in os.walk(input_folder):
        for filename in filenames:
            # Check if pdf file
            if not filename.endswith('.pdf'):
                continue
            # PDF File found
            inp_pdf_file = os.path.join(foldername, filename)
            print("Processing file =", inp_pdf_file)
            output_file = None
            if search_str:
                # Generate an output file
                output_file = os.path.join(os.path.dirname(
                    inp_pdf_file), 'ocr_' + os.path.basename(inp_pdf_file))
            ocr_file(
                input_file=inp_pdf_file, output_file=output_file, search_str=search_str, pages=pages, highlight_readable_text=False, action=action, show_comparison=False, generate_output=generate_output
            )
        if not recursive:
            break

def is_valid_path(path):
    """Validates the path inputted and checks whether it is a file path or a folder path"""
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path):
        return path
    elif os.path.isdir(path):
        return path
    else:
        raise ValueError(f"Invalid Path {path}")

def parse_args_pdf_ocr():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input-path', type=is_valid_path,
                        required=True, help="Enter the path of the file or the folder to process")
    parser.add_argument('-a', '--action', choices=[
                        'Highlight', 'Redact'], type=str, help="Choose to highlight or to redact")
    parser.add_argument('-s', '--search-str', dest='search_str',
                        type=str, help="Enter a valid search string")
    parser.add_argument('-p', '--pages', dest='pages', type=tuple,
                        help="Enter the pages to consider in the PDF file, e.g. (0,1)")
    parser.add_argument("-g", "--generate-output", action="store_true", help="Generate text content in a CSV file")
    path = parser.parse_known_args()[0].input_path
    if os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file',
                            type=str, help="Enter a valid output file")
        parser.add_argument("-t", "--highlight-readable-text", action="store_true", help="Highlight readable text in the generated image")
        parser.add_argument("-c", "--show-comparison", action="store_true", help="Show comparison between captured image and the generated image")
    if os.path.isdir(path):
        parser.add_argument("-r", "--recursive", action="store_true", help="Whether to process the directory recursively")
    # To Porse The Command Line Arguments
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

def pdf_ocr():
    """
    $ python pdf_ocr.py -s "BERT" -a Highlight -i example-image-containing-text.jpg
    $ python pdf_ocr.py -s "BERT" -i image.pdf -o output.pdf --generate-output -a "Highlight"
    $ python pdf_ocr.py
    usage: pdf_ocr.py [-h] -i INPUT_PATH [-a {Highlight,Redact}] [-s SEARCH_STR] [-p PAGES] [-g GENERATE_OUTPUT]

    Available Options

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_PATH, --input_path INPUT_PATH
                            Enter the path of the file or the folder to process
    -a {Highlight,Redact}, --action {Highlight,Redact}
                            Choose to highlight or to redact
    -s SEARCH_STR, --search_str SEARCH_STR
                            Enter a valid search string
    -p PAGES, --pages PAGES
                            Enter the pages to consider e.g.: (0,1)
    -g GENERATE_OUTPUT, --generate_output GENERATE_OUTPUT
                            Generate content in a CSV file
    """
    # Parsing command line arguments entered by user
    args = parse_args_pdf_ocr()
    # If File Path
    if os.path.isfile(args['input_path']):
        # Process a file
        if filetype.is_image(args['input_path']):
            ocr_img(
                # if 'search_str' in (args.keys()) else None
                img=None, input_file=args['input_path'], search_str=args['search_str'], highlight_readable_text=args['highlight_readable_text'], action=args['action'], show_comparison=args['show_comparison'], generate_output=args['generate_output']
            )
        else:
            ocr_file(
                input_file=args['input_path'], output_file=args['output_file'], search_str=args['search_str'] if 'search_str' in (args.keys()) else None, pages=args['pages'], highlight_readable_text=args['highlight_readable_text'], action=args['action'], show_comparison=args['show_comparison'], generate_output=args['generate_output']
            )
    # If Folder Path
    elif os.path.isdir(args['input_path']):
        # Process a folder
        ocr_folder(
            input_folder=args['input_path'],
            recursive=args['recursive'],
            search_str=args['search_str'] if 'search_str' in (args.keys()) else None,
            pages=args['pages'],
            action=args['action'],
            generate_output=args['generate_output']
        )

# PDF TEXT EXTRACT
# https://www.thepythoncode.com/article/extract-text-from-pdf-in-python

def get_arguments():
    """
    Since we're going to make a Python script that extracts text from PDF documents,
    we have to use the argparse module to parse the passed parameters in the command line.
    The following function parses the arguments and does some processing:

    First, we made our parser using ArgumentParserAnd add the following parameters:
    
    file: The input PDF document to extract text from.
    -p or --pages: The page indices to extract, starting from 0, if you do not specify, the default will be all pages.
    -o or --output-file: The output text file to write the extracted text. If you do not specify, the content will be printed in the standard output (i.e., in the console).
    -b or --by-page: This is a boolean indicating whether to output text by page. If not specified, all text is joined in a single file (when -o is specified).

    Second, we open our output_files to write into if -b is specified. Otherwise, a single file will be in the output_files dictionary.

    Finally, we return the necessary variables: PDF document, output files, and the list of page numbers.
    """
    parser = argparse.ArgumentParser(
        description="A Python script to extract text from PDF documents.")
    parser.add_argument("file", help="Input PDF file")
    parser.add_argument("-p", "--pages", nargs="*", type=int,
                        help="The pages to extract, default is all")
    parser.add_argument("-o", "--output-file", default=sys.stdout,
                        help="Output file to write text. default is standard output")
    parser.add_argument("-b", "--by-page", action="store_true",
                        help="Whether to output text by page. If not specified, all text is joined and will be written together")
    # parse the arguments from the command-line
    args = parser.parse_args()

    input_file = args.file
    pages = args.pages
    by_page = args.by_page
    output_file = args.output_file
    # print the arguments, just for logging purposes
    pprint(vars(args))
    # load the pdf file
    pdf = fitz.open(input_file)
    if not pages:
        # if pages is not set, default is all pages of the input PDF document
        pages = list(range(pdf.pageCount))
    # we make our dictionary that maps each pdf page to its corresponding file
    # based on passed arguments
    if by_page:
        if output_file is not sys.stdout:
            # if by_page and output_file are set, open all those files
            file_name, ext = os.path.splitext(output_file)
            output_files = { pn: open(f"{file_name}-{pn}{ext}", "w") for pn in pages }
        else:
            # if output file is standard output, do not open
            output_files = { pn: output_file for pn in pages }
    else:
        if output_file is not sys.stdout:
            # a single file, open it
            output_file = open(output_file, "w")
            output_files = { pn: output_file for pn in pages }
        else:
            # if output file is standard output, do not open
            output_files = { pn: output_file for pn in pages }

    # return the parsed and processed arguments
    return {
        "pdf": pdf,
        "output_files": output_files,
        "pages": pages,
    }

def extract_text(**kwargs):
    """
    make a function that accepts the above parameters and extract text from PDF documents accordingly:
    We iterate over the pages; if the page we're in is in the pages list,
    we extract the text of that page and write it to the specified file or standard output.
    Finally, we close the files.
    """
    # extract the arguments
    pdf          = kwargs.get("pdf")
    output_files = kwargs.get("output_files")
    pages        = kwargs.get("pages")
    # iterate over pages
    for pg in range(pdf.pageCount):
        if pg in pages:
            # get the page object
            page = pdf[pg]
            # extract the text of that page and split by new lines '\n'
            page_lines = page.get_text().splitlines()
            # get the output file
            file = output_files[pg]
            # get the number of lines
            n_lines = len(page_lines)
            for line in page_lines:
                # remove any whitespaces in the end & beginning of the line
                line = line.strip()
                # print the line to the file/stdout
                print(line, file=file)
            print(f"[*] Wrote {n_lines} lines in page {pg}")    
    # close the files
    for pn, f in output_files.items():
        if f is not sys.stdout:
            f.close()

def extract_text_from_pdf():
    """
    $ python extract_text_from_pdf.py bert-paper.pdf -o text.txt -b
    $ python extract_text_from_pdf.py bert-paper.pdf -o text.txt -b -p 0 1 2 14 15
    We can also print in the console instead of saving it to a file by not setting the -o option
    $ python extract_text_from_pdf.py bert-paper.pdf -p 0
    Or saving all the text of the PDF document into a single text file:
    $ python extract_text_from_pdf.py bert-paper.pdf -o all-text.txt
    """
    # get the arguments
    kwargs = get_arguments()
    # extract text from the pdf document
    extract_text(**kwargs)

# more
# /l)https://www.thepythoncode.com/article/sign-pdf-files-in-python
# $ pip install PDFNetPython3==8.1.0 pyOpenSSL==20.0.1
# Import Libraries
import OpenSSL
import os
import time
import argparse
from PDFNetPython3.PDFNetPython import *
from typing import Tuple


def createKeyPair(type, bits):
    """
    Create a public/private key pair
    Arguments: Type - Key Type, must be one of TYPE_RSA and TYPE_DSA
               bits - Number of bits to use in the key (1024 or 2048 or 4096)
    Returns: The public/private key pair in a PKey object

    The above function creates a public/private key pair to use when generating the self-signed certificate in order to perform asymmetric encryption.
    """
    pkey = OpenSSL.crypto.PKey()
    pkey.generate_key(type, bits)
    return pkey

def create_self_signed_cert(pKey):
    """
    Create a self signed certificate. This certificate will not require to be signed by a Certificate Authority.
    This function creates a self-signed certificate that does not require to be signed by a certificate authority.

    This function will assign the following attributes to the certificate:

        Common Name: BASSEM MARJI.
        Serial Number: a random number depending on the time function.
        Not After: Expiry after 10 years.

    """
    # Create a self signed certificate
    cert = OpenSSL.crypto.X509()
    # Common Name (e.g. server FQDN or Your Name)
    cert.get_subject().CN = "BASSEM MARJI"
    # Serial Number
    cert.set_serial_number(int(time.time() * 10))
    # Not Before
    cert.gmtime_adj_notBefore(0)  # Not before
    # Not After (Expire after 10 years)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    # Identify issue
    cert.set_issuer((cert.get_subject()))
    cert.set_pubkey(pKey)
    cert.sign(pKey, 'md5')  # or cert.sign(pKey, 'sha256')
    return cert

def load():
    """
    Generate the certificate
    a function that uses both functions to generate a certificate:
    This function performs the following:

    Creates a public/private key pair.
    Stores the private key within the file "private_key.pem" under the static folder.
    Generates a self-signed certificate and saves it to the file "certificate.cer" under the static folder.
    Saves the public key in the file "public_key.pem" under the static folder.
    Produces a container file "container.pfx" combining the private key and the certificate and places it under the static folder.

    Note that the private key should not be printed in the console. However, it is included in the summary dictionary (that will be printed) for demonstration purposes, make sure you remove the private key from the console output if you're serious about this.
    """
    summary = {}
    summary['OpenSSL Version'] = OpenSSL.__version__
    # Generating a Private Key...
    key = createKeyPair(OpenSSL.crypto.TYPE_RSA, 1024)
    # PEM encoded
    with open('.\static\private_key.pem', 'wb') as pk:
        pk_str = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)
        pk.write(pk_str)
        summary['Private Key'] = pk_str
    # Done - Generating a private key...
    # Generating a self-signed client certification...
    cert = create_self_signed_cert(pKey=key)
    with open('.\static\certificate.cer', 'wb') as cer:
        cer_str = OpenSSL.crypto.dump_certificate(
            OpenSSL.crypto.FILETYPE_PEM, cert)
        cer.write(cer_str)
        summary['Self Signed Certificate'] = cer_str
    # Done - Generating a self-signed client certification...
    # Generating the public key...
    with open('.\static\public_key.pem', 'wb') as pub_key:
        pub_key_str = OpenSSL.crypto.dump_publickey(
            OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey())
        #print("Public key = ",pub_key_str)
        pub_key.write(pub_key_str)
        summary['Public Key'] = pub_key_str
    # Done - Generating the public key...
    # Take a private key and a certificate and combine them into a PKCS12 file.
    # Generating a container file of the private key and the certificate...
    p12 = OpenSSL.crypto.PKCS12()
    p12.set_privatekey(key)
    p12.set_certificate(cert)
    open('.\static\container.pfx', 'wb').write(p12.export())
    # You may convert a PKSC12 file (.pfx) to a PEM format
    # Done - Generating a container file of the private key and the certificate...
    # To Display A Summary
    print("## Initialization Summary ##################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("############################################################################")
    return True

def sign_file(input_file: str, signatureID: str, x_coordinate: int, 
            y_coordinate: int, pages: Tuple = None, output_file: str = None
              ):
    """
    Sign a PDF file
    a function to sign a PDF file:

    The sign_file() function performs the following:

    Iterates across the pages of the input PDF file.
    Inserts a signature widget to the chosen pages of this file on a specific location.
    Adds the signature image and signs the file using the self-signed certificate.

    Make sure you have the certificates under the static folder (we'll see how to generate this later).
    """
    # An output file is automatically generated with the word signed added at its end
    if not output_file:
        output_file = (os.path.splitext(input_file)[0]) + "_signed.pdf"
    # Initialize the library
    PDFNet.Initialize()
    doc = PDFDoc(input_file)
    # Create a signature field
    sigField = SignatureWidget.Create(doc, Rect(
        x_coordinate, y_coordinate, x_coordinate+100, y_coordinate+50), signatureID)
    # Iterate throughout document pages
    for page in range(1, (doc.GetPageCount() + 1)):
        # If required for specific pages
        if pages:
            if str(page) not in pages:
                continue
        pg = doc.GetPage(page)
        # Create a signature text field and push it on the page
        pg.AnnotPushBack(sigField)
    # Signature image
    sign_filename = os.path.dirname(
        os.path.abspath(__file__)) + "\static\signature.jpg"
    # Self signed certificate
    pk_filename = os.path.dirname(
        os.path.abspath(__file__)) + "\static\container.pfx"
    # Retrieve the signature field.
    approval_field = doc.GetField(signatureID)
    approval_signature_digsig_field = DigitalSignatureField(approval_field)
    # Add appearance to the signature field.
    img = Image.Create(doc.GetSDFDoc(), sign_filename)
    found_approval_signature_widget = SignatureWidget(
        approval_field.GetSDFObj())
    found_approval_signature_widget.CreateSignatureAppearance(img)
    # Prepare the signature and signature handler for signing.
    approval_signature_digsig_field.SignOnNextSave(pk_filename, '')
    # The signing will be done during the following incremental save operation.
    doc.Save(output_file, SDFDoc.e_incremental)
    # Develop a Process Summary
    summary = {
        "Input File": input_file, "Signature ID": signatureID, 
        "Output File": output_file, "Signature File": sign_filename, 
        "Certificate File": pk_filename
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return True

def sign_folder(**kwargs):
    """
    Sign all PDF Files within a specified path
    
    for signing all PDF files within a specific folder:

    This function is targeted to sign the PDF files of a specific folder.

    It loops throughout the files of the specified folder either recursively or not depending on the value of the recursive parameter and processes these files one by one. It accepts the following parameters:

        input_folder: The path of the folder containing the PDF files to process.
        signatureID: The identifier of the signature widget to create.
        x_coordinate and y_coordinate: The coordinates indicating the location of the signature. 
        pages: The range of the pages to sign.
        recursive: whether to run this process recursively by looping across the subfolders or not.

    """
    input_folder = kwargs.get('input_folder')
    signatureID = kwargs.get('signatureID')
    pages = kwargs.get('pages')
    x_coordinate = int(kwargs.get('x_coordinate'))
    y_coordinate = int(kwargs.get('y_coordinate'))
    # Run in recursive mode
    recursive = kwargs.get('recursive')
    # Loop though the files within the input folder.
    for foldername, dirs, filenames in os.walk(input_folder):
        for filename in filenames:
            # Check if pdf file
            if not filename.endswith('.pdf'):
                continue
            # PDF File found
            inp_pdf_file = os.path.join(foldername, filename)
            print("Processing file =", inp_pdf_file)
            # Compress Existing file
            sign_file(input_file=inp_pdf_file, signatureID=signatureID, x_coordinate=x_coordinate,
                      y_coordinate=y_coordinate, pages=pages, output_file=None)
        if not recursive:
            break

# def is_valid_path(path):
#     """Validates the path inputted and checks whether it is a file path or a folder path"""
#     if not path:
#         raise ValueError(f"Invalid Path")
#     if os.path.isfile(path):
#         return path
#     elif os.path.isdir(path):
#         return path
#     else:
#         raise ValueError(f"Invalid Path {path}")


def parse_args_signing_pdf():
    """
    Get user command line parameters
    The parse_args() function defines and sets the appropriate constraints for the command line arguments to be specified by the user when running this utility.

    I will describe hereafter the defined arguments:

        --load or -l: Initialize the configuration settings by generating a self-signed certificate. This step should be executed once or on a need basis.
        --input_path or -i: Used to input the path of the file or the folder to process, this parameter is associated with the is_valid_path() function that is previously defined.
        --signatureID or -s: The identifier to assign to the signature widget. (in case multiple signees need to sign off the same PDF document).
        --pages or -p: The pages to sign off.
        --x_coordinate or -x and --y_coordinate or -y: Specifies the location of the signature on the page.
        --output_file or -o: The path of the output file. Filling in this argument is constrained by the selection of a file as input, not a directory.
        --recursive or -r: Whether to process a folder recursively or not.  Filling in this argument is constrained by the selection of a directory. 

    """
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-l', '--load', dest='load', action="store_true",
                        help="Load the required configurations and create the certificate")
    parser.add_argument('-i', '--input_path', dest='input_path', type=is_valid_path,
                        help="Enter the path of the file or the folder to process")
    parser.add_argument('-s', '--signatureID', dest='signatureID',
                        type=str, help="Enter the ID of the signature")
    parser.add_argument('-p', '--pages', dest='pages', type=tuple,
                        help="Enter the pages to consider e.g.: [1,3]")
    parser.add_argument('-x', '--x_coordinate', dest='x_coordinate',
                        type=int, help="Enter the x coordinate.")
    parser.add_argument('-y', '--y_coordinate', dest='y_coordinate',
                        type=int, help="Enter the y coordinate.")
    path = parser.parse_known_args()[0].input_path
    if path and os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file',
                            type=str, help="Enter a valid output file")
    if path and os.path.isdir(path):
        parser.add_argument('-r', '--recursive', dest='recursive', default=False, type=lambda x: (
            str(x).lower() in ['true', '1', 'yes']), help="Process Recursively or Non-Recursively")
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

def main_signing_pdf():
    """
    python sign_pdf.py --help
    $ python sign_pdf.py --load
    private and public keys were successfully generated, as well as the certificate. Again, as noted earlier. If you're using this code, you should exclude the private key from the summary dictionary so it won't be printed to the console.

    Now let’s sign the document entitled "Letter of confirmation.pdf" placed under the static folder:
    $ python sign_pdf.py -i ".\static\Letter of confirmation.pdf" -s "BM" -x 330 -y 280
    You can also specify the -p option to sign multiple pages within a PDF file, something like:

    $ python sign_pdf.py -i pdf_file.pdf -s "BM" -x 330 -y 300 -p [1, 3]

    Or signing multiple PDF files included within a folder:

    $ python sign_pdf.py -i pdf-files-folder -s "BM" -p [1] -x 330 -y 300 -r 0

    Digitally signing documents saves time, reduces the need for paper-driven processes, and offers you the flexibility to approve a document from almost anywhere.
    https://www.thepythoncode.com/code/sign-pdf-files-in-python
    """
    # Parsing command line arguments entered by user
    args = parse_args_signing_pdf()
    if args['load'] == True:
        load()
    else:
        # If File Path
        if os.path.isfile(args['input_path']):
            sign_file(
                input_file=args['input_path'], signatureID=args['signatureID'],
                x_coordinate=int(args['x_coordinate']), y_coordinate=int(args['y_coordinate']), 
                pages=args['pages'], output_file=args['output_file']
            )
        # If Folder Path
        elif os.path.isdir(args['input_path']):
            # Process a folder
            sign_folder(
                input_folder=args['input_path'], signatureID=args['signatureID'], 
                x_coordinate=int(args['x_coordinate']), y_coordinate=int(args['y_coordinate']),
                pages=args['pages'], recursive=args['recursive']
            )
# https://www.thepythoncode.com/article/split-pdf-files-in-python
# $ pip install pikepdf
import os
from pikepdf import Pdf

# split our PDF file into 3 new PDF documents, 
# the first contains the first 9 pages, from 0 to 9 (while 9 is not included).
# The second file will contain the pages from 9 (included) to 11,
# and the last file will contain the page range from 11 until the end or until reaching page 100 if it exists.
# a dictionary mapping PDF file to original PDF's page range

# If you want to split each page into a new PDF document, 
# you can simply replace [0, 9] to [0], 
# so it'll be a list of one element and that is the first page, and so on.
file2pages = {
    0: [0, 9], # 1st splitted PDF file will contain the pages from 0 to 9 (9 is not included)
    1: [9, 11], # 2nd splitted PDF file will contain the pages from 9 (9 is included) to 11
    2: [11, 100], # 3rd splitted PDF file will contain the pages from 11 until the end or until the 100th page (if exists)
}
def split_pdf(filename = "bert-paper.pdf"):
    """
    To make a new PDF file, you simply call the Pdf.new() method.
    The new_pdf_index variable is the index of the file,
    it will only be incremented when we're done with making the previous file.

    First, we iterate over all the PDF files using the pdf.pages attribute.
    If the page index is in the file page range in the file2pages dictionary,
    then we simply add the page into our new file. Otherwise,
    then we know we're done with the previous file,
    and it is time to save it to the disk using save() method,
    and we continue the loop until all pages are assigned to their files.
    And then finally, we save the last file outside the loop.
    """
    # the target PDF document to split
    
    # load the PDF file
    pdf = Pdf.open(filename)
    # make the new splitted PDF files
    new_pdf_files = [ Pdf.new() for i in file2pages ]
    # the current pdf file index
    new_pdf_index = 0
    # iterate over all PDF pages
    for n, page in enumerate(pdf.pages):
        if n in list(range(*file2pages[new_pdf_index])):
            # add the `n` page to the `new_pdf_index` file
            new_pdf_files[new_pdf_index].pages.append(page)
            print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
        else:
            # make a unique filename based on original file name plus the index
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}-{new_pdf_index}.pdf"
            # save the PDF file
            new_pdf_files[new_pdf_index].save(output_filename)
            print(f"[+] File: {output_filename} saved.")
            # go to the next file
            new_pdf_index += 1
            # add the `n` page to the `new_pdf_index` file
            new_pdf_files[new_pdf_index].pages.append(page)
            print(f"[*] Assigning Page {n} to the file {new_pdf_index}")

    # save the last PDF file
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}-{new_pdf_index}.pdf"
    new_pdf_files[new_pdf_index].save(output_filename)
    print(f"[+] File: {output_filename} saved.")
# https://www.thepythoncode.com/article/merge-pdf-files-in-python
# $ pip install PyPDF4==1.27.0

#Import Libraries
from PyPDF4 import PdfFileMerger
import os,argparse

def merge_pdfs(input_files: list, page_range: tuple, output_file: str, bookmark: bool = True):
    """
    Merge a list of PDF files and save the combined result into the `output_file`.
    `page_range` to select a range of pages (behaving like Python's range() function) from the input files
        e.g (0,2) -> First 2 pages 
        e.g (0,6,2) -> pages 1,3,5
    bookmark -> add bookmarks to the output file to navigate directly to the input file section within the output file.

    So we first create a PDFFileMerger object and then iterates over input_files from the input. After that, for each input PDF file, we define a bookmark if required depending on the bookmark variable and add it to the merger object taking into account the page_range chosen.

    Next, we use the append() method from the merger to add our PDF file.
    """
    # strict = False -> To ignore PdfReadError - Illegal Character error
    merger = PdfFileMerger(strict=False)
    for input_file in input_files:
        bookmark_name = os.path.splitext(os.path.basename(input_file))[0] if bookmark else None
        # pages To control which pages are appended from a particular file.
        merger.append(fileobj=open(input_file, 'rb'), pages=page_range, import_bookmarks=False, bookmark=bookmark_name)
    # Insert the pdf at specific page
    merger.write(fileobj=open(output_file, 'wb'))
    merger.close()

def parse_args_merge_pdf():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input_files', dest='input_files', nargs='*',
                        type=str, required=True, help="Enter the path of the files to process")
    parser.add_argument('-p', '--page_range', dest='page_range', nargs='*',
                        help="Enter the pages to consider e.g.: (0,2) -> First 2 pages")
    parser.add_argument('-o', '--output_file', dest='output_file',
                        required=True, type=str, help="Enter a valid output file")
    parser.add_argument('-b', '--bookmark', dest='bookmark', default=True, type=lambda x: (
        str(x).lower() in ['true', '1', 'yes']), help="Bookmark resulting file")
    # To Porse The Command Line Arguments
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

def main_merge_pdf():
    """
    $ python pdf_merger.py --help
    Here is an example merging two PDF files into one:
    $ python pdf_merger.py -i bert-paper.pdf letter.pdf -o combined.pdf
    """
    # Parsing command line arguments entered by user
    args = parse_args_merge_pdf()
    page_range = None
    if args['page_range']:
        page_range = tuple(int(x) for x in args['page_range'][0].split(','))
    # call the main function
    merge_pdfs(
        input_files=args['input_files'], page_range=page_range, 
        output_file=args['output_file'], bookmark=args['bookmark']
    )
# https://www.thepythoncode.com/article/convert-pdf-files-to-docx-in-python
# $ pip install pdf2docx==0.5.1
# Import Libraries
from pdf2docx import parse
from typing import Tuple

def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
    """Converts pdf to docx"""
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file,
                   docx_with_path=output_file, pages=pages)
    summary = {
        "File": input_file, "Pages": str(pages), "Output File": output_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return result

def main_pdf2docx():
    """
    $ python convert_pdf2docx.py letter.pdf letter.docx
    """
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_pdf2docx(input_file, output_file)
# https://www.thepythoncode.com/article/extract-pdf-links-with-python
# pip3 install pikepdf PyMuPDF
import pikepdf # pip3 install pikepdf
def pdf_extract_links():
    file = "1810.04805.pdf"
    # file = "1710.05006.pdf"
    pdf_file = pikepdf.Pdf.open(file)
    urls = []
    # iterate over PDF pages
    for page in pdf_file.pages:
        for annots in page.get("/Annots"):
            uri = annots.get("/A").get("/URI")
            if uri is not None:
                print("[+] URL Found:", uri)
                urls.append(uri)

    print("[*] Total URLs extracted:", len(urls))

import fitz # pip install PyMuPDF
import re

def pdf_extract_links_regex():
    # a regular expression of URLs
    url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    # extract raw text from pdf
    file = "1710.05006.pdf"
    # file = "1810.04805.pdf"
    # open the PDF file
    with fitz.open(file) as pdf:
        text = ""
        for page in pdf:
            # extract text of each PDF page
            text += page.getText()
    # Now text is the target string we want to parse URLs, let's use re module to parse them:
    urls = []
    # extract all urls using the regular expression
    for match in re.finditer(url_regex, text):
        url = match.group()
        print("[+] URL Found:", url)
        urls.append(url)
    print("[*] Total URLs extracted:", len(urls))


# https://www.thepythoncode.com/article/encrypt-pdf-files-in-python
# $ pip install PyPDF4==1.27.0 pyAesCrypt==6.0.0

# Import Libraries
from PyPDF4 import PdfFileReader, PdfFileWriter, utils
import os
import argparse
import getpass
from io import BytesIO
import pyAesCrypt

# Size of chunck
BUFFER_SIZE = 64*1024

def is_encrypted(input_file: str) -> bool:
    """Checks if the inputted file is encrypted using PyPDF4 library"""
    with open(input_file, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file, strict=False)
        return pdf_reader.isEncrypted

def encrypt_pdf(input_file: str, password: str):
    """
    Encrypts a file using PyPDF4 library.
    Precondition: File is not encrypted.

    The encrypt_pdf() function performs the following:

        It validates that the input PDF file is not encrypted using the PyPDF4 library.
        It iterates throughout its pages and adds them to a pdf_writer object.
        Encrypts the pdf_writer object using a given password.

    """
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
    if pdf_reader.isEncrypted:
        print(f"PDF File {input_file} already encrypted")
        return False, None, None
    try:
        # To encrypt all the pages of the input file, you need to loop over all of them
        # and to add them to the writer.
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError as e:
        print(f"Error reading PDF File {input_file} = {e}")
        return False, None, None
    # The default is 128 bit encryption (if false then 40 bit encryption).
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
    return True, pdf_reader, pdf_writer
def decrypt_pdf(input_file: str, password: str):
    """
    Decrypts a file using PyPDF4 library.
    Precondition: A file is already encrypted

    This function performs the following:

        It validates that the input PDF file is encrypted using PyPDF4 library.
        It decrypts the pdf_reader object using the password (must be the correct one).
        It iterates throughout its pages and adds them to a pdf_writer object.

    """
    pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
    if not pdf_reader.isEncrypted:
        print(f"PDF File {input_file} not encrypted")
        return False, None, None
    pdf_reader.decrypt(password=password)
    pdf_writer = PdfFileWriter()
    try:
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError as e:
        print(f"Error reading PDF File {input_file} = {e}")
        return False, None, None
    return True, pdf_reader, pdf_writer

def cipher_stream(inp_buffer: BytesIO, password: str):
    """Ciphers an input memory buffer and returns a ciphered output memory buffer"""
    # Initialize output ciphered binary stream
    out_buffer = BytesIO()
    inp_buffer.seek(0)
    # Encrypt Stream
    pyAesCrypt.encryptStream(inp_buffer, out_buffer, password, BUFFER_SIZE)
    out_buffer.seek(0)
    return out_buffer

def decipher_file(input_file: str, output_file: str, password: str):
    """
    Deciphers an input file and returns a deciphered output file

    In the decipher_file(), we use the decryptStream() method from pyAesCrypt module, which accepts input and output buffer, password, buffer size, and file size as parameters, and writes out the decrypted stream to the output buffer.

    For more convenient use of encryption and decryption of files, I suggest you read this tutorial which uses the cryptography module that is more friendly to Python developers.
    """
    inpFileSize = os.stat(input_file).st_size
    out_buffer = BytesIO()
    with open(input_file, mode='rb') as inp_buffer:
        try:
            # Decrypt Stream
            pyAesCrypt.decryptStream(
                inp_buffer, out_buffer, password, BUFFER_SIZE, inpFileSize)
        except Exception as e:
            print("Exception", str(e))
            return False
        inp_buffer.close()
    if out_buffer:
        with open(output_file, mode='wb') as f:
            f.write(out_buffer.getbuffer())
        f.close()
    return True

def encrypt_decrypt_file(**kwargs):
    """
    Encrypts or decrypts a file
    The above function accepts 5 keyword arguments:

        input_file: The input PDF file.
        output_file: The output PDF file.
        password: The password string you want to encrypt with.
        action: Accepts "encrypt" or "decrypt" actions as string.
        level: Which level of encryption do you want to use. Setting it to 1 means only adding a password during the opening of the PDF file, 2 adds file encryption as another layer of security.

    """
    input_file = kwargs.get('input_file')
    password = kwargs.get('password')
    output_file = kwargs.get('output_file')
    action = kwargs.get('action')
    # Protection Level
    # Level 1 --> Encryption / Decryption using PyPDF4
    # Level 2 --> Encryption and Ciphering / Deciphering and Decryption
    level = kwargs.get('level')
    if not output_file:
        output_file = input_file
    if action == "encrypt":
        result, pdf_reader, pdf_writer = encrypt_pdf(
            input_file=input_file, password=password)
        # Encryption completed successfully
        if result:
            output_buffer = BytesIO()
            pdf_writer.write(output_buffer)
            pdf_reader.stream.close()
            if level == 2:
                output_buffer = cipher_stream(output_buffer, password=password)
            with open(output_file, mode='wb') as f:
                f.write(output_buffer.getbuffer())
            f.close()
    elif action == "decrypt":
        if level == 2:
            decipher_file(input_file=input_file,
                          output_file=output_file, password=password)
        result, pdf_reader, pdf_writer = decrypt_pdf(
            input_file=input_file, password=password)
        # Decryption completed successfully
        if result:
            output_buffer = BytesIO()
            pdf_writer.write(output_buffer)
            pdf_reader.stream.close()
            with open(output_file, mode='wb') as f:
                f.write(output_buffer.getbuffer())
            f.close()

class Password(argparse.Action):
    """
    Hides the password entry
    a new class that inherits from argparse.Action to enter a password securely:

    It overrides __call__() method and sets the dest variable of the namespace object to the password that the user enters using the getpass module.
    """
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)

# def is_valid_path(path):
#     """Validates the path inputted and checks whether it is a file path or a folder path"""
#     if not path:
#         raise ValueError(f"Invalid Path")
#     if os.path.isfile(path):
#         return path
#     elif os.path.isdir(path):
#         return path
#     else:
#         raise ValueError(f"Invalid Path {path}")

def parse_args_encrypt():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="These options are available")
    parser.add_argument("file", help="Input PDF file you want to encrypt", type=is_valid_path)
    # parser.add_argument('-i', '--input_path', dest='input_path', type=is_valid_path,
    #                     required=True, help="Enter the path of the file or the folder to process")
    parser.add_argument('-a', '--action', dest='action', choices=[
                        'encrypt', 'decrypt'], type=str, default='encrypt', help="Choose whether to encrypt or to decrypt")
    parser.add_argument('-l', '--level', dest='level', choices=[
                        1, 2], type=int, default=1, help="Choose which protection level to apply")
    parser.add_argument('-p', '--password', dest='password', action=Password,
                        nargs='?', type=str, required=True, help="Enter a valid password")
    parser.add_argument('-o', '--output_file', dest='output_file',
                        type=str, help="Enter a valid output file")
    args = vars(parser.parse_args())
    # To Display Command Arguments Except Password
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j)
          for i, j in args.items() if i != 'password'))
    print("######################################################################")
    return args

def main_encrypt():
    """
    $ python encrypt_pdf.py --help
    $ python encrypt_pdf.py bert-paper.pdf -a encrypt -l 1 -p -o bert-paper-encrypted1.pdf
    A new PDF file that is secured with a password will appear in the current working directory, if you try to open it with any PDF reader program, you'll be prompted by a password, like shown in the below image:
    let's decrypt it now:

    $ python encrypt_pdf.py bert-paper-encrypted1.pdf -a decrypt -p -l 1 -o bert-paper-decrypted1.pdf
    """
    # Parsing command line arguments entered by user
    args = parse_args_encrypt()
    # Encrypting or Decrypting File
    encrypt_decrypt_file(
        input_file=args['file'], password=args['password'], 
        action=args['action'], level=args['level'], output_file=args['output_file']
    )

# https://www.thepythoncode.com/article/extract-pdf-images-in-python
# pip3 install PyMuPDF Pillow
import fitz # PyMuPDF
import io
from PIL import Image

def pdf_extract_images():
    """
    We're using the getImageList() method to list all available image objects as a list of tuples on that particular page. To get the image object index, we simply get the first element of the tuple returned.
    After that, we use the extractImage() method that returns the image in bytes and additional information, such as the image extension.
    Finally, we convert the image bytes to a PIL image instance and save it to the local disk using the save() method which accepts a file pointer as an argument; we're simply naming the images with their corresponding page and image indices.
    """
    # file path you want to extract images from
    file = "1710.05006.pdf"
    # open the file
    pdf_file = fitz.open(file)
    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        # get image list
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(image_list, start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))

# https://www.thepythoncode.com/article/extract-text-from-images-or-scanned-pdf-python
# $ pip install Filetype==1.0.7 numpy==1.19.4 opencv-python==4.4.0.46 pandas==1.1.4 Pillow==8.0.1 PyMuPDF==1.18.9 pytesseract==0.3.7
# 
import os
import re
import argparse
import pytesseract
from pytesseract import Output
import cv2
import numpy as np
import fitz
from io import BytesIO
from PIL import Image
import pandas as pd
import filetype

# Path Of The Tesseract OCR engine
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Include tesseract executable
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def pix2np(pix):
    """
    Converts a pixmap buffer into a numpy array
    This function converts a pixmap buffer representing a screenshot taken using the PyMuPDF library into a NumPy array.
    """
    # pix.samples = sequence of bytes of the image pixels like RGBA
    #pix.h = height in pixels
    #pix.w = width in pixels
    # pix.n = number of components per pixel (depends on the colorspace and alpha)
    im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.h, pix.w, pix.n)
    try:
        im = np.ascontiguousarray(im[..., [2, 1, 0]])  # RGB To BGR
    except IndexError:
        # Convert Gray to RGB
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
        im = np.ascontiguousarray(im[..., [2, 1, 0]])  # RGB To BGR
    return im

# Image Pre-Processing Functions to improve output accurracy
# Convert to grayscale
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove noise
def remove_noise(img):
    return cv2.medianBlur(img, 5)

# Thresholding
def threshold(img):
    # return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# dilation
def dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)

# erosion
def erode(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(img, kernel, iterations=1)

# opening -- erosion followed by a dilation
def opening(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# canny edge detection
def canny(img):
    return cv2.Canny(img, 100, 200)

# skew correction
def deskew(img):
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

# template matching
def match_template(img, template):
    return cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

def convert_img2bin(img):
    """
    Pre-processes the image and generates a binary output
    """
    # Convert the image into a grayscale image
    output_img = grayscale(img)
    # Invert the grayscale image by flipping pixel values.
    # All pixels that are grater than 0 are set to 0 and all pixels that are = to 0 are set to 255
    output_img = cv2.bitwise_not(output_img)
    # Converting image to binary by Thresholding in order to show a clear separation between white and blacl pixels.
    output_img = threshold(output_img)
    return output_img

# We have defined functions for many preprocessing tasks, including converting images to grayscale, flipping pixel values, separating white and black pixels, and much more.
def display_img(title, img):
    """Displays an image on screen and maintains the output until the user presses a key"""
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.setWindowTitle('img', title)
    cv2.resizeWindow('img', 1200, 900)
    # Display Image on screen
    cv2.imshow('img', img)
    # Mantain output until user presses a key
    cv2.waitKey(0)
    # Destroy windows when user presses a key
    cv2.destroyAllWindows()

# The display_img() function displays on-screen an image in a window having a title set to the title parameter and maintains this window open until the user presses a key on the keyboard.

def generate_ss_text(ss_details):
    """Loops through the captured text of an image and arranges this text line by line.
    This function depends on the image layout."""
    # Arrange the captured text after scanning the page
    parse_text = []
    word_list = []
    last_word = ''
    # Loop through the captured text of the entire page
    for word in ss_details['text']:
        # If the word captured is not empty
        if word != '':
            # Add it to the line word list
            word_list.append(word)
            last_word = word
        if (last_word != '' and word == '') or (word == ss_details['text'][-1]):
            parse_text.append(word_list)
            word_list = []
    return parse_text

def search_for_text(ss_details, search_str):
    """Search for the search string within the image content
    We will be using this function for searching specific text within the grabbed content of an image. It returns a generator of the found matches.
    """
    # Find all matches within one page
    results = re.findall(search_str, ss_details['text'], re.IGNORECASE)
    # In case multiple matches within one page
    for result in results:
        yield result

def save_page_content(pdfContent, page_id, page_data):
    """Appends the content of a scanned page, line by line, to a pandas DataFrame.
    save_page_content() function appends the grabbed content of an image line by line after scanning it to the pdfContent pandas dataframe.
    """
    if page_data:
        for idx, line in enumerate(page_data, 1):
            line = ' '.join(line)
            pdfContent = pdfContent.append(
                {'page': page_id, 'line_id': idx, 'line': line}, ignore_index=True
            )
    return pdfContent

def save_file_content(pdfContent, input_file):
    """Outputs the content of the pandas DataFrame to a CSV file having the same path as the input_file
    but with different extension (.csv)"""
    content_file = os.path.join(os.path.dirname(input_file), os.path.splitext(
        os.path.basename(input_file))[0] + ".csv")
    pdfContent.to_csv(content_file, sep=',', index=False)
    return content_file

def calculate_ss_confidence(ss_details: dict):
    """Calculate the confidence score of the text grabbed from the scanned image."""
    # page_num  --> Page number of the detected text or item
    # block_num --> Block number of the detected text or item
    # par_num   --> Paragraph number of the detected text or item
    # line_num  --> Line number of the detected text or item
    # Convert the dict to dataFrame
    df = pd.DataFrame.from_dict(ss_details)
    # Convert the field conf (confidence) to numeric
    df['conf'] = pd.to_numeric(df['conf'], errors='coerce')
    # Elliminate records with negative confidence
    df = df[df.conf != -1]
    # Calculate the mean confidence by page
    conf = df.groupby(['page_num'])['conf'].mean().tolist()
    return conf[0]

def ocr_img(
        img: np.array, input_file: str, search_str: str, 
        highlight_readable_text: bool = False, action: str = 'Highlight', 
        show_comparison: bool = False, generate_output: bool = True):
    """Scans an image buffer or an image file.
    Pre-processes the image.
    Calls the Tesseract engine with pre-defined parameters.
    Calculates the confidence score of the image grabbed content.
    Draws a green rectangle around readable text items having a confidence score > 30.
    Searches for a specific text.
    Highlight or redact found matches of the searched text.
    Displays a window showing readable text fields or the highlighted or redacted text.
    Generates the text content of the image.
    Prints a summary to the console.
    

    Scans an image buffer or an image file.
    Pre-processes the image.
    Runs the Tesseract engine with pre-defined parameters.
    Calculates the confidence score of the grabbed content of the image.
    Draws a green rectangle around the readable text items having a confidence score greater than 30.
    Searches for a specific text within the image grabbed content.
    Highlights or redacts the found matches of the searched text.
    Displays a window showing readable text fields or the highlighted text or the redacted text.
    Generates the text content of the image.
    Prints a summary to the console.

    """
    # If image source file is inputted as a parameter
    if input_file:
        # Reading image using opencv
        img = cv2.imread(input_file)
    # Preserve a copy of this image for comparison purposes
    initial_img = img.copy()
    highlighted_img = img.copy()
    # Convert image to binary
    bin_img = convert_img2bin(img)
    # Calling Tesseract
    # Tesseract Configuration parameters
    # oem --> OCR engine mode = 3 >> Legacy + LSTM mode only (LSTM neutral net mode works the best)
    # psm --> page segmentation mode = 6 >> Assume as single uniform block of text (How a page of text can be analyzed)
    config_param = r'--oem 3 --psm 6'
    # Feeding image to tesseract
    details = pytesseract.image_to_data(
        bin_img, output_type=Output.DICT, config=config_param, lang='eng')
    # The details dictionary contains the information of the input image
    # such as detected text, region, position, information, height, width, confidence score.
    ss_confidence = calculate_ss_confidence(details)
    boxed_img = None
    # Total readable items
    ss_readable_items = 0
    # Total matches found
    ss_matches = 0
    for seq in range(len(details['text'])):
        # Consider only text fields with confidence score > 30 (text is readable)
        if float(details['conf'][seq]) > 30.0:
            ss_readable_items += 1
            # Draws a green rectangle around readable text items having a confidence score > 30
            if highlight_readable_text:
                (x, y, w, h) = (details['left'][seq], details['top']
                                [seq], details['width'][seq], details['height'][seq])
                boxed_img = cv2.rectangle(
                    img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Searches for the string
            if search_str:
                results = re.findall(
                    search_str, details['text'][seq], re.IGNORECASE)
                for result in results:
                    ss_matches += 1
                    if action:
                        # Draw a red rectangle around the searchable text
                        (x, y, w, h) = (details['left'][seq], details['top']
                                        [seq], details['width'][seq], details['height'][seq])
                        # Details of the rectangle
                        # Starting coordinate representing the top left corner of the rectangle
                        start_point = (x, y)
                        # Ending coordinate representing the botton right corner of the rectangle
                        end_point = (x + w, y + h)
                        #Color in BGR -- Blue, Green, Red
                        if action == "Highlight":
                            color = (0, 255, 255)  # Yellow
                        elif action == "Redact":
                            color = (0, 0, 0)  # Black
                        # Thickness in px (-1 will fill the entire shape)
                        thickness = -1
                        boxed_img = cv2.rectangle(
                            img, start_point, end_point, color, thickness)
                            
    if ss_readable_items > 0 and highlight_readable_text and not (ss_matches > 0 and action in ("Highlight", "Redact")):
        highlighted_img = boxed_img.copy()
    # Highlight found matches of the search string
    if ss_matches > 0 and action == "Highlight":
        cv2.addWeighted(boxed_img, 0.4, highlighted_img,
                        1 - 0.4, 0, highlighted_img)
    # Redact found matches of the search string
    elif ss_matches > 0 and action == "Redact":
        highlighted_img = boxed_img.copy()
        #cv2.addWeighted(boxed_img, 1, highlighted_img, 0, 0, highlighted_img)
    # save the image
    cv2.imwrite("highlighted-text-image.jpg", highlighted_img)  
    # Displays window showing readable text fields or the highlighted or redacted data
    if show_comparison and (highlight_readable_text or action):
        title = input_file if input_file else 'Compare'
        conc_img = cv2.hconcat([initial_img, highlighted_img])
        display_img(title, conc_img)
    # Generates the text content of the image
    output_data = None
    if generate_output and details:
        output_data = generate_ss_text(details)
    # Prints a summary to the console
    if input_file:
        summary = {
            "File": input_file, "Total readable words": ss_readable_items, "Total matches": ss_matches, "Confidence score": ss_confidence
        }
        # Printing Summary
        print("## Summary ########################################################")
        print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
        print("###################################################################")
    return highlighted_img, ss_readable_items, ss_matches, ss_confidence, output_data
    # pass image into pytesseract module
    # pytesseract is trained in many languages
    #config_param = r'--oem 3 --psm 6'
    #details = pytesseract.image_to_data(img,config=config_param,lang='eng')
    # print(details)
    # return details

def image_to_byte_array(image: Image):
    """
    Converts an image into a byte array
    """
    imgByteArr = BytesIO()
    image.save(imgByteArr, format=image.format if image.format else 'JPEG')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

# The image_to_byte_array() function converts an image into a byte array.

# The ocr_file() function does the following:

#     Opens the input PDF file.
#     Opens a memory buffer for storing the output PDF file.
#     Creates a pandas dataframe for storing the page's statistics.
#     Iterates through the chosen pages of the input PDF file.
#     Grabs a screenshot (image) of the selected page of the input PDF file.
#     Converts the screenshot (pix) to a NumPy array.
#     Scans the grabbed screen-shot.
#     Collects the statistics of the screen-shot (page).
#     Saves the content of the screenshot.
#     Adds the updated screenshot to the output file.
#     Saves the whole content of the input PDF file to a CSV file.
#     Saves the output PDF file if required.
#     Prints a summary to the console.

def ocr_file(**kwargs):
    """Opens the input PDF File.
    Opens a memory buffer for storing the output PDF file.
    Creates a DataFrame for storing pages statistics
    Iterates throughout the chosen pages of the input PDF file
    Grabs a screen-shot of the selected PDF page.
    Converts the screen-shot pix to a numpy array
    Scans the grabbed screen-shot.
    Collects the statistics of the screen-shot(page).
    Saves the content of the screen-shot(page).
    Adds the updated screen-shot (Highlighted, Redacted) to the output file.
    Saves the whole content of the PDF file.
    Saves the output PDF file if required.
    Prints a summary to the console."""
    input_file = kwargs.get('input_file')
    output_file = kwargs.get('output_file')
    search_str = kwargs.get('search_str')
    pages = kwargs.get('pages')
    highlight_readable_text = kwargs.get('highlight_readable_text')
    action = kwargs.get('action')
    show_comparison = kwargs.get('show_comparison')
    generate_output = kwargs.get('generate_output')
    # Opens the input PDF file
    pdfIn = fitz.open(input_file)
    # Opens a memory buffer for storing the output PDF file.
    pdfOut = fitz.open()
    # Creates an empty DataFrame for storing pages statistics
    dfResult = pd.DataFrame(
        columns=['page', 'page_readable_items', 'page_matches', 'page_total_confidence'])
    # Creates an empty DataFrame for storing file content
    if generate_output:
        pdfContent = pd.DataFrame(columns=['page', 'line_id', 'line'])
    # Iterate throughout the pages of the input file
    for pg in range(pdfIn.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        # Select a page
        page = pdfIn[pg]
        # Rotation angle
        rotate = int(0)
        # PDF Page is converted into a whole picture 1056*816 and then for each picture a screenshot is taken.
        # zoom = 1.33333333 -----> Image size = 1056*816
        # zoom = 2 ---> 2 * Default Resolution (text is clear, image text is hard to read)    = filesize small / Image size = 1584*1224
        # zoom = 4 ---> 4 * Default Resolution (text is clear, image text is barely readable) = filesize large
        # zoom = 8 ---> 8 * Default Resolution (text is clear, image text is readable) = filesize large
        zoom_x = 2
        zoom_y = 2
        # The zoom factor is equal to 2 in order to make text clear
        # Pre-rotate is to rotate if needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        # To captue a specific part of the PDF page
        # rect = page.rect #page size
        # mp = rect.tl + (rect.bl - (0.75)/zoom_x) #rectangular area 56 = 75/1.3333
        # clip = fitz.Rect(mp,rect.br) #The area to capture
        # pix = page.getPixmap(matrix=mat, alpha=False,clip=clip)
        # Get a screen-shot of the PDF page
        # Colorspace -> represents the color space of the pixmap (csRGB, csGRAY, csCMYK)
        # alpha -> Transparancy indicator
        pix = page.getPixmap(matrix=mat, alpha=False, colorspace="csGRAY")
        # convert the screen-shot pix to numpy array
        img = pix2np(pix)
        # Erode image to omit or thin the boundaries of the bright area of the image
        # We apply Erosion on binary images.
        #kernel = np.ones((2,2) , np.uint8)
        #img = cv2.erode(img,kernel,iterations=1)
        upd_np_array, pg_readable_items, pg_matches, pg_total_confidence, pg_output_data \
            = ocr_img(img=img, input_file=None, search_str=search_str, highlight_readable_text=highlight_readable_text  # False
                      , action=action  # 'Redact'
                      , show_comparison=show_comparison  # True
                      , generate_output=generate_output  # False
                      )
        # Collects the statistics of the page
        dfResult = dfResult.append({'page': (pg+1), 'page_readable_items': pg_readable_items,
                                   'page_matches': pg_matches, 'page_total_confidence': pg_total_confidence}, ignore_index=True)
        if generate_output:
            pdfContent = save_page_content(
                pdfContent=pdfContent, page_id=(pg+1), page_data=pg_output_data)
        # Convert the numpy array to image object with mode = RGB
        #upd_img = Image.fromarray(np.uint8(upd_np_array)).convert('RGB')
        upd_img = Image.fromarray(upd_np_array[..., ::-1])
        # Convert the image to byte array
        upd_array = image_to_byte_array(upd_img)
        # Get Page Size
        """
        #To check whether initial page is portrait or landscape
        if page.rect.width > page.rect.height:
            fmt = fitz.PaperRect("a4-1")
        else:
            fmt = fitz.PaperRect("a4")

        #pno = -1 -> Insert after last page
        pageo = pdfOut.newPage(pno = -1, width = fmt.width, height = fmt.height)
        """
        pageo = pdfOut.newPage(
            pno=-1, width=page.rect.width, height=page.rect.height)
        pageo.insertImage(page.rect, stream=upd_array)
        #pageo.insertImage(page.rect, stream=upd_img.tobytes())
        #pageo.showPDFpage(pageo.rect, pdfDoc, page.number)
    content_file = None
    if generate_output:
        content_file = save_file_content(
            pdfContent=pdfContent, input_file=input_file)
    summary = {
        "File": input_file, "Total pages": pdfIn.pageCount, 
        "Processed pages": dfResult['page'].count(), "Total readable words": dfResult['page_readable_items'].sum(), 
        "Total matches": dfResult['page_matches'].sum(), "Confidence score": dfResult['page_total_confidence'].mean(), 
        "Output file": output_file, "Content file": content_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("\nPages Statistics:")
    print(dfResult, sep='\n')
    print("###################################################################")
    pdfIn.close()
    if output_file:
        pdfOut.save(output_file)
    pdfOut.close()

def ocr_folder(**kwargs):
    """Scans all PDF Files within a specified path
    
    This function is intended to scan the PDF files included within a specific folder. It loops throughout the files of the specified folder either recursively or not depending on the value of the parameter recursive and processes these files one by one.

    It accepts the following parameters:

        input_folder: The path of the folder containing the PDF files to process.
        search_str: The text to search for to manipulate.
        recursive: whether to run this process recursively by looping across the subfolders or not.
        action: the action to perform among the following: Highlight, Redact.
        pages: the pages to consider.
        generate_output: select whether to save the content of the input PDF file to a CSV file or not

    Before we finish, let's define useful functions for parsing command-line arguments:
    """
    input_folder = kwargs.get('input_folder')
    # Run in recursive mode
    recursive = kwargs.get('recursive')
    search_str = kwargs.get('search_str')
    pages = kwargs.get('pages')
    action = kwargs.get('action')
    generate_output = kwargs.get('generate_output')
    # Loop though the files within the input folder.
    for foldername, dirs, filenames in os.walk(input_folder):
        for filename in filenames:
            # Check if pdf file
            if not filename.endswith('.pdf'):
                continue
            # PDF File found
            inp_pdf_file = os.path.join(foldername, filename)
            print("Processing file =", inp_pdf_file)
            output_file = None
            if search_str:
                # Generate an output file
                output_file = os.path.join(os.path.dirname(
                    inp_pdf_file), 'ocr_' + os.path.basename(inp_pdf_file))
            ocr_file(
                input_file=inp_pdf_file, output_file=output_file, search_str=search_str, pages=pages, highlight_readable_text=False, action=action, show_comparison=False, generate_output=generate_output
            )
        if not recursive:
            break

# def is_valid_path(path):
#     """Validates the path inputted and checks whether it is a file path or a folder path"""
#     if not path:
#         raise ValueError(f"Invalid Path")
#     if os.path.isfile(path):
#         return path
#     elif os.path.isdir(path):
#         return path
#     else:
#         raise ValueError(f"Invalid Path {path}")


def parse_args_extract_text():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input-path', type=is_valid_path,
                        required=True, help="Enter the path of the file or the folder to process")
    parser.add_argument('-a', '--action', choices=[
                        'Highlight', 'Redact'], type=str, help="Choose to highlight or to redact")
    parser.add_argument('-s', '--search-str', dest='search_str',
                        type=str, help="Enter a valid search string")
    parser.add_argument('-p', '--pages', dest='pages', type=tuple,
                        help="Enter the pages to consider in the PDF file, e.g. (0,1)")
    parser.add_argument("-g", "--generate-output", action="store_true", help="Generate text content in a CSV file")
    path = parser.parse_known_args()[0].input_path
    if os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file',
                            type=str, help="Enter a valid output file")
        parser.add_argument("-t", "--highlight-readable-text", action="store_true", help="Highlight readable text in the generated image")
        parser.add_argument("-c", "--show-comparison", action="store_true", help="Show comparison between captured image and the generated image")
    if os.path.isdir(path):
        parser.add_argument("-r", "--recursive", action="store_true", help="Whether to process the directory recursively")
    # To Porse The Command Line Arguments
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

# The is_valid_path() function validates a path inputted as a parameter and checks whether it is a file path or a directory path.

# The parse_args() function defines and sets the appropriate constraints for the user's command-line arguments when running this utility.

# Below are explanations for all the parameters:

#     input_path: A required parameter to input the path of the file or the folder to process, this parameter is associated with the is_valid_path() function previously defined.
#     action: The action to perform among a list of pre-defined options to avoid any erroneous selection.
#     search_str: The text to search for to manipulate.
#     pages: the pages to consider when processing a PDF file.
#     generate_content: specifies whether to generate the input file's grabbed content, whether an image or a PDF to a CSV file or not.
#     output_file: The path of the output file. Filling in this argument is constrained by the selection of a file as input, not a directory. 
#     highlight_readable_text: to draw green rectangles around readable text fields having a confidence score greater than 30.
#     show_comparison: Displays a window showing a comparison between the original image and the processed image.
#     recursive: whether to process a folder recursively or not.  Filling in this argument is constrained by the selection of a directory. 
def main_extract_text():
    """
    
    $ python pdf_ocr.py

    $ python pdf_ocr.py -s "BERT" -a Highlight -i example-image-containing-text.jpg
    $ python pdf_ocr.py -s "BERT" -i image.pdf -o output.pdf --generate-output -a "Highlight"
    """
    # Parsing command line arguments entered by user
    args = parse_args_extract_text()
    # If File Path
    if os.path.isfile(args['input_path']):
        # Process a file
        if filetype.is_image(args['input_path']):
            ocr_img(
                # if 'search_str' in (args.keys()) else None
                img=None, input_file=args['input_path'], search_str=args['search_str'], highlight_readable_text=args['highlight_readable_text'], action=args['action'], show_comparison=args['show_comparison'], generate_output=args['generate_output']
            )
        else:
            ocr_file(
                input_file=args['input_path'], output_file=args['output_file'], search_str=args['search_str'] if 'search_str' in (args.keys()) else None, pages=args['pages'], highlight_readable_text=args['highlight_readable_text'], action=args['action'], show_comparison=args['show_comparison'], generate_output=args['generate_output']
            )
    # If Folder Path
    elif os.path.isdir(args['input_path']):
        # Process a folder
        ocr_folder(
            input_folder=args['input_path'], recursive=args['recursive'], search_str=args['search_str'] if 'search_str' in (args.keys()) else None, pages=args['pages'], action=args['action'], generate_output=args['generate_output']
        )
# https://www.thepythoncode.com/article/extract-pdf-metadata-in-python
# $ pip install pikepdf
import pikepdf
import sys

def extract_pdf_metadata_simple():
    # get the target pdf file from the command-line arguments
    pdf_filename = sys.argv[1]
    # read the pdf file
    pdf = pikepdf.Pdf.open(pdf_filename)
    docinfo = pdf.docinfo
    for key, value in docinfo.items():
        print(key, ":", value)

# $ python extract_pdf_metadata_simple.py bert-paper.pdf
# $ python extract_pdf_metadata_simple.py python_cheat_sheet.pdf
import pikepdf
import datetime
import re
from dateutil.tz import tzutc, tzoffset
import sys

pdf_date_pattern = re.compile(''.join([
    r"(D:)?",
    r"(?P<year>\d\d\d\d)",
    r"(?P<month>\d\d)",
    r"(?P<day>\d\d)",
    r"(?P<hour>\d\d)",
    r"(?P<minute>\d\d)",
    r"(?P<second>\d\d)",
    r"(?P<tz_offset>[+-zZ])?",
    r"(?P<tz_hour>\d\d)?",
    r"'?(?P<tz_minute>\d\d)?'?"]))

def transform_date(date_str):
    """
    Convert a pdf date such as "D:20120321183444+07'00'" into a usable datetime
    http://www.verypdf.com/pdfinfoeditor/pdf-date-format.htm
    (D:YYYYMMDDHHmmSSOHH'mm')
    :param date_str: pdf date string
    :return: datetime object
    """
    global pdf_date_pattern
    match = re.match(pdf_date_pattern, date_str)
    if match:
        date_info = match.groupdict()

        for k, v in date_info.items():  # transform values
            if v is None:
                pass
            elif k == 'tz_offset':
                date_info[k] = v.lower()  # so we can treat Z as z
            else:
                date_info[k] = int(v)

        if date_info['tz_offset'] in ('z', None):  # UTC
            date_info['tzinfo'] = tzutc()
        else:
            multiplier = 1 if date_info['tz_offset'] == '+' else -1
            date_info['tzinfo'] = tzoffset(None, multiplier*(3600 * date_info['tz_hour'] + 60 * date_info['tz_minute']))

        for k in ('tz_offset', 'tz_hour', 'tz_minute'):  # no longer needed
            del date_info[k]

        return datetime.datetime(**date_info)

def extract_pdf_metadata_simple2():
    # get the target pdf file from the command-line arguments
    pdf_filename = sys.argv[1]
    # read the pdf file
    pdf = pikepdf.Pdf.open(pdf_filename)
    docinfo = pdf.docinfo
    for key, value in docinfo.items():
        if str(value).startswith("D:"):
            # pdf datetime format, convert to python datetime
            value = transform_date(str(pdf.docinfo["/CreationDate"]))
        print(key, ":", value)


# https://www.thepythoncode.com/article/compress-pdf-files-in-python
# $ pip install PDFNetPython3==8.1.0
# Import Libraries
import os
import sys
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def compress_file(input_file: str, output_file: str):
    """Compress PDF file"""
    if not output_file:
        output_file = input_file
    initial_size = os.path.getsize(input_file)
    try:
        # Initialize the library
        PDFNet.Initialize()
        doc = PDFDoc(input_file)
        # Optimize PDF with the default settings
        doc.InitSecurityHandler()
        # Reduce PDF size by removing redundant information and compressing data streams
        Optimizer.Optimize(doc)
        doc.Save(output_file, SDFDoc.e_linearized)
        doc.Close()
    except Exception as e:
        print("Error compress_file=", e)
        doc.Close()
        return False
    compressed_size = os.path.getsize(output_file)
    ratio = 1 - (compressed_size / initial_size)
    summary = {
        "Input File": input_file, "Initial Size": get_size_format(initial_size),
        "Output File": output_file, f"Compressed Size": get_size_format(compressed_size),
        "Compression Ratio": "{0:.3%}.".format(ratio)
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return True

def main_compress_pdf():
    """
    $ python pdf_compressor.py bert-paper.pdf bert-paper-min.pdf

    """
    # Parsing command line arguments entered by user
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    compress_file(input_file, output_file)

# https://www.thepythoncode.com/article/optical-character-recognition-pytesseract-python
# pip3 install pytesseract
# pip3 install numpy matplotlib opencv-python pillow
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def ocr_tesseract():
    # read the image using OpenCV
    image = cv2.imread("test.png")
    # or you can use Pillow
    # image = Image.open("test.png")
    # get the string
    string = pytesseract.image_to_string(image)
    # print it
    print(string)
    # make a copy of this image to draw in
    image_copy = image.copy()
    # the target word to search for
    target_word = "dog"
    # get all data from the image
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    # get all occurences of the that word
    word_occurences = [ i for i, word in enumerate(data["text"]) if word.lower() == target_word ]
    for occ in word_occurences:
        # extract the width, height, top and left position for that detected word
        w = data["width"][occ]
        h = data["height"][occ]
        l = data["left"][occ]
        t = data["top"][occ]
        # define all the surrounding box points
        p1 = (l, t)
        p2 = (l + w, t)
        p3 = (l + w, t + h)
        p4 = (l, t + h)
        # draw the 4 lines (rectangular)
        image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=2)
        image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=2)
        image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=2)
        image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=2)
    plt.imsave("all_dog_words.png", image_copy)
    plt.imshow(image_copy)
    plt.show()



# https://www.thepythoncode.com/article/watermark-in-pdf-using-python
# $ pip install PyPDF4==1.27.0 reportlab==3.5.59

from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_
import os
import argparse
from io import BytesIO
from typing import Tuple
# Import the reportlab library
from reportlab.pdfgen import canvas
# The size of the page supposedly A4
from reportlab.lib.pagesizes import A4
# The color of the watermark
from reportlab.lib import colors

PAGESIZE = A4
FONTNAME = 'Helvetica-Bold'
FONTSIZE = 40
# using colors module
# COLOR = colors.lightgrey
# or simply RGB
# COLOR = (190, 190, 190)
COLOR = colors.red
# The position attributes of the watermark
X = 250
Y = 10
# The rotation angle in order to display the watermark diagonally if needed
ROTATION_ANGLE = 45

def get_info(input_file: str):
    """
    Extracting the file info
    """
    # If PDF is encrypted the file metadata cannot be extracted
    with open(input_file, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file, strict=False)
        output = {
            "File": input_file, "Encrypted": ("True" if pdf_reader.isEncrypted else "False")
        }
        if not pdf_reader.isEncrypted:
            info = pdf_reader.getDocumentInfo()
            num_pages = pdf_reader.getNumPages()
            output["Author"] = info.author
            output["Creator"] = info.creator
            output["Producer"] = info.producer
            output["Subject"] = info.subject
            output["Title"] = info.title
            output["Number of pages"] = num_pages
    # To Display collected metadata
    print("## File Information ##################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in output.items()))
    print("######################################################################")
    return True, output

def get_output_file(input_file: str, output_file: str):
    """
    Check whether a temporary output file is needed or not
    """
    input_path = os.path.dirname(input_file)
    input_filename = os.path.basename(input_file)
    # If output file is empty -> generate a temporary output file
    # If output file is equal to input_file -> generate a temporary output file
    if not output_file or input_file == output_file:
        tmp_file = os.path.join(input_path, 'tmp_' + input_filename)
        return True, tmp_file
    return False, output_file

def create_watermark(wm_text: str):
    """
    Creates a watermark template.
    """
    if wm_text:
        # Generate the output to a memory buffer
        output_buffer = BytesIO()
        # Default Page Size = A4
        c = canvas.Canvas(output_buffer, pagesize=PAGESIZE)
        # you can also add image instead of text
        # c.drawImage("logo.png", X, Y, 160, 160)
        # Set the size and type of the font
        c.setFont(FONTNAME, FONTSIZE)
        # Set the color
        if isinstance(COLOR, tuple):
            color = (c/255 for c in COLOR)
            c.setFillColorRGB(*color)
        else:
            c.setFillColor(COLOR)
        # Rotate according to the configured parameter
        c.rotate(ROTATION_ANGLE)
        # Position according to the configured parameter
        c.drawString(X, Y, wm_text)
        c.save()
        return True, output_buffer
    return False, None

# This function performs the following:

#     Creates a watermark file and stores it in memory.
#     Apply the parameters defined earlier on our created canvas using reportlab.

# Note that you can instead of using the drawString() method to write text, you can use drawImage() to draw an image, as written as a comment in the above function.

def save_watermark(wm_buffer, output_file):
    """
    Saves the generated watermark template to disk
    """
    with open(output_file, mode='wb') as f:
        f.write(wm_buffer.getbuffer())
    f.close()
    return True

def watermark_pdf(input_file: str, wm_text: str, pages: Tuple = None):
    """
    Adds watermark to a pdf file.
    """
    result, wm_buffer = create_watermark(wm_text)
    if result:
        wm_reader = PdfFileReader(wm_buffer)
        pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
        pdf_writer = PdfFileWriter()
        try:
            for page in range(pdf_reader.getNumPages()):
                # If required to watermark specific pages not all the document pages
                if pages:
                    if str(page) not in pages:
                        continue
                page = pdf_reader.getPage(page)
                page.mergePage(wm_reader.getPage(0))
                pdf_writer.addPage(page)
        except Exception as e:
            print("Exception = ", e)
            return False, None, None
        return True, pdf_reader, pdf_writer
# This function aims to merge the inputted PDF file with the generated watermark. It accepts the following parameters:

#     input_file: The path of the PDF file to watermark.
#     wm_text: The text to set as a watermark.
#     pages: The pages to watermark.

# It performs the following:

#     Creates a watermark and stores it in the memory buffer.
#     Iterates throughout the pages of the input file and merge each of the selected pages with the watermark that is previously generated. The watermark acts like an overlay on top of the page.
#     Adds the resulting page to the pdf_writer object.

def unwatermark_pdf(input_file: str, wm_text: str, pages: Tuple = None):
    """
    Removes watermark from the pdf file.
    """
    pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
    pdf_writer = PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
        # If required for specific pages
        if pages:
            if str(page) not in pages:
                continue
        page = pdf_reader.getPage(page)
        # Get the page content
        content_object = page["/Contents"].getObject()
        content = ContentStream(content_object, pdf_reader)
        # Loop through all the elements page elements
        for operands, operator in content.operations:
            # Checks the TJ operator and replaces the corresponding string operand (Watermark text) with ''
            if operator == b_("Tj"):
                text = operands[0]
                if isinstance(text, str) and text.startswith(wm_text):
                    operands[0] = TextStringObject('')
        page.__setitem__(NameObject('/Contents'), content)
        pdf_writer.addPage(page)
    return True, pdf_reader, pdf_writer


# The purpose of this function is to remove the watermark text from the PDF file. It accepts the following parameters:

#     input_file: The path of the PDF file to watermark.
#     wm_text: The text to set as a watermark.
#     pages: The pages to watermark.

# It performs the following:

#     Iterates throughout the pages of the input file and grab the content of each page.
#     Using the grabbed content, it finds the operator TJ and replaces the string (watermark text) following this operator.
#     Adds the resulting page following the merge to the pdf_writer object.

def watermark_unwatermark_file(**kwargs):
    input_file = kwargs.get('input_file')
    wm_text = kwargs.get('wm_text')
    # watermark   -> Watermark
    # unwatermark -> Unwatermark
    action = kwargs.get('action')
    # HDD -> Temporary files are saved on the Hard Disk Drive and then deleted
    # RAM -> Temporary files are saved in memory and then deleted.
    mode = kwargs.get('mode')
    pages = kwargs.get('pages')
    temporary, output_file = get_output_file(
        input_file, kwargs.get('output_file'))
    if action == "watermark":
        result, pdf_reader, pdf_writer = watermark_pdf(
            input_file=input_file, wm_text=wm_text, pages=pages)
    elif action == "unwatermark":
        result, pdf_reader, pdf_writer = unwatermark_pdf(
            input_file=input_file, wm_text=wm_text, pages=pages)
    # Completed successfully
    if result:
        # Generate to memory
        if mode == "RAM":
            output_buffer = BytesIO()
            pdf_writer.write(output_buffer)
            pdf_reader.stream.close()
            # No need to create a temporary file in RAM Mode
            if temporary:
                output_file = input_file
            with open(output_file, mode='wb') as f:
                f.write(output_buffer.getbuffer())
            f.close()
        elif mode == "HDD":
            # Generate to a new file on the hard disk
            with open(output_file, 'wb') as pdf_output_file:
                pdf_writer.write(pdf_output_file)
            pdf_output_file.close()
            pdf_reader.stream.close()
            if temporary:
                if os.path.isfile(input_file):
                    os.replace(output_file, input_file)
                output_file = input_file

# The above function accepts several parameters:

#     input_file: The path of the PDF file to watermark.
#     wm_text: The text to set as a watermark.
#     action: The action to perform whether to watermark or to un-watermark file.
#     mode: The location of the temporary file whether to memory or hard disk.
#     pages: The pages to watermark.

# watermark_unwatermark_file() function calls the previously defined functions watermark_pdf() or unwatermark_pdf() depending on the chosen action.

# Based on the selected mode, and if the output file has a similar path as the input file or no output file is specified, then a temporary file will be created in case the selected mode is HDD (hard disk drive).

# Next, let's add the ability to add or remove watermark from a folder containing multiple PDF files:

def watermark_unwatermark_folder(**kwargs):
    """
    Watermarks all PDF Files within a specified path
    Unwatermarks all PDF Files within a specified path
    """
    input_folder = kwargs.get('input_folder')
    wm_text = kwargs.get('wm_text')
    # Run in recursive mode
    recursive = kwargs.get('recursive')
    # watermark   -> Watermark
    # unwatermark -> Unwatermark
    action = kwargs.get('action')
    # HDD -> Temporary files are saved on the Hard Disk Drive and then deleted
    # RAM -> Temporary files are saved in memory and then deleted.
    mode = kwargs.get('mode')
    pages = kwargs.get('pages')
    # Loop though the files within the input folder.
    for foldername, dirs, filenames in os.walk(input_folder):
        for filename in filenames:
            # Check if pdf file
            if not filename.endswith('.pdf'):
                continue
            # PDF File found
            inp_pdf_file = os.path.join(foldername, filename)
            print("Processing file:", inp_pdf_file)
            watermark_unwatermark_file(input_file=inp_pdf_file, output_file=None,
                                       wm_text=wm_text, action=action, mode=mode, pages=pages)
        if not recursive:
            break

# def is_valid_path(path):
#     """
#     Validates the path inputted and checks whether it is a file path or a folder path
#     """
#     if not path:
#         raise ValueError(f"Invalid Path")
#     if os.path.isfile(path):
#         return path
#     elif os.path.isdir(path):
#         return path
#     else:
#         raise ValueError(f"Invalid Path {path}")
def parse_args_pdf_watermark():
    """
    Get user command line parameters
    """
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input_path', dest='input_path', type=is_valid_path,
                        required=True, help="Enter the path of the file or the folder to process")
    parser.add_argument('-a', '--action', dest='action', choices=[
                        'watermark', 'unwatermark'], type=str, default='watermark',
                        help="Choose whether to watermark or to unwatermark")
    parser.add_argument('-m', '--mode', dest='mode', choices=['RAM', 'HDD'], type=str,
                        default='RAM', help="Choose whether to process on the hard disk drive or in memory")
    parser.add_argument('-w', '--watermark_text', dest='watermark_text',
                        type=str, required=True, help="Enter a valid watermark text")
    parser.add_argument('-p', '--pages', dest='pages', type=tuple,
                        help="Enter the pages to consider e.g.: [2,4]")
    path = parser.parse_known_args()[0].input_path
    if os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file',
                            type=str, help="Enter a valid output file")
    if os.path.isdir(path):
        parser.add_argument('-r', '--recursive', dest='recursive', default=False, type=lambda x: (
            str(x).lower() in ['true', '1', 'yes']), help="Process Recursively or Non-Recursively")
    # To Porse The Command Line Arguments
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

# Below are the arguments defined:

#     input_path: A required parameter to input the path of the file or the folder to process, this parameter is associated with the is_valid_path() function previously defined.
#     action: The action to perform, which is either watermark or unwatermark the PDF file, default is to watermark.
#     mode: To specify the destination of the generated temporary file, whether to memory or hard disk.
#     watermark_text: The string to set as a watermark.
#     pages: The pages to watermark (e.g first page is [0], the second page and the fourth page is [1, 3], etc.). If not specified, then all pages.
#     output_file: The path of the output file.
#     recursive: Whether to process a folder recursively.

# Now that we have everything, let's write the main code to execute based on parameters passed:

def main_pdf_watermark():
    """
    $ python pdf_watermarker.py --help
    $ python pdf_watermarker.py -a watermark -i "CV Bassem Marji_Eng.pdf" -w "CONFIDENTIAL" -o CV_watermark.pdf
    $ python pdf_watermarker.py -a unwatermark -i "CV_watermark.pdf" -w "CONFIDENTIAL" -o CV.pdf
    You can also set the -m and -p for mode and pages respectively. You can also watermark a list of PDF files located under a specific path:
    $ python pdf_watermarker.py -i "C:\Scripts\Test" -a "watermark" -w "CONFIDENTIAL" -r False
    $ python pdf_watermarker.py -i "C:\Scripts\Test" -a "unwatermark" -w "CONFIDENTIAL" -m HDD -p[0] -r False
    """
    # Parsing command line arguments entered by user
    args = parse_args_pdf_watermark()
    # If File Path
    if os.path.isfile(args['input_path']):
        # Extracting File Info
        get_info(input_file=args['input_path'])
        # Encrypting or Decrypting a File
        watermark_unwatermark_file(
            input_file=args['input_path'], wm_text=args['watermark_text'], action=args[
                'action'], mode=args['mode'], output_file=args['output_file'], pages=args['pages']
        )
    # If Folder Path
    elif os.path.isdir(args['input_path']):
        # Encrypting or Decrypting a Folder
        watermark_unwatermark_folder(
            input_folder=args['input_path'], wm_text=args['watermark_text'],
            action=args['action'], mode=args['mode'], recursive=args['recursive'], pages=args['pages']
        )

# https://www.thepythoncode.com/article/convert-pdf-files-to-images-in-python
# $ pip install PyMuPDF==1.18.9
import fitz

from typing import Tuple
import os

def convert_pdf2img(input_file: str, pages: Tuple = None):
    """Converts pdf to image and generates a file by page"""
    # Open the document
    pdfIn = fitz.open(input_file)
    output_files = []
    # Iterate throughout the pages
    for pg in range(pdfIn.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        # Select a page
        page = pdfIn[pg]
        rotate = int(0)
        # PDF Page is converted into a whole picture 1056*816 and then for each picture a screenshot is taken.
        # zoom = 1.33333333 -----> Image size = 1056*816
        # zoom = 2 ---> 2 * Default Resolution (text is clear, image text is hard to read)    = filesize small / Image size = 1584*1224
        # zoom = 4 ---> 4 * Default Resolution (text is clear, image text is barely readable) = filesize large
        # zoom = 8 ---> 8 * Default Resolution (text is clear, image text is readable) = filesize large
        zoom_x = 2
        zoom_y = 2
        # The zoom factor is equal to 2 in order to make text clear
        # Pre-rotate is to rotate if needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        output_file = f"{os.path.splitext(os.path.basename(input_file))[0]}_page{pg+1}.png"
        pix.writePNG(output_file)
        output_files.append(output_file)
    pdfIn.close()
    summary = {
        "File": input_file, "Pages": str(pages), "Output File(s)": str(output_files)
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return output_files

def main_pdf_to_image():
    import sys
    input_file = sys.argv[1]
    convert_pdf2img(input_file)


# https://www.thepythoncode.com/article/convert-html-to-pdf-in-python
# $ apt update
# $ apt install wkhtmltopdf
# $ sudo yum makecache --refresh
# $ sudo yum -y install wkhtmltopdf
# $ brew install Caskroom/cask/wkhtmltopdf
# $ pip install pdfkit
import pdfkit

def html_to_pdf():
    """
    We use the from_file() function, the first argument is the location of the HTML file,
    and the second is the resulting PDF document path,
    we set the enable-local-file-access to True in the options parameter to allow local file access from this HTML file to images and CSS/JS files.
    """
    # directly from url
    pdfkit.from_url("https://google.com", "google.pdf", verbose=True)
    print("="*50)
    # from file
    pdfkit.from_file("webapp/index.html", "index.pdf", verbose=True, options={"enable-local-file-access": True})
    print("="*50)
    # from HTML content
    pdfkit.from_string("<p><b>Python</b> is a great programming language.</p>", "string.pdf", verbose=True)
    print("="*50)

# js:
# https://dzone.com/articles/pdf-document-generation-with-templates-in-javascri
