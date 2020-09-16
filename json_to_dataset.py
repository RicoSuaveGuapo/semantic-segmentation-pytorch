import labelme
import os, sys




if __name__ == "__main__":
    mode = 'val'
    kind = 'U100'
    path=f"/home/rico-li/Job/豐興鋼鐵/data/clean_data_20frames/{kind}/images/{mode}"
    dest = f"/home/rico-li/Job/豐興鋼鐵/data/clean_data_20frames/{kind}/annotations/{mode}"
    dirs = os.listdir(path)
    dirs = [dir for dir in dirs if dir.endswith('.json')]
    dirs = [os.path.join(path,dir) for dir in dirs]
    

    for i, item in enumerate(dirs):
        json_name = item.split('/')[-1].split('.')[0]
        os.system("labelme_json_to_dataset "+item+" --save "+dest)