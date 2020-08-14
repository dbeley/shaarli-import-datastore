import json
import time
import datetime

with open("datastore.json", "r") as f:
    content = json.loads(f.read())

HEADER = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<!-- This is an automatically generated file.
     It will be read and overwritten.
     Do Not Edit! -->
<TITLE>My links</TITLE>
<H1>Shaarli export of all bookmarks from datastore.php</H1>
<DL><p>"""

FOOTER = "</DL><p>"

print(HEADER)

for i in content:
    # TODO better timezone handling
    timestamp = int(
        datetime.datetime.strptime(
            i["created"]["date"], "%Y-%m-%d %H:%M:%S.000000"
        ).timestamp()
    )
    print(
        f"""<DT><A HREF=\"{i['url']}\" ADD_DATE=\"{timestamp}\" PRIVATE=\"{i['private']}\" TAGS=\"{i['tags']}\">{i['title']}</A>
<DD>{i['description']}"""
    )

print(FOOTER)
