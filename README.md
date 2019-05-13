## GalleryApp
This project was generated using python version 3.6.and the Django framework. This is a gallery application. It allows a user(admin) to post pictures, add locations category and locations for the images. Other users can view the images and search for images based on category.

## SETUP INSTRUCTIONS:

### Installation
1.Python 3.6.5
2.Django 1.11

### Cloning the repository

`git clone https://github.com/yontiii/Gallery.git && cd My-Gallery`

### Creating a virtual environment
`sudo apt-get install python3.6-venv`
`python3.6 -m venv --without-pip virtual`
`source virtual/bin/activate`

### Installing dependencies
`pip install -r requirements.txt`

### Running tests
`python3.6 manage.py test photos`

### Running the Development server
`python3.6 manage.py runserver`

## BEHAVIOUR DRIVEN DEVELOPMENT
| GENERAL BEHAVIOUR | INPUT | OUTPUT|
|:------------------|:--------|:-----------|
|User wants to search for an image| They enter the search category on the search bar |all relevant images are displayed|
|User wants to view the image descriptions|They click on the image |Image descriptions are displayed|
|User(admin) wants to upload an image| They navigate to the admin route and upload the image along with its description,category and location.|Image is uploaded|


## Further help
To get more help on the Python CLI use ng help or go check out the Python CLI README and Python documentation. You may also read the news API documentation on the news API website.

## CONTACT INFORMATIONIf
For more information or clarification reach me through my email address : muasajohn01@gmail.com