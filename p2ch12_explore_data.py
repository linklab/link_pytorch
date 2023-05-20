import copy
import numpy as np
import matplotlib.pyplot as plt

import torch
from p2ch12.dsets import getCandidateInfoList, getCt, LunaDataset
from util.util import xyz2irc

# candidateInfo_list = getCandidateInfoList(requireOnDisk_bool=False)
# print(len(candidateInfo_list))
# print(candidateInfo_list[0])

# from p2ch12.vis import findPositiveSamples, showCandidate
# positiveSample_list = findPositiveSamples()


augmentation_dict = {}
augmentation_list = [
    ('None', {}),
    ('flip', {'flip': True}),
    ('offset', {'offset': 0.1}),
    ('scale', {'scale': 0.2}),
    ('rotate', {'rotate': True}),
    ('noise', {'noise': 25.0}),
]
ds_list = [
    LunaDataset(sortby_str='label_and_size', augmentation_dict=augmentation_dict)
    for title_str, augmentation_dict in augmentation_list
]

# print(ds_list)

all_dict = {}
for title_str, augmentation_dict in augmentation_list:
    all_dict.update(augmentation_dict)
all_ds = LunaDataset(sortby_str='label_and_size', augmentation_dict=all_dict)

augmentation_list.extend([('All', augmentation_dict)] * 3)
ds_list.extend([all_ds] * 3)

# for ds in ds_list:
#     print(len(ds))

sample_ndx = 100
sample_ndx = 154
sample_ndx = 155

sample_tup = all_ds[sample_ndx]
print(sample_tup[0].shape, sample_tup[1:])
