from google_images_download import google_images_download
import urllib
import random
import string


def find_image(search_label):
    response = google_images_download.googleimagesdownload()

    search_query = search_label

    arg = {
        "keywords":search_query,
        "format":"jpg",
        "limit":100,
        "no_download":True,
        "silent_mode":True
    }

    pre = "static/"
    name = ""
    ext = ".jpg"

    test = response.download(arg)
    query = test[0][search_query][random.randint(0 , 100)]
    chars=string.ascii_uppercase + string.digits
    name = name.join(random.choice(chars) for _ in range(5))
    saveext = pre+name+ext
    saved = name+ext
    print(saveext)
    output_img = urllib.request.urlretrieve(str(query), saveext)
    return str(saved)