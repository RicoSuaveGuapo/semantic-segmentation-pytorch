import os
import sys
from shutil import copyfile

def rename(img_path):
    image_name_list = os.listdir(img_path)
    image_name_list = [image_name for image_name in image_name_list \
         if (image_name != 'train') or (image_name != 'val')]

    image_dir_list = [os.path.join(img_path, image_name) for image_name in image_name_list]
    for i, image_dir in enumerate(image_dir_list):
        img_list = os.listdir(image_dir)
        new_img = [image_name_list[i]+'_'+img for img in img_list]
        img_list = [os.path.join(image_dir, image_name) for image_name in img_list]
        new_img = [os.path.join(image_dir, image_name) for image_name in new_img]
        _ = [os.rename(img, new_img[j]) for j, img in enumerate(img_list)]

def data_split(img_path, mode):
    assert mode in ['train','val'], 'only two modes'
    # ratio is 0.6:0.4

    image_name_list = os.listdir(img_path)
    image_name_list = [image_name for image_name in image_name_list \
         if (image_name != 'train') and (image_name != 'val')]
    image_dir_list = [os.path.join(img_path, image_name) for image_name in image_name_list]

    total = 0
    for i, image_dir in enumerate(image_dir_list):
        img_list = os.listdir(image_dir)
        img_list = [os.path.join(image_dir, image_name) for image_name in img_list]
        counts = len(img_list)
        total += counts
        counts = int(0.6 * counts)
        if mode == 'train':
            img_list = img_list[:counts]
            _ = [copyfile(img, os.path.join(img_path, 'train', img.split('/')[-1])) for img in img_list]
        else:
            img_list = img_list[counts:]
            _ = [copyfile(img, os.path.join(img_path, 'val', img.split('/')[-1])) for img in img_list]
    print(total)

if __name__ == "__main__":
    kind = ['U150','U100','A30']
    for j in kind:
        kind_path = f'/home/rico-li/Job/豐興鋼鐵/data/clean_data/{j}'
        if not os.path.exists(os.path.join(kind_path, 'train')):
            os.mkdir(os.path.join(kind_path, 'train'))
        if not os.path.exists(os.path.join(kind_path, 'val')):
            os.mkdir(os.path.join(kind_path, 'val'))
        rename(kind_path)
        mode = ['train','val']
        for i in mode:
            data_split(kind_path, i)