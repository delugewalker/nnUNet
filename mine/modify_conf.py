import os
import pickle
import numpy as np

"""修改训练计划中的参数，例如batch_size和patch_size等。"""

pkl_path = '/workspace/Datasets/nnUNet/nnUNet_preprocessed_data/Task082_BraTS2020/'
pkl_name = 'nnUNetPlansv2.1_plans_3D.pkl'
pkl_file = os.path.join(pkl_path, pkl_name)
plans = pickle.load(open(pkl_file, 'rb'), encoding='utf-8')

# 查看原来的参数
print(plans['plans_per_stage'][0]['batch_size'])
print(plans['plans_per_stage'][0]['patch_size'])

# 修改原来的参数
plans['plans_per_stage'][0]['batch_size'] = 2
#
# # 保存到默认的路径下，这样才能被识别，必须以_plans_2D.pkl或者_plans_3D.pkl结尾；可以按照以下方式命名方便通过文件名识别batchsize的大小
# pkl_name_new = 'nnUNetPlansv2.1_plans_3D_bs2.pkl'
pkl_file_new = os.path.join(pkl_path, pkl_name)

with open(pkl_file_new, 'wb') as f:
    pickle.dump(plans, f)
