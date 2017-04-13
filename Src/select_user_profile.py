import codecs
import logging
import datetime
import time
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

try:
    input_file = codecs.open('../Original-data/otoxemay.vn_user_profile', mode='r')
except IOError as (error, strerror):
    logging.error('Input file : I/O error ({0}):{1}'.format(error, strerror))
else:
    user_profile = codecs.open('../Data/user_profile', mode='w')
    # test_file = codecs.open('../Data/user_profile_test', mode='w')

    to_time = time.mktime(datetime.datetime.strptime("04/10/2016", "%d/%m/%Y").timetuple()) * 1000
    from_time = time.mktime(datetime.datetime.strptime("15/09/2016", "%d/%m/%Y").timetuple()) * 1000

    for line in input_file:
        tmp_list = line.strip().split('\t')
        user_id = int(tmp_list.pop(0))
        items = [item.strip().split(',').pop(1) for item in tmp_list]

        if len(items) > 5 and len(items) < 50:
            user_profile.write('%s,%s\n' % (user_id, ','.join(items)))

        # train_items = []
        # test_items = []
        # for item in items:
        #     if int(item[0]) > from_time and int(item[0]) < to_time:
        #         train_items.append(item[1])
        #     elif int(item[0]) >= to_time:
        #         test_items.append(item[1])

        # number_train_item = len(train_items)
        # number_test_item = len(test_items)

        # if number_train_item + number_test_item > 5 and number_train_item + number_test_item < 50:
        #     if number_test_item and number_train_item and number_train_item / number_test_item > 2:
        #         train_file.write('%s,%s\n' % (user_id, ','.join(train_items)))
        #         test_file.write('%s,%s\n' % (user_id, ','.join(test_items)))
        #     elif number_train_item and number_test_item:
        #         train_file.write('%s,%s\n' % (user_id, ','.join(test_items) + ',' + ','.join(train_items)))
        #     elif number_train_item:
        #         train_file.write('%s,%s\n' % (user_id, ','.join(train_items)))
        #     else:
        #         train_file.write('%s,%s\n' % (user_id, ','.join(test_items)))

    logging.info('Finished making training and testing file.')

