import os

RANDOM_NO_FILTER = False

EPOCHS = 85

TOTAL_FLASHES_W_FILTER = 60

CHANNELS = [8, 10, 12, 48, 50, 52, 60, 62]

DATA_POINTS_PER_FLASH = 242

# Multiply the index of the data point by this to get to the next data point.
FLASH_MULTIPLIER = 42

FLASHES_PER_TRIAL = 12

TRIALS_PER_EPOCH = 15

FILE_PATH = os.path.join("BCI_Comp_III_Wads_2004", "Subject_A_Train.mat")

TEST_FILE_PATH = os.path.join("BCI_Comp_III_Wads_2004", "Subject_A_Test.mat")

FLASHES_PER_EPOCH = FLASHES_PER_TRIAL * TRIALS_PER_EPOCH

NUM_DATAPOINTS_SKIPPED = 11

TRAINING_NUM = (int(EPOCHS * 0.85) - 1) * 180
TESTING_NUM = (EPOCHS - TRAINING_NUM - 1) * 180