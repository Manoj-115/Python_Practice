#Check for url in a given string
import re

def url(url_string):


    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    match_url = url_pattern.search(url_string)
    return bool(match_url)

# url_string = "Check tbis strin gcontains this url ttps://www.geeksforgeeks.org/python-check-url-string/"
url_string = "Check tbis strin gcontains this url"

if url(url_string):
    print(f"THe given string {url} has url")
else:
    print(f"THe given string {url} has no url")
