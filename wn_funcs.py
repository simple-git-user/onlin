import nltk
from nltk.corpus import wordnet as wn
import itertools as itt

def get_all_synonyms(word):
    """gets in a list all synonyms of all the synsets of word"""
    l_syns = []
    synsets = wn.synsets(word)
    for synset in synsets:
        for lemma_name in synset.lemma_names:
            l_syns.append(  lemma_name )
    return l_syns
	
def get_all_antonyms(word):
	"""get in a list all antonyms of all synsets of word"
	l_antonyms = []
    synsets = wn.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas:
            l_antonyms.extend(  lemma.antonyms() )
    return l_antonyms

#AxB
#itt.product([0,1,2],[1,2])
#(1,2),(2,1)...
#itt.permutations([1,2,3],2)

