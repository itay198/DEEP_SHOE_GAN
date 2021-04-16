# DEEP_SHOE_GAN

Our first try was to implement a regular shallow GAN net with the classic ut-zap50k-images
Data Set which consists of 136X102 images (mostly).
in this one we recived pretty much poor results.
You can see that try in the SHOECGAN file.

After that We concluded a deep GAN net might improve the results, so we explored for
a deep GAN net architecture, and the results became much much better.
We enable to creat Shoe, Boot, Sandal or Slipper images.
You can see the final results in the file **SHOE_GAN256_DEEP.ipynb**.

We also started the opttion to make functoinality to the data set 
in the file attributeClassifier.py.
in this one you can take images from the data set, and decide which one has more from an attribute.
for running the attribute classifier insert 2 arguments: 
1. path to directory with the desired pictures.
2. the desired atrribute.
