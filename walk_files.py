import os
from PIL import Image

f = open('walk_files_results.txt', 'w')

for filepath, dirnames, filenames in os.walk('UAV-benchmark-M'):
    for filename in filenames:
        img_path = os.path.join(filepath, filename)
        img_file = Image.open(img_path)
        width, height = img_file.size
        dataset, group, img = img_path.split('\\')
        f.write(dataset + '/images/' + group + '/' + img + '\n')
        label_path = './labels_with_ids/' + group
        label_name = img.replace('.jpg', '.txt')
        if not os.path.exists(label_path):
            os.makedirs(label_path)
        label_file = open(label_path + '/' + label_name, 'w')
        gt_file = open('./GT/' + group + '_gt.txt', 'r')
        gt_list = []
        for line in gt_file.readlines():
            line_split = line.split(',')
            frame, id, p1, p2, p3, p4 = int(line_split[0]), int(line_split[1]), int(line_split[2]), int(line_split[3]), int(line_split[4]), int(line_split[5])
            if frame == int(img[3:9]):
                gt_list.append([0, id, (p1+p3/2)/width, (p2+p4/2)/ height, p3/ width,
                                p4 / height])
        to_write = ''
        for i in gt_list:
            to_write += '0 ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3]) + ' ' + str(i[4]) + ' ' + str(i[5]) + '\n'
        label_file.write(to_write)
        label_file.close()
