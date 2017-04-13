import codecs
import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

try:
    similarity_point = codecs.open('../Data/similarity_point', mode='r')
except IOError as (error, strerror):
    logging.error('Input file : I/O error ({0}):{1}'.format(error, strerror))
else:
    rating = codecs.open('../Data/user_rating', mode='w')
    for line in similarity_point:
        tmp_list = line.strip().split(', ')
        # print ('length of list: %s' % len(tmp_list))
        user_id = tmp_list.pop(0)
        number_items = len(tmp_list)
        # print ('length of item: %s' % number_items)

        for i in range(0, number_items):
            tup = tmp_list[i].strip().split(':')
            item_iid = tup[0]
            distance_point = float(tup[1])

            if (distance_point < 0.2):
                rate = 1
            elif (distance_point >= 0.2 and distance_point < 0.4):
                rate = 2
            elif (distance_point >= 0.4 and distance_point < 0.6):
                rate = 3
            elif (distance_point >= 0.6 and distance_point < 0.8):
                rate = 4
            else:
                rate = 5

            # print distance_point
            # print [rate, number_items / 5, i]

            if (i < number_items / 5):
                rate = (rate + 5) / 2
            elif (i < 2 * number_items / 5):
                rate = (rate + 4) / 2
            elif (i < 3 * number_items / 5):
                rate = (rate + 3) / 2
            elif (i < 4 * number_items / 5):
                rate = (rate + 2) / 2
            else:
                rate = (rate + 1) / 2

            rating.write('%s, %s, %s\n' % (user_id, item_iid, rate))
logging.info('Finished CF preprocessing.')
