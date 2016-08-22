import sys
import json

from collections import OrderedDict
from operator import itemgetter
from clarifai.client import ClarifaiApi


def main(argv):

    clarifai_api = ClarifaiApi() # assumes environment variables are set.

    with open('data.json') as data_file:    
        apiResult = json.load(data_file)

    #apiResult = clarifai_api.tag_images(open('C:\\images\\Buildings\\45ad67e6.jpg', 'rb'))

    #with open('data.txt', 'w') as outfile:
    #    json.dump(apiResult, outfile)

    apiResult = apiResult['results'][0]
    tagsResults = apiResult['result']['tag']
    tagMap = dict()

    # Normalize the data, as it's in parallel arrays
    for tag, conf in zip(tagsResults['classes'], tagsResults['probs']):
        tagMap[tag] = conf

    # Sort tags by confidence value, descending, because why not.
    tagMap = OrderedDict(sorted(tagMap.items(), key=itemgetter(1), reverse=True))

    print(json.dumps(tagMap, sort_keys=False, indent=4))
        
if __name__ == '__main__':
  main(sys.argv)