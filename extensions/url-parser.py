import urlparse

# Title: URL Parsing to extract metadata
# Description: This extension is used to parse urls to extract metadata like categories.
# Required data:

# captures the Web Path
path = urlparse.urlparse(document.uri).path

categories = {}

for i, p in enumerate(path.split("/")):
    if p:
        # add categories as meta1, meta2, meta3.
        # You can use an array if you want specific names for the categories.
        categories['meta'+str(i)] = p

if len(p):
    # Set the categories
    document.add_meta_data(categories)
