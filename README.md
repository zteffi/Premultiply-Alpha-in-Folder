# Premultiply-Alpha-in-Folder
### Make sure you have backup of the folder, since this tool rewrites all the images!

Python script that recursively premultiplies rgb values by alpha for all .png images in a folder, i.e.:
pixel_in = (r,g,b,a)
pixel_out = (r*a, g*a, b*a)


## Installing dependencies
You need [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed. Then just run
``` shell
sudo pip install Pillow 
```

## Usage
``` 
$python Premultiply.py images
```
where images is the root folder, with subfolder 
``` 
$python Premultiply.py 'images folder'
```
Use apostropes if the folder name contains spaces
