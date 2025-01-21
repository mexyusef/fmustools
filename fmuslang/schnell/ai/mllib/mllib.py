import json, random

import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tensorflow as tf
import tflearn


################## utk standalone
import sys
schnelldir = '/home/usef/danger/ulib/schnell'
sys.path.extend([schnelldir, '..'])
from app.dirutils import (
	ayah, here, joiner,
	save_dir_under_tempdir,
	save_file_under_tempdir,
)
from app.fileutils import file_content, json_file_content
from app.serial import kirim, terima
print('pytest importing...')
##################

def create_stemmer(stemmer_type=LancasterStemmer):
	stemmer = stemmer_type()
	return stemmer

# bow = bag_of_words

class CDW:

	def __init__(self, stemmer_type=LancasterStemmer, intents_file='intents.json', training_file='training.bin'):
		self.intents_file = intents_file
		self.training_file = training_file
		self.classes = []
		self.documents = []
		self.words = []
		self.ignore_words = ['?']
		self.stemmer = create_stemmer(stemmer_type)
		self.projectname = 'mllib'
		self.logdir = save_dir_under_tempdir('mllib/logs', persistent=True)
		self.modeldir = save_dir_under_tempdir('mllib/model.tflearn', persistent=True)
		self.ERROR_THRESHOLD = 0.25
		# create a data structure to hold user context
		self.context = {}

	def clean_up_sentence(self, sentence):
		sentence_words = nltk.word_tokenize(sentence)
		sentence_words = [self.stemmer.stem(word.lower()) for word in sentence_words]
		return sentence_words


	# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
	def bag_of_words(self, sentence, show_details=False):
		# tokenize the pattern
		sentence_words = self.clean_up_sentence(sentence)
		# bag of words
		bag = [0] * len(self.words)  
		for s in sentence_words:
			for i,w in enumerate(self.words):
				if w == s: 
					bag[i] = 1
					if show_details:
						print ("found in bag: %s" % w)

		return(np.array(bag))

	def load_intents_file(self):
		self.intents = json_file_content(self.intents_file)

	def load_data(self):
		self.load_intents_file()

		print('loaded intents =', self.intents, type(self.intents))

		# loop through each sentence in our intents patterns
		for intent in self.intents['intents']:
			for pattern in intent['patterns']:
				# tokenize each word in the sentence
				w = nltk.word_tokenize(pattern)
				# add to our words list
				self.words.extend(w)
				# add to documents in our corpus
				self.documents.append((w, intent['tag']))
				# add to our classes list
				if intent['tag'] not in self.classes:
					self.classes.append(intent['tag'])

		# stem and lower each word and remove duplicates
		self.words = [self.stemmer.stem(w.lower()) for w in self.words if w not in self.ignore_words]
		self.words = sorted(list(set(self.words)))
		# remove duplicates
		self.classes = sorted(list(set(self.classes)))

		self.print_cdw()

	def print_cdw(self):
		print (len(self.documents), "documents")
		print (len(self.classes), "classes", self.classes)
		print (len(self.words), "unique stemmed words", self.words)

	def training_data(self):
		# create our training data
		self.training = []
		self.output = []
		# create an empty array for our output
		output_empty = [0] * len(self.classes)

		# training set, bag of words for each sentence
		for doc in self.documents:
			# initialize our bag of words
			bag = []
			# list of tokenized words for the pattern
			pattern_words = doc[0]
			# stem each word
			pattern_words = [self.stemmer.stem(word.lower()) for word in pattern_words]
			# create our bag of words array
			for w in self.words:
				bag.append(1) if w in pattern_words else bag.append(0)

			# output is a '0' for each tag and '1' for current tag
			output_row = list(output_empty)
			output_row[self.classes.index(doc[1])] = 1

			self.training.append([bag, output_row])

		# shuffle our features and turn into np.array
		random.shuffle(self.training)
		# /home/usef/danger/ulib/schnell/ai/mllib/mllib.py:127: VisibleDeprecationWarning: 
		# Creating an ndarray from ragged nested sequences 
		# (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) 
		# is deprecated. 
		# If you meant to do this, you must specify 'dtype=object' when creating the ndarray
		self.training = np.array(self.training)

		# create train and test lists
		self.train_x = list(self.training[:,0])
		self.train_y = list(self.training[:,1])

	def build_neural_network(self):
		# reset underlying graph data
		# tf.reset_default_graph()
		tf.compat.v1.reset_default_graph()
		# Build neural network
		net = tflearn.input_data(shape=[None, len(self.train_x[0])])
		net = tflearn.fully_connected(net, 8)
		net = tflearn.fully_connected(net, 8)
		net = tflearn.fully_connected(net, len(self.train_y[0]), activation='softmax')
		net = tflearn.regression(net)

		# Define model and setup tensorboard
		self.model = tflearn.DNN(net, tensorboard_dir=self.logdir)

	def create_model(self):
		self.build_neural_network()
		# Start training (apply gradient descent algorithm)
		self.model.fit(self.train_x, self.train_y, n_epoch=1000, batch_size=8, show_metric=True)    

	def model_predict(self, kalimat):
		return self.model.predict(
			[
				self.bag_of_words(kalimat)
			]
		)

	def training_handle_file(self, reading=False):
		return open(self.training_file, 'rb' if reading else 'wb')

	def save_model(self):
		self.model.save(self.modeldir)
		print('saving to:', self.modeldir)

	def load_model(self):
		print('loading from:', self.modeldir)
		self.model.load(self.modeldir)

	def save_training(self):
		data = {
			'words'     : self.words, 
			'classes'   : self.classes, 
			'train_x'   : self.train_x, 
			'train_y'   : self.train_y,
		}
		kirim(data, file_handle=self.training_handle_file())

	def load_training(self):
		data = terima(file_handle=self.training_handle_file(reading=True))
		self.words = data['words']
		self.classes = data['classes']
		self.train_x = data['train_x']
		self.train_y = data['train_y']

	def classify(self, sentence):
		# generate probabilities from the model
		results = self.model.predict(
			[
				self.bag_of_words(sentence)
			]
		)[0]
		# filter out predictions below a threshold
		results = [[i,r] for i,r in enumerate(results) if r>self.ERROR_THRESHOLD]
		# sort by strength of probability
		results.sort(key=lambda x: x[1], reverse=True)
		return_list = []
		for r in results:
			return_list.append(
				(self.classes[r[0]], r[1])
			)
		# return tuple of intent and probability
		return return_list

	

	def response(self, sentence, userID='wieke', show_details=False):
		results = self.classify(sentence)
		# if we have a classification then find the matching intent tag
		if results:
			# loop as long as there are matches to process
			while results:
				for i in self.intents['intents']:
					# find a tag matching the first result
					if i['tag'] == results[0][0]:
						# set context for this intent if necessary
						if 'context_set' in i:
							if show_details: 
								print ('context:', i['context_set'])
							self.context[userID] = i['context_set']

						# check if this intent is contextual and applies to this user's conversation
						if not 'context_filter' in i or \
							(userID in self.context and \
								'context_filter' in i and \
								i['context_filter'] == self.context[userID]):
							if show_details: 
								print ('tag:', i['tag'])
							# a random response from the intent
							return random.choice(i['responses'])

				results.pop(0)


