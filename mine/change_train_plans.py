import os
import argparse
from batchgenerators.utilities.file_and_folder_operations import *

"""分布式训练后需要转换训练计划才能执行推理，主要是将保存的模型对应的属性文件(例如model_best.model.pkl)修改为单卡训练的模式"""

def change_trainer_moduel(train_plans_file, fold):
    plans = load_pickle(train_plans_file)
    for index, item in enumerate(plans['init']):
        print(index, ':', item)
    print("plans['name']:", plans['name'])
    
    if len(plans['init']) == 11:
        old_tuple = plans['init']
        list1 = list(old_tuple)
        list1.pop(9)
        list1.pop(2)
        plans['init'] = tuple(list1)
    else:
        print("[init] don't changed")
    plans['name'] = "nnUNetTrainerV2"

    print("length of plans['init']", len(plans['init']))
    for index, item in enumerate(plans['init']):
        print(index, ':', item)
    
    print(plans['name'])
    save_pickle(plans, train_plans_file)


def read_plans(read_plans_file):
    plans = load_pickle(read_plans_file)
    # print(len(plans[1]['train']))
    print(plans['name'])


if __name__ == '__main__':

    root_path = '/workspace/Datasets/nnUNet/nnUNet_trained_models/nnUNet/'
    model = '3d_fullres'
    Task = 'Task043_BraTS2019'
    Trainer = 'nnUNetTrainerV2__nnUNetPlansv2.1'
    fold = 'all'
    # fold = 'fold_0'
    checkpoint = 'model_latest.model.pkl'
    
    train_plans_path = os.path.join(root_path, model, Task, Trainer, fold, checkpoint)


    change_trainer_moduel(train_plans_path, fold)
    print(train_plans_path)
    # read_plans(train_plans_path)