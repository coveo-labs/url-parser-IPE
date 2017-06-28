# url-parser-IPE
Indexing Pipeline Extension to parse a document URL and extract metadata

## Description
Simple Coveo Indexing Pipeline Extension that parses a document URL to extract some useful information/metadata.
e.g. http://mywebsite.com/section1/document-category/author/my-doc.html
--> meta1 = section1
--> meta2 = document-category
--> meta3 = author

## How to build
Create a Coveo Extension in the Coveo Admin Console. Copy/Paste the Python code.
Don't forget to also create the adequate fields in the index to store the metadata values

### The files
url-parser.py

## How to run
https://onlinehelp.coveo.com/en/cloud/extensions.htm

## Available documentation
* [Coveo Indexing Pipeline Extensions](https://onlinehelp.coveo.com/en/cloud/extensions.htm)
 
## Authors
- Gauthier Robe (https://github.com/gforce81
