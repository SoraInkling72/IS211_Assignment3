import argparse
# other imports go here
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
args = parser.parse_args()
main(args.url)


def downloadData(url, values=None):
    """Downloads the data"""
    import urllib.request

    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    return response
def page_images(downloadData):
    import re
        items = re.search('^/.')
        image_hits = re.search('^[\.jpg , \.png , \.gif]')
    image% = re.count( image_hits / items )
    print("image% + '%'")

def popular_browser(downloadData):
    import re
        Mozilla_hits = re.search('^[Mozilla]')
        Chrome_hits = re.search('^[Chrome]')
        IE_hits = re.search('^[Expolorer]')
        Safari_hits = re.search('^[Safari]')

    def high_browser_usage
        if Mozilla_hits > Chrome_hits + IE_hits + Safari_hits:
            print('Firefox is the most used browser that day')
        elif Chrome_hits > Mozilla_hits + IE_hits + Safari_hits:
            print('Chrome is the most used browser that day')
        elif IE_hits > Mozilla_hits + Chrome_hits + Safari_hits:
            print('Internet Explorer is the most used browser that day')
        elif Safari_hits > Mozilla_hits + Chrome_hits + IE_hits:
            print('Safari is the most used browser that day')

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
