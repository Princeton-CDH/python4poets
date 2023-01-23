import re,requests,os,sys,random
import nltk

# make sure we have the tokenizer package
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


cache_nouns = None

### strings
austen_str = 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'
potter_str = '''Harry had a thin face, knobbly knees, black hair and bright-green eyes. He wore round glasses held together with a lot of Sellotape because of all the times Dudley had punched him on the nose. The only thing Harry liked about his own appearance was a very thin scar on his forehead which was shaped like a bolt of lightning.'''


### functions



def tokenize(text):
    """
    Split a text into tokens (words, morphemes we can separate such as
    "n't", and punctuation).
    """
    return list(_tokenize_gen(text))


def _tokenize_gen(text):
    for sent in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sent):
            yield word


def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
    text = ' '.join(words)
    step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .', '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
        "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()



# Step 1. Getting list of nouns
def get_list_of_nouns():
    # cached already?
    global cache_nouns
    if cache_nouns: return cache_nouns
    
    # set url
    url = 'https://raw.githubusercontent.com/Princeton-CDH/python-for-poets/main/data/nouns.txt'
    
    # download the url to a text string
    text = requests.get(url).text

    # split it by new lines
    words = text.strip().split('\n')

    # sort
    words.sort()

    # add it to cache
    cache_nouns = words

    # return list of words
    return words
    

def swap_words(text, swap):
    orig_words = tokenize(text)
    swap = {
        **dict((v,k) for k,v in swap.items()),
        **dict((k.title(), v.title()) for k,v in swap.items()),
        **dict((v.title(), k.title()) for k,v in swap.items()),
        **swap, 
    }

    new_words = [
        swap.get(orig_word, orig_word)
        for orig_word in orig_words
    ]
    
    return untokenize(new_words)


def quick_plot(x_list, y_list):
    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax = plt.subplots()
    ax.plot(x_list, y_list, linewidth=2.0)
    plt.show()


def printm(x):
    from IPython.display import Markdown
    display(Markdown(x))