# # -*- coding: utf-8 -*-
# import time
# import codecs
# import recsys.algorithm
# from recsys.algorithm.factorize import SVD
# from recsys.datamodel.data import Data

# recsys.algorithm.VERBOSE = True

# start_time = time.time()

# dataset = Data()
# dataset.load('./Data/similarity.txt', sep=', ', format={'col': 0, 'row': 1, 'value': 2, 'ids': int})

# svd = SVD()
# # svd.load_data(filename='./data/dataset-recsys.csv', sep=',', format={'col':0, 'row':1, 'value':2, 'ids': int})
# # About format parameter:
# # 'row': 1 -> Rows in matrix come from second column in dataset-recsys.csv file
# # 'col': 0 -> Cols in matrix come from first column in dataset-recsys.csv file
# # 'value': 2 -> Values (Mij) in matrix come from third column in dataset-recsys.csv file
# # 'ids': int -> Ids (row and col ids) are integers (not strings)

# # train, test = data.split_train_test(percent=70) # 70% train, 30% test

# svd.set_data(dataset)
# k = 100
# # svd.compute(k=k, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True)
# # min_values = 10 means those items that had less than 10 users who rated it, and those users that
# # rated less than 10 items are removed

# # Parameters:
# # k (int) – number of dimensions
# # min_values (int) – min. number of non-zeros (or non-empty values) any row or col must have
# # pre_normalize (string) – normalize input matrix. Possible values are tfidf, rows, cols, all.
# # mean_center (Boolean) – centering the input matrix (aka mean substraction)
# # post_normalize (Boolean) – Normalize every row of U Sigma to be a unit vector. Thus, row similarity
# # (using cosine distance) returns [-1.0 .. 1.0]
# # savefile (string) – path to save the SVD factorization (U, Sigma and V matrices)

# # output SVD model can also be saved in a zip file
# svd.compute(k=k, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True, savefile='./datamodel')
# # svd.similarity(ITEMID1, ITEMID2)


# output = codecs.open('./Data/recsys_model_output', mode='w')
# tmp = svd.recommend(50, n=10, only_unknowns=True, is_row=False)
# tmp_string = ",".join("(%s,%s)" % tup for tup in tmp)
# output.write(tmp_string + '\n')
# # and then the zipped model can be loaded
# # svd2 = SVD(filename='/tmp/movielens')
# # svd2.similarity(ITEMID1, ITEMID2)
# print("--- %s seconds ---" % round(time.time() - start_time))
