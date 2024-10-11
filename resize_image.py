import cv2 
import os 


original_path = "./real_images_1200_1024x1024/picked_real_images_1200/"
#go through all the images in the folder 
count = 0
for image_name in os.listdir(original_path):

    img = cv2.imread(original_path+image_name)

    resized = cv2.resize(img, (256, 256))

    result_path = "./real_images_1200_256x256/"

    cv2.imwrite(result_path+"resized_nearest_"+image_name, resized)