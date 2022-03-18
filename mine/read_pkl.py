import os
import pickle
import numpy as np

"""查看pkl文件内容。"""

# pkl_path = '/workspace/Datasets/nnUNet/nnUNet_cropped_data/Task082_BraTS2020/'  # 裁剪后的数据信息
pkl_path = '/workspace/Datasets/nnUNet/nnUNet_preprocessed_data/Task082_BraTS2020/nnUNetData_plans_v2.1_stage0/BraTS20_Training_001.pkl'  # 数据预处理后的数据信息
pkl_path = '/workspace/Datasets/nnUNet/nnUNet_preprocessed_data/Task082_BraTS2020/dataset_properties.pkl'  # dataset_properties.pkl路径
pkl_name = 'BraTS20_Training_001.pkl'
pkl_file = os.path.join(pkl_path, pkl_name)
plans = pickle.load(open(pkl_path, 'rb'), encoding='utf-8')

# 查看参数
for key, value in plans.items():
    print(key, ':', value)


# nnUNet_cropped_data
"""original_size_of_raw_data : [155 240 240]
original_spacing : [1. 1. 1.]
list_of_data_files : ['/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0000.nii.gz', 
                    '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0001.nii.gz', 
                    '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0002.nii.gz', 
                    '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0003.nii.gz']
seg_file : /workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/labelsTr/BraTS20_Training_001.nii.gz
itk_origin : (-0.0, -239.0, 0.0)
itk_spacing : (1.0, 1.0, 1.0)
itk_direction : (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
crop_bbox : [[4, 139], [42, 215], [49, 186]]
classes : [-1.  0.  1.  2.  3.]
size_after_cropping : (135, 173, 137)
use_nonzero_mask_for_norm : OrderedDict([(0, True), (1, True), (2, True), (3, True)])
"""

# nnUNet_preprocessed_data
"""
original_size_of_raw_data : [155 240 240]
original_spacing : [1. 1. 1.]
list_of_data_files : ['/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0000.nii.gz', 
                    '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0001.nii.gz',
                    '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0002.nii.gz',
                    '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0003.nii.gz']
seg_file : /workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/labelsTr/BraTS20_Training_001.nii.gz
itk_origin : (-0.0, -239.0, 0.0)
itk_spacing : (1.0, 1.0, 1.0)
itk_direction : (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
crop_bbox : [[4, 139], [42, 215], [49, 186]]
classes : [-1.  0.  1.  2.  3.]
size_after_cropping : (135, 173, 137)
use_nonzero_mask_for_norm : OrderedDict([(0, True), (1, True), (2, True), (3, True)])
size_after_resampling : (135, 173, 137)
spacing_after_resampling : [1. 1. 1.]
class_locations : {1: array([[ 64,  60,  14],
       [ 60, 106,  60],
       [ 66,  64,  65],
       ...,
       [ 57, 122,  30],
       [ 68,  68,  20],
       [ 69, 100,  27]]), 2: array([[60, 96, 51],
       [43, 70, 28],
       [41, 78, 43],
       ...,
       [62, 72, 31],
       [50, 69, 36],
       [61, 98, 49]]), 3: array([[76, 79, 37],
       [69, 72, 39],
       [51, 73, 37],
       ...,
       [65, 70, 37],
       [48, 61, 30],
       [48, 86, 58]])}
"""