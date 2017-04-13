# -*- coding: utf-8 -*-
import logging
import codecs
import re
from gensim import corpora
from collections import defaultdict
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

try:
    input_file = codecs.open('../Original-data/otoxemay.vn_item_content_tokenized', encoding='utf-8', mode='r')
except IOError as (error, strerror):
    logging.error('Input file : I/O error ({0}):{1}'.format(error, strerror))
else:
    # remove special characters and numbers in text
    regex = re.compile('\D+')
    texts = [[word for word in line.split() if len(word) > 1 and regex.match(word)] for line in input_file]

    # set a frequency dictionary of tokens
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # remove 10% highest and 10% lowest frequent tokens
    tmp_list = frequency.values()
    tmp_list.sort()
    min_frequency = tmp_list[len(tmp_list) / 10]
    max_frequency = tmp_list[len(tmp_list) / 10 * 9]

    texts = [[token for token in text if frequency[token] > min_frequency and frequency[token] < max_frequency]
             for text in texts]

    # save dictionary and corpus to use later
    dictionary = corpora.Dictionary(texts)
    dictionary.save('../Data/corpus.dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('../Data/corpus.mm', corpus)
