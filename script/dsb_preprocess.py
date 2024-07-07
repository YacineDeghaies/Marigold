import os 

images_dir = '/vol/fob-vol3/mi20/deghaisa/code/Marigold/input/1_source_sequence'
depth_dir = '/vol/fob-vol3/mi20/deghaisa/code/Marigold/input/2_gt_depth'


#zip returns an iterator over tuples in the form of (image1, depth1), (image2, depth2), etc..
for image_file, depth_file in zip(os.listdir(images_dir), os.listdir(depth_dir) ):
    #Construct full path of images
    img_full_path = os.path.join(images_dir, image_file)
    depth_full_path = os.path.join(depth_dir, depth_file)

    all_split_filenames = '/vol/fob-vol3/mi20/deghaisa/code/Marigold/data_split/dsb/all_splits_filenames.txt'

    with open(all_split_filenames, 'a') as file:
        file.write(img_full_path+' '+depth_full_path + '\n')

# train_ratio = 0.8
# val_ratio = 0.1
# test_ratio = 0.1
