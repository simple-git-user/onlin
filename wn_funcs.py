import nltk
from nltk.corpus import wordnet as wn

def get_all_synonyms(word):
    """gets in a list all synonyms of all the synsets of word"""
    l_syns = []
    synsets = wn.synsets(word)
    for synset in synsets:
        for lemma_name in synset.lemma_names:
            l_syns.append(  lemma_name )
    return l_syns