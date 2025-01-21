import pytesseract
# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# https://pypi.org/project/pytesseract/
from PIL import Image
from wand.image import Image as wi
import io


def open_image_blob(imgblob):
	''' dari wand-image make_blob '''
	return Image.open(io.BytesIO(imgblob))

# from imagehandler import open_image_blob
# def imgblob_to_pilimage(imgblob):
# 	return open_image_blob(imgblob)


def itext(pil_image, lang='eng'):
	return pytesseract.image_to_string(pil_image, lang=lang)

def pdf_to_pdfimg(filepath, imgtype='jpeg', resolution=300):
	pdf = wi(filename=filepath, resolution=resolution)
	return pdf.convert(imgtype)

def pdfimg_to_imgseq(pdf_image):
	return pdf_image.sequence

def imgseq_to_imgblobs(image_seq, imgtype='jpeg'):
	image_blobs = []
	for img in image_seq:
		img_page = wi(image=img)
		image_blobs.append(img_page.make_blob(imgtype))
	return image_blobs

def recognize_blobs(imgblobs):
	recognized_texts = []
	for ib in imgblobs:
		pil_image = open_image_blob(ib) # imgblob_to_pilimage( ib )
		text = itext( pil_image )
		recognized_texts.append(text)

	return recognized_texts

def pdf_to_text(pdf_filepath):
	'''
	https://github.com/nikhilkumarsingh/tesseract-python/blob/master/pdf_example.py
	'''
	pdf_image = pdf_to_pdfimg(pdf_filepath)
	image_seq = pdfimg_to_imgseq(pdf_image)
	iblobs = imgseq_to_imgblobs(image_seq)
	recognized = recognize_blobs(iblobs)
	return recognized
