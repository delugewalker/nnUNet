import os
import SimpleITK as sitk
import numpy as np
import nibabel as nib

nii_file_path = '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/inferVal/'
nii_file_path_p = '/workspace/Datasets/nnUNet/nnUNet_raw_data/Task082_BraTS2020/inferVal_best_p'

os.makedirs(nii_file_path_p, exist_ok=True)

for file in os.listdir(nii_file_path):
    nii_file = os.path.join(nii_file_path, file)
    nii_file_p = os.path.join(nii_file_path_p, file)
    print(nii_file)

    nii_image = sitk.ReadImage(nii_file)
    direction = nii_image.GetDirection()
    origin = nii_image.GetOrigin()
    spacing = nii_image.GetSpacing()
    size = nii_image.GetSize()

    nii_array = sitk.GetArrayFromImage(nii_image)

    print('nii_array_unique:', np.unique(nii_array))
    print('nii_array_shape:', nii_array.shape)

    nii_array[np.where(nii_array == 3)] = 4
    nii_array[np.where(nii_array == 2)] = 5
    nii_array[np.where(nii_array == 1)] = 2
    nii_array[np.where(nii_array == 5)] = 1
    print('nii_array_unique:', np.unique(nii_array))

    nii_image = sitk.GetImageFromArray(nii_array)
    nii_image.SetDirection(direction)
    nii_image.SetOrigin(origin)
    nii_image.SetSpacing(spacing)
    sitk.WriteImage(nii_image, nii_file_p)


# for file in os.listdir(nii_file_path):
#     nii_file = os.path.join(nii_file_path, file)
#     nii_file_p = os.path.join(nii_file_path_p, file)
#     print('nii_file:', nii_file)

#     data = nib.load(nii_file)
#     data = data.get_fdata()
#     data = np.array(data, dtype='uint8')
#     print(data.shape)

#     print(np.unique(data))
#     data[np.where(data == 3)] = 4
#     data[np.where(data == 2)] = 5
#     data[np.where(data == 1)] = 2
#     data[np.where(data == 5)] = 1
#     print(np.unique(data))

#     nib.save(nib.Nifti1Image(data, None), nii_file_p)







