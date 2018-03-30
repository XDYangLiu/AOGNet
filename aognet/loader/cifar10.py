import os
import sys
import mxnet as mx


def cifar10_iterator(cfg, kv):

    train_rec = os.path.join(cfg.dataset.data_dir, "cifar10_train.rec")
    val_rec = os.path.join(cfg.dataset.data_dir, "cifar10_val.rec")

    mean = [125.31, 123.01, 113.91]
    std = [63.01, 62.09, 66.71]

    train = mx.io.ImageRecordIter(
            path_imgrec         = train_rec,
            label_width         = 1,
            data_name           = 'data',
            label_name          = 'softmax_label',
            data_shape          = (3, 32, 32),
            batch_size          = cfg.batch_size,
            pad                 = 4,
            fill_value          = 127,
            #mean_r              = mean[0],
            #mean_g              = mean[1],
            #mean_b              = mean[2],
            #std_r               = std[0],
            #std_g               = std[1],
            #std_b               = std[2],
            rand_crop           = True if cfg.dataset.aug_level > 0 else False,
            rand_mirror         = True if cfg.dataset.aug_level > 0 else False,
            shuffle             = True if cfg.dataset.aug_level >= 0 else False,
            num_parts           = kv.num_workers,
            part_index          = kv.rank)

    val = mx.io.ImageRecordIter(
            path_imgrec         = val_rec,
            label_width         = 1,
            data_name           = 'data',
            label_name          = 'softmax_label',
            batch_size          = cfg.batch_size,
            data_shape          = (3, 32, 32),
            #mean_r              = mean[0],
            #mean_g              = mean[1],
            #mean_b              = mean[2],
            #std_r               = std[0],
            #std_g               = std[1],
            #std_b               = std[2],
            rand_crop           = False,
            rand_mirror         = False,
            num_parts           = kv.num_workers,
            part_index          = kv.rank)

    return train, val