def save_model():  
	# cdw = CDW()
	# cdw.load_data()
	# cdw.training_data()
	# cdw.create_model()
	# cdw.save_model()
	return 'OK'


def load_model():
	# cdw = CDW()
	# cdw.load_model()
	# p = cdw.bag_of_words('when is your shop open today?')
	# print('p:', p)
	# print('classes:', cdw.classes)
	return 'OK'


def save_load_model():
	cdw = CDW()
	# cdw.load_data()
	# cdw.training_data()
	# cdw.create_model()
	# cdw.save_model()
	# cdw.save_training()	

	# gini toh urutannya
	
	# intents
	cdw.load_data()
	# train_x, train_y, words, classes
	cdw.load_training()
	# define model
	cdw.build_neural_network()
	# load model
	cdw.load_model()

	print('\n' + '='*80 + '\n')
	print('classes:', cdw.classes)
	kalimat = 'when is your shop open today?'
	while kalimat:
		if kalimat == 'tags' or kalimat == 'classes':
			print('classes:', cdw.classes)
		else:
			pred = cdw.model_predict(kalimat).tolist() # arr of arr [[]]
			# result = list(zip(cdw.classes, *pred))
			# result = result.sort(key=lambda tup: tup[1])
			# result = sorted(result, key=lambda item: item[1])
			# print(f'prediction for {kalimat}:', json.dumps(result, indent=4))
			print(f'prediction for {kalimat}:', pred)
			out1 = cdw.classify(kalimat)
			out2 = cdw.response(kalimat)
			print('kalimat:', kalimat)
			print('classify:', out1)
			print('response:', out2)
		kalimat = input('Masukkan kalimat lain: ')

if __name__ == '__main__':
	# save_model()
	# load_model()
	save_load_model()
