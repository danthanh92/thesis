import csv
import time
import codecs
from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import cosine_distances
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender

start_time = time.time()
dataset = {}  # define a dictionary
with open('dataset-recsys.csv') as myfile:
    reader = csv.DictReader(myfile, delimiter=',')
    i = 0
    for line in reader:
        i += 1
        if (i == 1):
            continue

        if (int(line['user_id']) not in dataset):
            dataset[int(line['user_id'])] = {}

        dataset[int(line['user_id'])][int(line['item_id'])] = float(line['star_rating'])


model = MatrixPreferenceDataModel(dataset)

# User-based Similarity

similarity = UserSimilarity(model, cosine_distances)
recsys = UserBasedRecommender(model, similarity, with_preference=True)

# Item-based Similarity

# similarity = ItemSimilarity(model, cosine_distances)
# nhood_strategy = ItemsNeighborhoodStrategy()
# recsys = ItemBasedRecommender(model, similarity, nhood_strategy, with_preference=False)

# recsys = MatrixFactorBasedRecommender(model=model, items_selection_strategy=nhood_strategy,
# n_features=10, n_interations=1)

# evaluator = CfEvaluator()

# result = evaluator.evaluate(recsys, None, permutation=False, at=10, sampling_ratings=0.7)


# Cross Validation
# result = evaluator.evaluate_on_split(recsys, 'rmse', permutation=False, at=10, cv=5, sampling_ratings=0.7)

# pprint (result)
# print output
output = codecs.open('./Data/CF_model_output_1', mode='w')
for user_id in dataset:
    tmp_string = ",".join("(%s,%s)" % tup for tup in recsys.recommend(user_id))
    output.write(tmp_string + '\n')
print ("--- %s seconds ---" % round(time.time() - start_time))

