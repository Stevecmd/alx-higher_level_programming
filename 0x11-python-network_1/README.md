# 0x11. Python - Network #1 
### Resources
[HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
[Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
[Requests package](https://pypi.org/project/requests/)

## General

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST/PUT/`etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

### Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks
0. What's my status? #0
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- You must use a `with` statement

```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ pycodestyle 0-hbtn_status.py 
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./0-hbtn_status.py | cat -e
Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
```
File: `0-hbtn_status.py`

1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- You must use the packages `urllib` and `sys`
- You are not allow to import packages other than `urllib` and `sys`
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a with statement
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ chmod +x 1-hbtn_header.py 
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ pycodestyle 1-hbtn_header.py 
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
5d802a52-6267-4c4f-a8fe-6258b984c34d
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
071142e6-3c97-4b48-b869-1bf1ee7772f5
```
File: `1-hbtn_header.py`

2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement

Please test your script in the sandbox provided, using the web server running on port 5000
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```
To confirm server availability use:
```sh
curl -d "email=hr@holbertonschool.com" http://0.0.0.0:5000/post_email
```
File: `2-post_email.py`

3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- You have to manage `urllib.error.HTTPError` exceptions and print: `Error code`: followed by the HTTP status code
- You must use the packages `urllib` and `sys`
- You are not allowed to import other packages than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./3-error_code.py http://0.0.0.0:5000
Index
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```
File: `3-error_code.py`

4. What's my status? #1
Write a Python script that fetches https://alx-intranet.hbtn.io/status

- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example (tabulation before -)
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
```
File: `4-hbtn_status.py`

5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ 
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
```
File: `5-hbtn_header.py`

6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to error check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```
File: `6-post_email.py`

7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: `Error code`: followed by the value of the HTTP status code
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./7-error_code.py http://0.0.0.0:5000
Index
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```
File: `7-error_code.py`

8. Search API
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
    - Display `Not a valid JSON` if the JSON is invalid
    - Display `No result` if the JSON is empty
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`

Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random- 
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./8-json_api.py 
No result
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./8-json_api.py a
[8446] amnirqhtfjq
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./8-json_api.py 2
No result
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./8-json_api.py b
[7094] bmofakakhke
```
File: `8-json_api.py`

9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the `GitHub API` to display your id

- You must use `Basic Authentication` with a `personal access token` as password to access to your information (only `read:user` permission is needed)
- The first argument will be your `username`
- The second argument will be your `password` (in your case, a `personal access token` as password)
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./10-my_github.py papamuziko cisfun
2531536
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./10-my_github.py papamuziko wrong_pwd
None
```
File: `10-my_github.py`

10. Time for an interview!
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```txt

Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

```

Write a Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the `repository name`
- The second argument will be the `owner name`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.

```sh

(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x11-python-network_1$ ./100-github_commits.py rails rails
0d30e84878223df68efda3b0e1741611d9682a45: Jean Boussier
a9a93368a6845579379afc250adbbda84d035af7: Petrik de Heus
126445239fa6d31ab081414a7d6d8d50fdfcb6ce: Jean Boussier
126cab3af7402efd9ce9d3195dffa43b7f6d7070: kabirpathak
fc7637103a7edc723b92a1b7fec297eede0c5cb9: heka1024
c79671cc5ca3855482745d3fd028318bc52633c1: Jean Boussier
2edad3c542d1a305600130020176b9d18c5dcedb: Jean Boussier
2410312733a253ad18a93f03ba3a64a8d11cc6ee: fatkodima
4fa56814f18fd3da49c83931fa773caa727d8096: eileencodes
71e14aa7e9d48a88b4e39322f1c6485e21511221: Eileen M. Uchitelle

```
Be careful: only 60 requests by hour by IP for unauthenticated requests [Rate limit](https://docs.github.com/en/rest?apiVersion=2022-11-28).

File: `100-github_commits.py`