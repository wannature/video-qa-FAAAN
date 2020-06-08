# -*- coding: UTF-8 -*-
import os
import numpy as np

def file_name(file_dir):
    result = []
    f = file(file_dir+"map", "r")
    for line in f.readlines():
        result.append(list(map(str, line.split(' '))))
    print(result)
    for root, dirs, files in os.walk(file_dir):
        continue
    for temp in result:
        for file1 in files:
           if temp[0]==file1:
                os.rename(os.path.join(file_dir, file1), os.path.join(file_dir, temp[1]))


if __name__ == '__main__':
    file_name("/home/zhangwenqiao/Project/VideoQA/video/MSVD/YouTubeClips/")