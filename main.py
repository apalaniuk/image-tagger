import sys
import json

from collections import OrderedDict
from operator import itemgetter
from clarifai.client import ClarifaiApi
from os.path import isfile, join

det 


def main(argv):
    
    config = {
        'input_images_dir' : './',
        'output_dir' : 'output'
    }

    clarifai_api = ClarifaiApi() # assumes environment variables are set.

    # Create the output directory
    if not os.path.exists(settings('output_dir')):
        os.makedirs(settings('output_dir'))

    processImages(config['input_images_dir'])

processImages(directory):
    inputDirs = os.walk(directory).dirs

    # Loop through all input directories.
    if inputDirs.length == 0:
        # Process all images in this leaf directory
        inputImages = os.walk(directory).filenames
        inputImages = [ img for img in inputImages if img.endswith('.jpg'')]

        for imageName in inputImages:
            processImageFake(imageName)
    else:
        #Recurse through subdirectory
        for inputDir in inputDirs:
            processImages(inputDir)

processImageFake(image):
    print('Processing ' + image)
        
processImage(apiRef):
    apiResult = clarifai_api.tag_images(open('C:\\images\\Buildings\\45ad67e6.jpg', 'rb'))

    apiResult = apiResult['results'][0]['result']
    tagsResults = apiResult['tag']
    tagMap = dict()

    # Normalize the data, as it's in parallel arrays
    for tag, conf in zip(tagsResults['classes'], tagsResults['probs']):
        tagMap[tag] = conf

    # Sort tags by confidence value, descending, because why not.
    tagMap = OrderedDict(sorted(tagMap.items(), key=itemgetter(1), reverse=True))

    print(json.dumps(tagMap, sort_keys=False, indent=4))
        
if __name__ == '__main__':
  main(sys.argv)