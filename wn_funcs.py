
def get_all_synonyms(word):
    """gets in a list all synonyms of all the synsets of word"""
    l_syns = []
    synsets = wn.synsets(word)
    for synset in synsets:
        if word2 in synset.lemma_names:
            l_syns.append(  word2 )
    return l_syns