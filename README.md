# shaarli-import-datastore

If you only have your old datastore.php and can't copy-paste it in your new instance (either because you don't have shell access or the new database is already populated), follow these instructions to create an html file from a datastore.php file you can import in the shaarli web UI.

## Requirements

- bash
- php
- jq
- python

## Instructions

Assuming your database is called datastore.php and is in the same directory as the scripts :

```
chmod +x read_datastore.sh
./read_datastore.sh > datastore.json
python convert_json_to_html.py > content.html
```

You can then import the content.html file in shaarli (Tools > Import links).
