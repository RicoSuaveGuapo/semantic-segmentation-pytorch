import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
path_ADE = 'data/ADEChallengeData2016/annotations/validation/ADE_val_00000001.png'
path_MET = 'data/MetalCurvatureDetection2020/annotations/train/1500_curve_3_frame0551.png'
img_ADE = cv2.imread(path_ADE, cv2.COLOR_BGR2GRAY)
img_MET = cv2.imread(path_MET, cv2.COLOR_BGR2GRAY)

fig, axs = plt.subplots(1,2)
fig.set_figheight(15)
fig.set_figwidth(40)
axs[0].imshow(img_ADE*200)
axs[1].imshow(img_MET)
plt.show()

# print(np.min(img_ADE))
# print(img_MET[0,:,0])

# fig, axs = plt.subplots(1,3)
# fig.set_figheight(15)
# fig.set_figwidth(40)
# for i in range(3):
#     axs[i].imshow(img_ADE[...,i])
# plt.show()

# fig, axs = plt.subplots(1,2)
# fig.set_figheight(15)
# fig.set_figwidth(40)
# axs[0].imshow(img_ADE[...,0]-img_ADE[...,1])
# axs[1].imshow(img_ADE[...,0]-img_ADE[...,2])
# plt.show()

# segm_ADE = Image.open(path_ADE)
# segm_MET = Image.open(path_MET)
# segm_MET = segm_MET.convert('L')
# print(segm_ADE.size, segm_ADE.mode)
# print(segm_MET.size, segm_MET.mode)
# segm_MET.show()
# segm_ADE.show()