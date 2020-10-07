from yacs.config import CfgNode as CN

cfg = CN()
cfg.OUTPUT_DIR = 'output'
cfg.LOG_DIR = 'log'
cfg.DATA_DIR = ''
cfg.GPUS = (0,)
cfg.WORKERS = 4
cfg.PRINT_FREQ = 1000
cfg.AUTO_RESUME = True
cfg.PIN_MEMORY = True
cfg.RANK = 0
cfg.VERBOSE = True
cfg.DIST_BACKEND = 'nccl'
cfg.MULTIPROCESSING_DISTRIBUTED = True

# FP16 training params
cfg.FP16 = CN()
cfg.FP16.ENABLED = False
cfg.FP16.STATIC_LOSS_SCALE = 1.0
cfg.FP16.DYNAMIC_LOSS_SCALE = False

# Cudnn related params
cfg.CUDNN = CN()
cfg.CUDNN.BENCHMARK = True
cfg.CUDNN.DETERMINISTIC = False
cfg.CUDNN.ENABLED = True

# common params for NETWORK
cfg.MODEL = CN()
cfg.MODEL.NAME = 'pose_higher_hrnet'
cfg.MODEL.INIT_WEIGHTS = True
cfg.MODEL.PRETRAINED = ''
cfg.MODEL.NUM_JOINTS = 17
cfg.MODEL.TAG_PER_JOINT = True
cfg.MODEL.EXTRA = CN(new_allowed=True)
cfg.MODEL.SYNC_BN = False
cfg.MODEL.PRETRAINED = 'models/pytorch/imagenet/hrnet_w32-36af842e.pth'

cfg.MODEL.EXTRA.NO_STAGE = 4
cfg.MODEL.EXTRA.FINAL_CONV_KERNEL = 1
cfg.MODEL.EXTRA.PRETRAINED_LAYERS = ['*']
cfg.MODEL.EXTRA.STEM_INPLANES = 64

cfg.MODEL.EXTRA.STAGE1 = CN()
cfg.MODEL.EXTRA.STAGE1.NUM_MODULES = 1
cfg.MODEL.EXTRA.STAGE1.NUM_BRANCHES = 1
cfg.MODEL.EXTRA.STAGE1.BLOCK = 'BOTTLENECK'
cfg.MODEL.EXTRA.STAGE1.NUM_BLOCKS = [4]
cfg.MODEL.EXTRA.STAGE1.NUM_CHANNELS = [64]
cfg.MODEL.EXTRA.STAGE1.FUSE_METHOD = 'SUM'

cfg.MODEL.EXTRA.STAGE2 = CN()
cfg.MODEL.EXTRA.STAGE2.NUM_MODULES = 1
cfg.MODEL.EXTRA.STAGE2.NUM_BRANCHES = 2
cfg.MODEL.EXTRA.STAGE2.BLOCK = 'BASIC'
cfg.MODEL.EXTRA.STAGE2.NUM_BLOCKS = [4,4]
cfg.MODEL.EXTRA.STAGE2.NUM_CHANNELS = [32,64]
cfg.MODEL.EXTRA.STAGE2.FUSE_METHOD = 'SUM'

cfg.MODEL.EXTRA.STAGE3 = CN()
cfg.MODEL.EXTRA.STAGE3.NUM_MODULES = 4
cfg.MODEL.EXTRA.STAGE3.NUM_BRANCHES = 3
cfg.MODEL.EXTRA.STAGE3.BLOCK = 'BASIC'
cfg.MODEL.EXTRA.STAGE3.NUM_BLOCKS = [4,4,4]
cfg.MODEL.EXTRA.STAGE3.NUM_CHANNELS = [32,64,128]
cfg.MODEL.EXTRA.STAGE3.FUSE_METHOD = 'SUM'

cfg.MODEL.EXTRA.STAGE4 = CN()
cfg.MODEL.EXTRA.STAGE4.NUM_MODULES = 3
cfg.MODEL.EXTRA.STAGE4.NUM_BRANCHES = 4
cfg.MODEL.EXTRA.STAGE4.BLOCK = 'BASIC'
cfg.MODEL.EXTRA.STAGE4.NUM_BLOCKS = [4,4,4,4]
cfg.MODEL.EXTRA.STAGE4.NUM_CHANNELS = [32,64,128,256]
cfg.MODEL.EXTRA.STAGE4.FUSE_METHOD = 'SUM'

cfg.MODEL.EXTRA.DECONV = CN()
cfg.MODEL.EXTRA.DECONV.NUM_DECONVS = 1
cfg.MODEL.EXTRA.DECONV.NUM_CHANNELS = [32]
cfg.MODEL.EXTRA.DECONV.KERNEL_SIZE = [4]
cfg.MODEL.EXTRA.DECONV.NUM_BASIC_BLOCKS = 4
cfg.MODEL.EXTRA.DECONV.CAT_OUTPUT = [True]

