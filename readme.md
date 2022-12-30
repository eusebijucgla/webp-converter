# Image converter to optimize images for the web.

This script iterates over all the images placed in the ./source_images folder and converts them to WEBP, a format
that is optimized for web.

## How to use
To use this converter just drop the images in the ./source_images folder and run the python script. This will automatically convert the
images to a WEBP format which is better optimized for the web.
You can select the target_size for the minimum size of your converted images, also the quality and the filter that you would need.
The default settings seem to work fine for most cases.

If you structure the images with folders inside ./source_images, the ./output_images will keep the same folder strucutre, which helps to organize the files.
Keeping the folder structure is important because the script checks if the file already exists, 
which speeds up the process if you add new images to the ./source_images folder. 

## How it works
If you organize the images in folders the converted images will also follow the same folder hierarchy. For example.

Having this structure under the ./source_images folder:
```
source_images
├───project1
│       image1.*
│       image2.*
│
└───project2
    │   image1.*
    │
    └───test
            image1.*
```
Will be exported to ./output_images like the following:
```
output_images
├───project1
│       image1.webp
│       image2.webp
│
└───project2
    │   image1.webp
    │
    └───test
            image1.webp
```

