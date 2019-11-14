import os
from pathlib import Path


OUTPUT_DIR_TRAIN='data/train.dat'
OUTPUT_DIR_TEST='data/test.dat'
ROOT_DIR='data/final_dataset.txt'
#CLEAN_FILE = os.path.abspath(os.path.join(p, '..', 'data/raw/filmtrust/clean_ratings.txt'))
NUM_USERS=3579
NUM_TEST_RATINGS=15


def count_rating_per_user():

    rating_per_user={}

    for line in open(ROOT_DIR):

        line=line.split(',')
        user_nr=int(line[0])

        if user_nr in rating_per_user:
            rating_per_user[user_nr]+=1
        else:
            rating_per_user[user_nr]=1

    return rating_per_user



def train_test_split():

    user_rating=count_rating_per_user()
    print(user_rating)
    test_counter=0

    next_user=1
    '''
    clean_writer = open(CLEAN_FILE,'w')
    for line in open(ROOT_DIR):
        splitted_line=line.split()
        user_nr=int(splitted_line[0])
        if user_rating[user_nr]<=NUM_TEST_RATINGS*2:
            continue
        clean_writer.write(line)
    clean_writer.close()
    '''

    train_writer=open(OUTPUT_DIR_TRAIN, 'w')
    test_writer=open(OUTPUT_DIR_TEST, 'w')
    write_test_samples = True
    prev_user = -1
    i = 0
    test_flag = False
    for line in open(ROOT_DIR):

        splitted_line=line.split(',')
        user_nr=int(splitted_line[0])
        if user_nr != prev_user:
            test_flag = True
        if i == NUM_TEST_RATINGS:
            test_flag = False
            i = 0
        if test_flag:
            test_writer.write(line)
            i += 1
        else:
            train_writer.write(line)

        prev_user = user_nr

if __name__ == "__main__":

    train_test_split()
