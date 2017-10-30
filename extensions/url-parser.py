import urlparse

# Title: URL Parsing to extract metadata
# Description: This extension is used to parse urls to extract metadata like categories.
# Required data:

# captures the Web Path
path = urlparse.urlparse(document.uri).path

categories = {}

for i, p in enumerate(path.split("/")):
    # path will start with /, so the first p (i=0) is usually empty
    if p:
        # Add categories as meta1, meta2, meta3.
        # You can use an array if you want specific names for the categories.
        categories['meta'+str(i)] = p

if len(categories):
    # Set the categories
    document.add_meta_data(categories)
