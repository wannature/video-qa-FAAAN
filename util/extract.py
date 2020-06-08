# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
from tensorflow.python import pywrap_tensorflow
import pandas as pd
from pandas import Series, DataFrame
from PIL import Image
from glob import glob
import skimage.io
inputs = tf.placeholder(tf.float32, [20, 224, 224, 3])
def select_frames(path):
    """Select representative frames for video.

    Ignore some frames both at begin and end of video.

    Args:
        path: Path of video.
    Returns:
        frames: list of frames.
    """
    frames = list()
    image_files = list(sorted(glob(path + '/*.jpg')))
    total_frames = len(image_files)
    print total_frames
    # video_data = skvideo.io.vread(path)
    # total_frames = video_data.shape[0]

    # Ignore some frame at begin and end.
    for i in np.linspace(0, total_frames, 22)[1:21]:
        video_data = skimage.io.imread(image_files[int(i)])
        img = Image.fromarray(video_data)
        img = img.resize((224, 224), Image.BILINEAR)
        frame_data = np.array(img)
        frames.append(frame_data)

        # frame_data = video_data[int(i)]
        # img = Image.fromarray(frame_data)
        # img = img.resize((224, 224), Image.BILINEAR)
        # frame_data = np.array(img)
        # frames.append(frame_data)
    return frames
def extract(sess, path):
        frames = select_frames(path)
        # We usually take features after the non-linearity, by convention.
        feature = sess.run( feed_dict={inputs: frames})
        return feature

meta_path = '/home/zhangwenqiao/Project/VideoQA/util/ResNet-L152.meta'
model_path = '/home/zhangwenqiao/Project/VideoQA/util/ResNet-L152.ckpt'
saver = tf.train.import_meta_graph(meta_path)

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    saver.restore(sess, model_path)
    graph = tf.get_default_graph()
    prob_op = graph.get_operation_by_name('prob')
    prediction = graph.get_tensor_by_name('prob:0')
    extract(sess,'/home/zhangwenqiao/Project/VideoQA/video/MSVD/output/vid1')
