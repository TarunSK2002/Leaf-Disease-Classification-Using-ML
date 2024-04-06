import os
import random
random.seed(1234)


base_dir = r"C:\Users\Tarun_SK\OneDrive\Desktop\DATASET\images"
subdirs = ['Healthy', 'CedarAppleRust', 'Scab', 'Combinations']

out_dir = r"D:\project\FGVC-Plant-Pathology-2020-challenge-dataset--master\AppleDiseaseClassifyCode\data_split"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

val_ratio = 0.2

train_val_list = []
train_list = []
val_list = []
for subdir in subdirs:
    for item in sorted(os.listdir(os.path.join(base_dir, subdir, '2048px'))):
        if item[-4:] != '.jpg':
            continue

        fpath = os.path.join(base_dir, subdir, '2048px', item)
        label = subdir

        data_item = (label, fpath)

        train_val_list.append(data_item)

        if random.random() < val_ratio:
            val_list.append(data_item)
        else:
            train_list.append(data_item)


def write_to_file(fpath, data_list):
    with open(fpath, 'w') as fp:
        for data_item in data_list:
            label, fpath = data_item
            fp.write('{}\t{}\n'.format(label, fpath))


write_to_file(os.path.join(out_dir, 'train_val.txt'), train_val_list)
write_to_file(os.path.join(out_dir, 'train.txt'), train_list)
write_to_file(os.path.join(out_dir, 'val.txt'), val_list)

print('# train items: {}'.format(len(train_list)))
print('# val items: {}'.format(len(val_list)))
