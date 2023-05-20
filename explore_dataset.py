import copy
import numpy as np
import matplotlib.pyplot as plt

import torch
from p2ch10.dsets import getCandidateInfoList, getCt, LunaDataset
from p2ch10.vis import findPositiveSamples
from util.util import xyz2irc

#######################################################################################################################

# candidateInfo_list = getCandidateInfoList(requireOnDisk_bool=False)
# print(len(candidateInfo_list))
# print(candidateInfo_list[0])
#
# positiveInfo_list = [x for x in candidateInfo_list if x.isNodule_bool]
# print("positiveInfo_list:", len(positiveInfo_list))
# diameter_list = [x.diameter_mm for x in positiveInfo_list]
#
# for i in range(0, len(diameter_list), 100):
#     print('{:4}  {:5.3f} mm'.format(i, diameter_list[i]))
#
# for candidateInfo_tup in positiveInfo_list[:10]:
#     print(candidateInfo_tup)
#
# print()
#
# for candidateInfo_tup in positiveInfo_list[-10:]:
#     print(candidateInfo_tup)
#
# print()
#
# for candidateInfo_tup in positiveInfo_list:
#     if candidateInfo_tup.series_uid.endswith('565'):
#         print(candidateInfo_tup)
#
# host, bin_edges = np.histogram(diameter_list)
# print(host)
# print(bin_edges)

#######################################################################################################################

# from p2ch10.vis import findPositiveSamples, showCandidate
# positiveSample_list = findPositiveSamples()
# print(len(positiveSample_list))
# print(positiveSample_list[0])
#
# series_uid = positiveSample_list[11][2]
# print(series_uid)
# showCandidate(series_uid)
#

######################################
import time
dataset = LunaDataset()

# start = time.time()
#
# num_positive_samples = 0
# for idx, data in enumerate(dataset):
#     print("IDX: {0:>5}, Candidate Sample Shape: {1}, Bool: {2}, Center_IRC".format(
#         idx, data[0].shape, data[1], data[2]
#     ))
#     if data[1][1] == 1:
#         num_positive_samples += 1
#
# print("TOTAL: {0} - POSITIVE: {1}, NEGATIVE: {2}".format(
#     len(dataset), num_positive_samples, len(dataset) - num_positive_samples
# ))
# end = time.time()
#
# print(end - start)

def draw_sample(data_candidate_t):
    from PIL import Image
    img_numpy = data_candidate_t.numpy()
    print(img_numpy.shape)
    img = Image.fromarray(img_numpy[0, 1], 'RGB')
    img.save('my.png')
    img.show()


# augmentation_dict = {}
# augmentation_list = [
#     ('None', {}),
#     ('flip', {'flip': True}),
#     ('offset', {'offset': 0.1}),
#     ('scale', {'scale': 0.2}),
#     ('rotate', {'rotate': True}),
#     ('noise', {'noise': 25.0}),
# ]
# ds_list = [
#     LunaDataset(sortby_str='label_and_size', augmentation_dict=augmentation_dict)
#     for title_str, augmentation_dict in augmentation_list
# ]
#
# # print(ds_list)
#
# all_dict = {}
# for title_str, augmentation_dict in augmentation_list:
#     all_dict.update(augmentation_dict)
# all_ds = LunaDataset(sortby_str='label_and_size', augmentation_dict=all_dict)
#
# augmentation_list.extend([('All', augmentation_dict)] * 3)
# ds_list.extend([all_ds] * 3)
#
# # for ds in ds_list:
# #     print(len(ds))
#
# sample_ndx = 100
# sample_ndx = 154
# sample_ndx = 155
#
# sample_tup = all_ds[sample_ndx]
# print(sample_tup[0].shape, sample_tup[1:])
