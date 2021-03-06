import nltk
#state of union from various presidents
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
# train tokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# test tokenizer
tokenized = custom_sent_tokenizer.tokenize(sample_text)
# String_tokenizer -> word_tokenizer
def process_content():
	try:
		for i in tokenized[5:]:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			#regex modifiers to get ANY adverb
			#dont forget r in front and triple quotes
			#this will chunk everything
			chunkGram = r"""Chunk: {<.*>+}
			#close open curly braces for chinking
									}<VB.?|IN|DT|TO>+{ """
			
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			#requires matplotlib
			chunked.draw()

	except Exception as e:
		print(str(e))

process_content()

#chinking is the removal of stuff from chunks
#chunking everything except for a specific thing



