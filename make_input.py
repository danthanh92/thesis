# import random
# import csv

# fieldnames = ['user_id', 'item_id', 'star_rating']
# with open('dataset-recsys_1.csv', "w") as myfile:  # writing data to new csv file
#     writer = csv.DictWriter(myfile, delimiter=',', fieldnames=fieldnames)
#     writer.writeheader()

#     # for x in range(1, 3000):
#     #     items = random.sample(list(range(1, 3000)), 20)
#     #     for item in items:
#     #         writer.writerow({'user_id': x, 'item_id': item,
#     #                          'star_rating': random.randint(1, 5)})

#     for x in range(1, 300):
#             items = random.sample(list(range(1, 300)), 20)
#             for item in items:
#                 writer.writerow({'user_id': x, 'item_id': item,
#                                  'star_rating': random.randint(1, 5)})

import codecs
output = codecs.open('./Data/similarity', mode='w')
a1 = 11
a2 = 0.2
a = []
a.append([12, 0.8])
a.append([a1, a2])
print a
output.write('%s, %s\n' % (a1, ', '.join(':'.join(str(value) for value in tup) for tup in a)))
