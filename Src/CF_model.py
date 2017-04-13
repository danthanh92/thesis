# -*- coding: utf-8 -*-
import time
import codecs
import recsys.algorithm
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
from recsys.evaluation.prediction import RMSE, MAE

recsys.algorithm.VERBOSE = True
PERCENT_TRAIN = 20
MIN_RATING = 0.0
MAX_RATING = 5.0
start_time = time.time()

data = Data()
data.load('../Data/user_rating', sep=', ', format={'col': 0, 'row': 1, 'value': 2, 'ids': int})

# Train & Test data
train, test = data.split_train_test(percent=PERCENT_TRAIN)

svd = SVD()
# svd.load_data(filename='./data/dataset-recsys.csv', sep=',', format={'col':0, 'row':1, 'value':2, 'ids': int})
# About format parameter:
# 'row': 1 -> Rows in matrix come from second column in rating file
# 'col': 0 -> Cols in matrix come from first column in rating file
# 'value': 2 -> Values (Mij) in matrix come from third column in rating file
# 'ids': int -> Ids (row and col ids) are integers (not strings)

# train, test = data.split_train_test(percent=70) # 70% train, 30% test

svd.set_data(train)
k = 100
# svd.compute(k=k, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True)
# min_values = 10 means those items that had less than 10 users who rated it, and those users that
# rated less than 10 items are removed

# Parameters:
# k (int) – number of dimensions
# min_values (int) – min. number of non-zeros (or non-empty values) any row or col must have
# pre_normalize (string) – normalize input matrix. Possible values are tfidf, rows, cols, all.
# mean_center (Boolean) – centering the input matrix (aka mean substraction)
# post_normalize (Boolean) – Normalize every row of U Sigma to be a unit vector. Thus, row similarity
# (using cosine distance) returns [-1.0 .. 1.0]
# savefile (string) – path to save the SVD factorization (U, Sigma and V matrices)

# output SVD model can also be saved in a zip file
svd.compute(k=k, min_values=1, pre_normalize=None, mean_center=True, post_normalize=True, savefile='../Data/datamodel')
# svd.similarity(ITEMID1, ITEMID2)

recommend_output = codecs.open('../Data/recommender_output', mode='w')
model_rating = codecs.open('../Data/model_rating_result', mode='w')

# for user_id in users_list:
#     recommend_list = svd.recommend(int(user_id), n=10, is_row=False)
#     recommend_iids = [tup[0] for tup in recommend_list]
#     tmp_string = ','.join(str(iid) for iid in recommend_iids)
#     recommend_output.write(user_id + ',' + tmp_string + '\n')

# Evaluation using prediction-based metrics
rmse = RMSE()
mae = MAE()
for rating, item_id, user_id in test.get():
    try:
        pred_rating = svd.predict(item_id, user_id)
        model_rating.write('%s, %s, %s, %s\n' % (user_id, item_id, rating, pred_rating))
        rmse.add(rating, pred_rating)
        mae.add(rating, pred_rating)
    except KeyError:
        continue

print 'RMSE = %s' % rmse.compute()
print 'MAE = %s' % mae.compute()
print("--- %s seconds ---" % round(time.time() - start_time))