cfg.LOSS = CN()
cfg.LOSS.NUM_STAGES = 2
cfg.LOSS.WITH_HEATMAPS_LOSS = [True, True]
cfg.LOSS.HEATMAPS_LOSS_FACTOR = [1.0, 1.0]
cfg.LOSS.WITH_AE_LOSS = [True, False]
cfg.LOSS.AE_LOSS_TYPE = 'exp'
cfg.LOSS.PUSH_LOSS_FACTOR = [0.001, 0.001]
cfg.LOSS.PULL_LOSS_FACTOR = [0.001, 0.001]
cfg.LOSS.WITH_HEATMAPS_TS_LOSS = [True,True]
cfg.LOSS.WITH_TAGMAPS_TS_LOSS = [False,False]

# DATASET related params
cfg.DATASET = CN()
cfg.DATASET.ROOT = 'coco'
cfg.DATASET.DATASET = 'coco_kpt'
cfg.DATASET.DATASET_TEST = 'coco'
cfg.DATASET.NUM_JOINTS = 17
cfg.DATASET.MAX_NUM_PEOPLE = 30
cfg.DATASET.TRAIN = 'train2017'
cfg.DATASET.TEST = 'val2017'
cfg.DATASET.DATA_FORMAT = 'jpg'
cfg.DATASET.SIGMA = 2
cfg.DATASET.FLIP = 0.5

# training data augmentation
cfg.DATASET.MAX_ROTATION = 30
cfg.DATASET.MIN_SCALE = 0.75
cfg.DATASET.MAX_SCALE = 1.5
cfg.DATASET.SCALE_TYPE = 'short'
cfg.DATASET.MAX_TRANSLATE = 40
cfg.DATASET.INPUT_SIZE = 512
cfg.DATASET.OUTPUT_SIZE = [128, 256]

# heatmap generator (default is OUTPUT_SIZE/64)
cfg.DATASET.SIGMA = -1
cfg.DATASET.SCALE_AWARE_SIGMA = False
cfg.DATASET.BASE_SIZE = 256.0
cfg.DATASET.BASE_SIGMA = 2.0
cfg.DATASET.INT_SIGMA = False

cfg.DATASET.WITH_CENTER = False

# train
cfg.TRAIN = CN()

cfg.TRAIN.LR_FACTOR = 0.1
cfg.TRAIN.LR_STEP = [60, 90]
cfg.TRAIN.LR = 0.001

cfg.TRAIN.OPTIMIZER = 'adam'
cfg.TRAIN.MOMENTUM = 0.9
cfg.TRAIN.WD = 0.0001
cfg.TRAIN.NESTEROV = False
cfg.TRAIN.GAMMA1 = 0.99
cfg.TRAIN.GAMMA2 = 0.0

cfg.TRAIN.BEGIN_EPOCH = 0
cfg.TRAIN.END_EPOCH = 100

cfg.TRAIN.RESUME = False
cfg.TRAIN.CHECKPOINT = ''

cfg.TRAIN.IMAGES_PER_GPU = 12
cfg.TRAIN.SHUFFLE = True

cfg.TRAIN.TEACHER_WEIGHT = 0.9

# testing
cfg.TEST = CN()

# size of images for each device
# cfg.TEST.BATCH_SIZE = 32
cfg.TEST.IMAGES_PER_GPU = 1
# Test Model Epoch
cfg.TEST.FLIP_TEST = True
cfg.TEST.ADJUST = True
cfg.TEST.REFINE = True
cfg.TEST.SCALE_FACTOR = [1]
# group
cfg.TEST.DETECTION_THRESHOLD = 0.1
cfg.TEST.TAG_THRESHOLD = 1.
cfg.TEST.USE_DETECTION_VAL = True
cfg.TEST.IGNORE_TOO_MUCH = False
cfg.TEST.MODEL_FILE = ''
cfg.TEST.IGNORE_CENTER = True
cfg.TEST.NMS_KERNEL = 5
cfg.TEST.NMS_PADDING = 2
cfg.TEST.PROJECT2IMAGE = True

cfg.TEST.WITH_HEATMAPS = (True,True)
cfg.TEST.WITH_AE = (True,False)

cfg.TEST.LOG_PROGRESS = False

# debug
cfg.DEBUG = CN()
cfg.DEBUG.DEBUG = True
cfg.DEBUG.SAVE_BATCH_IMAGES_GT = False
cfg.DEBUG.SAVE_BATCH_IMAGES_PRED = False
cfg.DEBUG.SAVE_HEATMAPS_GT = True
cfg.DEBUG.SAVE_HEATMAPS_PRED = True
cfg.DEBUG.SAVE_TAGMAPS_PRED = True

"""if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'w') as f:
        print(_C, file=f)"""
