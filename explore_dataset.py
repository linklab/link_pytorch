import copy
import numpy as np
import matplotlib.pyplot as plt

import torch
from p2ch10.dsets import getCandidateInfoList, getCt, LunaDataset, Ct
from p2ch10.vis import findPositiveSamples, showCandidate
from util.util import xyz2irc

import time


def traverse_dataset(dataset):
    start = time.time()

    num_positive_samples = 0
    for idx, data in enumerate(dataset):
        print("Num: {0:>5}, Candidate Sample: {1}, Bool: {2}, UID: {3}, CenterIRC: {4}".format(
            idx, data[0].shape, data[1], data[2], data[3]
        ))
        if data[1][1] == 1:
            num_positive_samples += 1

    print("TOTAL: {0} - POSITIVE: {1}, NEGATIVE: {2}".format(
        len(dataset), num_positive_samples, len(dataset) - num_positive_samples
    ))
    end = time.time()

    print(end - start)


def draw_ct(series_uid):
    showCandidate(series_uid)
    # ct = Ct(series_uid)

    # img_numpy = ct_t.numpy()
    # print(img_numpy.shape)
    # img = Image.fromarray(img_numpy[0, 1], 'RGB')
    # img.save('my.png')
    # img.show()


def draw_sample(data_candidate_t):
    from PIL import Image
    img_numpy = data_candidate_t.numpy()
    print(img_numpy.shape)
    img = Image.fromarray(img_numpy[0, 1], 'RGB')
    img.save('my.png')
    img.show()


def main():
    dataset = LunaDataset()
    traverse_dataset(dataset)
    draw_ct(series_uid="1.3.6.1.4.1.14519.5.2.1.6279.6001.511347030803753100045216493273")
    draw_sample(dataset[0][0])


if __name__ == "__main__":
    main()
