from pathlib import Path

GPU_BATCH_SIZE = 4
GRADIENT_BATCH_SIZE = 64
PATH_LENGTH_REGULIZER_FREQUENCY = 2
GRADIENT_ACCUMULATE_EVERY = 4 # unused if using run.py


CONDITION_ON_MAPPER = True
CHANNELS = 1
NETWORK_CAPACITY = 16
STYLE_DEPTH = 8
IMAGE_SIZE = 64
LATENT_DIM = 512
USE_BIASES = False

EXTS = ['jpg', 'png']
FOLDER = "E:\\datasets\\GochiUsa_128\\train"

HOMOGENEOUS_LATENT_SPACE = True
USE_DIVERSITY_LOSS = False
MIXED_PROBABILITY = 0.9

MOVING_AVERAGE_START = 4000
MOVING_AVERAGE_PERIOD = 200

EVALUATE_EVERY = 100
SAVE_EVERY = 250
NUM_TRAIN_STEPS = EVALUATE_EVERY*100

NAME = "default"
CURRENT_DIR = Path('.')
LOG_FILENAME = CURRENT_DIR / 'logs.csv'
MODELS_DIR = CURRENT_DIR / 'models'
RESULTS_DIR = CURRENT_DIR / 'results'

NEW = True
LOAD_FROM = -1

GPU = '0'
EPSILON = 1e-8
LEARNING_RATE = 2e-4
LABEL_EPSILON = 0
