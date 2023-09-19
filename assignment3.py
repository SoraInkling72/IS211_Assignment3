import argparse
# other imports go here
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
args = parser.parse_args()
main(args.url)


def downloadData(url):
    """Downloads the data"""
    import urllib.request

    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    return response
def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
