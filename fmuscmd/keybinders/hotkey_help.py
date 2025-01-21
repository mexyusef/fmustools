from schnell.app.ocrutils import take_screenshot

def screenshot(bisa_berisi_file_folder):
	# take_screenshot(output_file=None, output_dir=None)
	args = [bisa_berisi_file_folder.strip()]
	if ',' in bisa_berisi_file_folder:
		args = [item.strip() for item in bisa_berisi_file_folder.split(',')]
	if args:
		take_screenshot(*args)
	else:
		take_screenshot()

def buat_kalimat_aktor(kata_kata, nama_aktor):
	bariskalimat = f"""create a lively, vibrant, crazy, funny, bizarre, imaginative, emotional, memorable story about a person named "{nama_aktor}".

1. Please incorporate the following words in the story:
{kata_kata}

2. The story should be just {len(kata_kata)//3} paragraphs.

3. Give the Indonesian translation right after the story separated by a line of 40 '=' characters.

Then give answer to the following questions:
1. Where and when were the settings?
2. What is the plot?
3. Are there actors beside {nama_aktor}? If yes, who are they?
4. Why is it easy to remember?
"""
	return bariskalimat
