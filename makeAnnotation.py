import glob
import os
import json

def makeAnnotation(image_dir, save_dir, extension, classes):
    annDic = {}
    for img_name in sorted(glob.glob(os.path.join(images_dir, '*' + extension))):
        img_name = os.path.basename(img_name)
        for i in range(len(classes)):
            if classes[i] in img_name: class_id = i
        annDic[img_name] = class_id

    with open(os.path.join(save_dir, 'annotation.json'), 'w') as f:
        json.dump(annDic, f)

if __name__ == '__main__':
    images_dir = '/Users/kishiyuma/Desktop/obake_ai/maico_todai/'
    save_dir = images_dir
    extension = 'JPG'
    classes = ['kiku', 'maico']
    makeAnnotation()
