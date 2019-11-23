import requests, json

URL = "https://api.github.com/gists/7b6da3e88ce657fae4a5344f087d720b"

r = requests.get(url = URL)

data = r.json()

print(data["files"]["bowistweet"]["content"])

token = "d5c7b2bde8475663ae77c18e174e9d209386e4db"

heads = {"Authorization":'token %s'%token}
params={"scope":"gist"}
payload={
    "description" : "bowis",
    "files" : {
        "bowistweet" : {
            "content" : "1",
            "filename" : "bowistweet"
        }
    }
}

result = requests.patch(URL, data=json.dumps(payload),headers=heads,params=params)

print(result)

"""{
  "description": "Hello World Examples",
  "files": {
    "hello_world_ruby.txt": {
      "content": "Run `ruby hello_world.rb` or `python hello_world.py` to print Hello World",
      "filename": "hello_world.md"
    },
    "hello_world_python.txt": null,
    "new_file.txt": {
      "content": "This is a new placeholder file."
    }
  }
}"""