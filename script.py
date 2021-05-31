from PIL import Image
import os


def getSizes():
    photos_sizes =[]

    for i in range(1, 79):
        photoName = f'1 ({i}).jpg'
        with Image.open(photoName) as image:

            width, height = image.size
            imageSize = (width, height)
            photos_sizes.append( imageSize)
    return photos_sizes


def orderedDictionay():
    count = {}
    photo_sizes = getSizes()
    for photo in photo_sizes:
        count.setdefault(photo, 0)    
        count[photo] = count[photo] + 1

    orderedList = [(size, fileName) for size, fileName in sorted(count.items(), key=lambda x:x[1], reverse = True)]
    orderedDict = {}
    for tu in orderedList:
        orderedDict[tu[0]] = tu[1]
    return orderedDict

def filterPhotos(numSize:int):

    for i in range(1, numSize+1):
        photoName = f'1 ({i}).jpg'
        with Image.open(photoName) as image:
            width, height = image.size
            image_size = (width, height)
            orderedDict = orderedDictionay()
            for size, number in orderedDict.items():
                if (image_size == size) and number > 1:
                    try:
                        image.save(f'{image_size}/{photoName}')
                    except:
                        os.makedirs(f'{image_size}')
                        image.save(f'{image_size}/{photoName}')

filterPhotos(numSize=78)
