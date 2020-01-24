from __future__ import print_function
import os 
import zipfile
import random
from shutil import copyfile

RACE_LIST = ['Asian', 'Black', 'India', 'Others', 'White']

CUR_DIR = 'ALL DATA/'
TRAIN_DIR = 'train/'
TEST_DIR = 'test/'


for race in RACE_LIST:
    print(race, "has", len(os.listdir(CUR_DIR + '/' + race)), " images")

def make_diretory(DIR):
    for race in RACE_LIST:
        os.mkdir(DIR + '/' + race)
    
def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE = 0.9):
    for race in RACE_LIST:
        files = []
        for filename in os.listdir(SOURCE + '/' + race):
            file = SOURCE + '/' + race + '//' + filename
            if os.path.getsize(file) > 0:
                files.append(filename)
            else:
                print(filename, "is zero length!")
        training_length = int(len(files) * SPLIT_SIZE)
        testing_length = len(files) - training_length
        files = random.sample(files, len(files))
        training_set = files[:training_length]
        testing_set = files[-testing_length:]

        for filename in training_set:
            src = SOURCE + '/' + race + '//' + filename
            dst = TRAINING + '/' + race + '//' + filename
            copyfile(src, dst)

        for filename in testing_set:
            src = SOURCE + '/' + race + '//' + filename
            dst = TESTING + '/' + race + '//' + filename
            copyfile(src, dst)


make_diretory(TRAIN_DIR)
make_diretory(TEST_DIR)

split_data(CUR_DIR, TRAIN_DIR, TEST_DIR, 0.9)
