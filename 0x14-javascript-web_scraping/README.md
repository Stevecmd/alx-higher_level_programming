# 0x14. JavaScript - Web scraping

Requirements
General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. `Rules of Standard `+ `semicolons on top`. Also as reference: `AirBnB style`
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

More Info
Install Node 14
```sh

$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Install semi-standard

[Documentation](https://github.com/standard/semistandard)


`$ sudo npm install semistandard --global`

Install request module and use it

[Documentation](https://github.com/request/request)

```sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

<b>Notes</b>: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Virtual env:
```sh
virtualenv myenv
source myenv/bin/activate
deactivate
```

## Tasks
0. Readme

Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in `utf-8`
* If an error occurred during the reading, print the error object


```sh

(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ chmod +x 0-readme.js 
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./0-readme.js cisfun
C is super fun!

(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./0-readme.js doesntexist
[Error: ENOENT: no such file or directory, open 'doesntexist'] {
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist'
}
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ semistandard 0-readme.js

```

File: `0-readme.js`

1. Write me 
Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object

```sh

(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ chmod +x 1-writeme.js 
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./1-writeme.js my_file.txt "Python is cool"
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ cat my_file.txt ; echo ""
Python is cool
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ semistandard 1-writeme.js 

```

File: `1-writeme.js`

2. Status code 
Write a script that display the status code of a `GET` request.

- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`
```sh
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ sudo npm install request -g
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ chmod +x 2-statuscode.js
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ semistandard 2-statuscode.js
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404

```


File: `2-statuscode.js`

3. Star wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the `Star wars API` with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- You must use the module `request`

```sh
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ semistandard 3-starwars_title.js 
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./3-starwars_title.js 1
A New Hope
(myenv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-higher_level_programming/0x14-javascript-web_scraping$ ./3-starwars_title.js 5
Attack of the Clones

```

File: `3-starwars_title.js`

4. Star wars Wedge Antilles




File: `4-starwars_count.js`

5. Loripsum




File: `5-request_store.js`


6. How many completed?




File: `6-completed_tasks.js`

7. Who was playing in this movie?



File: `100-starwars_characters.js`

8. Right order



File: `101-starwars_characters.js`