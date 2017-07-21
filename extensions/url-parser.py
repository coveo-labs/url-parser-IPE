from urlparse import urlparse

# Title: URL Parsing to extract metadata
# Description: This extension is used to parse urls to extract metadata like categories.
# Required data:

# captures the Web Path
path = urlparse(document_api.v1.get_meta_data_value("originaluri")[0]).path
# Set the category
try:
    category1 = "webroot" if path in ("/", "", None) else path.split("/")[1]
    document_api.v1.add_meta_data({'meta1': category1})
except:
    print("error on category1")
try:
    category2 = "webroot" if path in ("/", "", None) else path.split("/")[2]
    document_api.v1.add_meta_data({'meta2': category2})
except:
    print("error on category2")
try:
    category3 = "webroot" if path in ("/", "", None) else path.split("/")[3]
    document_api.v1.add_meta_data({'meta3': category3})
except:
    print("error on category3")
