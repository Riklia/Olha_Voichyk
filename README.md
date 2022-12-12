### WebAPIs bascis - Homework - Olha Voichyk

This repository is my solution for WebAPIs bascis homework.

### How to start
1. Get the files and go to the directory where they are.
2. Install all the requirements with 
```
pip install -r requirements.txt
```
3. Open the file config.py and change 'YOUR_ACCESS_TOKEN' to your access token. 
If you don't have one, you need to get a Dropbox account and create an app (https://www.dropbox.com/developers) with file.metadata.write, files.content.write, files.content.read permissions. After that generate an access token. Notice that access token can inspire after some time.
3. Run
```
behave
pytest test.py --html=report.html
```
