import requests

def downloadAndUnzipData():
    userName = raw_input("Enter kaggle user name: ")
    pwd = raw_input("Enter kaggle password: ")

    URL1 = raw_input("Enter URL 1: ")
    URL2 = raw_input("Enter URL 2: ")
    URL3 = raw_input("Enter URL 3: ")

    dataURLs = [URL1, URL2, URL3]

    for dataURL in dataURLs:
        print 'download %s ' % dataURL
        localFileName = dataURL.split('/')[-1]

        kaggleInfo = {'UserName': userName, 'password': pwd}

        r = requests.post(requests.get(dataURL).url, data=kaggleInfo)

        f = open('/Users/lihaotian/PycharmProjects/kaggle/' + localFileName, 'w')

        for chunk in r.iter_content(chunk_size=512 * 1024):
            if chunk:
                f.write(chunk)

        f.close()
        print("Done")


if __name__ == '__main__':
    downloadAndUnzipData()