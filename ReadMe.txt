# Gan_Painter
This Deep Learning Project is based on GAN algorithm to do piaiting new fake images.
In this project we have a folder named Images. In this folder we have a Cubism 
folder. 
Our dataset is some thousands of images which located in imgaes/cubism.

This project has three seperated files to generating new images. 

1.Create_Dataset.py
	Reads all images files from images/cubism and resizing then to 128*128 pixel.
	After resizing all images, storing all 128*128 *images in single file named
	"training_data.npy". This is a numpy file that stores all images. We use this file
	for easy loading all dataset file

2.View_Images.py
	This file is developed for testing previous phase. In this phase, loads the "View_Images.py"
	file and loads all images by one bye and shows by Cv2.imshow.

3.GAN_Painters.py
	This is main GAN phase to generating fake paiting image files.
	This phase hase two neural network to generating nad discriminating painting images.
	The first neural network(NN) is Generator. This neura network receive the dataset images as input
	and trained the images y Convolutional neral network and generated the new images.
	The Second neural is discriminator. After training and generating images by generator
	and inspect all images and discriminated all fake and real images and detect
	type of file as Fake and Real. After finishing epochs, generator neural network
	predicts final fake image and we will save 28 fake images in output folder.

Note: Order of running python files:
1.Create_Dataset.py
2.View_Images.py

