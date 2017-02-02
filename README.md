# Premultiply-Alpha-in-Folder
#####Make sure you have backup of the folder, since this tool rewrites all the images!

Python script that recursively premultiplies alpha for specified folder 

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
