### WebAPIs basics - Homework - Olha Voichyk

This repository is my solution for WebAPIs basics homework.

### How to start
1. Get the files and go to the directory where they are.
2. Install all the requirements with 
```
pip install -r requirements.txt
```
3. Open the file config.py and change 'YOUR_ACCESS_TOKEN' to your access token. 
If you don't have one, you need to get a Dropbox account and create an app (https://www.dropbox.com/developers) with file.metadata.write, files.content.write, files.content.read permissions. After that generate an access token. Notice that access token can inspire after some time.
4. If you want, you can also change the file (and its final destination in Dropbox storage) which you want to upload, but I attached test.txt, so you can test fastly.
5. Run
```
behave
pytest test.py --html=report.html
```
