from nltk.tokenize import sent_tokenize


def file_into_sentence(filepath):
	data = None
	with open(filepath, 'r') as fd:
		data = fd.read().replace('\n', '')

	return data


def tokenize_sentence(data, language="english"):
    """
    ls ~/nltk_data/tokenizers/punkt
    czech 
    danish
    dutch
    english
    estonian
    finnish
    french
    german
    greek
    italian
    norwegian
    polish
    portuguese
    slovenespanish
    swedish
    turkish
    """
    sentences = sent_tokenize(data, language=language)
    return sentences


def print_sentences(sentences, printer=print):
    for s in sentences:
        printer(s)
