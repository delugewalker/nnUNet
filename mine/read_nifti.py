import os
import nibabel as nib
import SimpleITK as sitk
import numpy as np

"""查看nifti文件内容。"""

# nii_path_raw = '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0000.nii.gz'  # 原始图像
# nii_path_cropped = '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0000.nii.gz'  # 裁剪后图像
# nii_path_preprocessed = '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/imagesTr/BraTS20_Training_001_0000.nii.gz'  # 预处理后图像

# nii_raw_image = sitk.ReadImage(nii_path_raw)
# nii_raw_array = sitk.GetArrayFromImage(nii_raw_image)

# nii_cropped_image = sitk.ReadImage(nii_path_cropped)
# nii_cropped_array = sitk.GetArrayFromImage(nii_cropped_image)

# nii_preprocessed_image = sitk.ReadImage(nii_path_preprocessed)
# nii_preprocessed_array = sitk.GetArrayFromImage(nii_preprocessed_image)

# print('nii_raw_array:', nii_raw_array.shape)
# print('nii_cropped_array:', nii_cropped_array.shape)
# print('nii_preprocessed_array:', nii_preprocessed_array.shape)


# nii_file = '../data/BraTS20_Training_001_0000.nii.gz'
nii_file = '../data/sitk_save.nii.gz'
seg_file = '../data/BraTS20_Training_001.nii.gz'

# nibabel读取
nii_image = nib.load(nii_file)
nii_image = nii_image.get_fdata()
nii_array = np.array(nii_image)
print('nii_array:', nii_array.shape)

nib.save(nib.Nifti1Image(nii_array, None), '../data/nib_save.nii.gz')


# SimpleITK读取
nii_image2 = sitk.ReadImage(nii_file)

direction = nii_image2.GetDirection()
origin = nii_image2.GetOrigin()
spacing = nii_image2.GetSpacing()
size = nii_image2.GetSize()

nii_array2 = sitk.GetArrayFromImage(nii_image2) # 这一步会将维度顺序变换，(240, 200, 155) -> (155, 200, 240)
print('nii_array2:', nii_array2.shape)
print('nii_array2:', nii_array2.shape)

nii_array2 = nii_array2[:, :200, :]
nii_image2 = sitk.GetImageFromArray(nii_array2) # 这一步会将维度顺序变换回去，(155, 200, 240) -> (240, 200, 155)
nii_image2.SetDirection(direction)
nii_image2.SetOrigin(origin)
nii_image2.SetSpacing(spacing)
sitk.WriteImage(nii_image2, '../data/sitk_save.nii.gz')

