import codecs
import logging
from gensim import corpora, models
from scipy.spatial.distance import cosine

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
num_topics = 20
try:
    dict_file = codecs.open('../Data/corpus.dict', encoding='utf-8', mode='r')
    corpus_file = codecs.open('../Data/corpus.mm', encoding='utf-8', mode='r')
    user_profiles = codecs.open('../Data/user_profile', mode='r')
    item_contents = codecs.open('../Original-data/otoxemay.vn_item_content_tokenized', mode='r')
except IOError as (error, strerror):
    logging.error('Input file : I/O error ({0}):{1}'.format(error, strerror))
else:
    # load dictionary and copus to build model
    dictionary = corpora.Dictionary.load('../Data/corpus.dict')
    corpus = corpora.MmCorpus('../Data/corpus.mm')

    # build LDA model
    model = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topics, minimum_probability=0.0)

    # load all contents
    contents = [line for line in item_contents]

    output = codecs.open('../Data/similarity_point', mode='w')

    # compute similarity between each vector user and each vector document had read

    for line in user_profiles:
        tmp_list = line.strip().split(',')
        user_id = tmp_list.pop(0)
        item_ids = [int(item) for item in tmp_list]

        # join all contents user had read
        user_contents = ''
        for iid in item_ids:
            user_contents = ' '.join((user_contents, contents[iid]))

        user_bow = dictionary.doc2bow(user_contents.split())  # list of tokens of user-docs
        user_vec = model[user_bow]  # convert user-docs to LDA space

        user_vec_1D = [value[1] for value in user_vec]
        # user_vec_1D = [0] * num_topics
        # for value in user_vec:
        #     user_vec_1D[value[0]] = value[1]
        # logging.info(user_vec_1D)

        distance_list = []
        for iid in item_ids:
            item_bow = dictionary.doc2bow(contents[iid].split())  # list of tokens of doc
            item_vec = model[item_bow]  # convert doc to LDA space

            item_vec_1D = [value[1] for value in item_vec]
            # item_vec_1D = [0] * num_topics
            # for value in item_vec:
            #     item_vec_1D[value[0]] = value[1]

            # logging.info(item_vec_1D)

            distance = cosine(user_vec_1D, item_vec_1D)
            distance_list.append([iid, distance])

        output.write('%s, %s\n' % (user_id, ', '.join(':'.join(str(value) for value in tup) for tup in distance_list)))
        # break


