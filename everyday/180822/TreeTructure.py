# from nltk.corpus import treebank
# t=treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()
#
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

#/Library/Frameworks/Python.framework/Versions/3.6/nltk_data