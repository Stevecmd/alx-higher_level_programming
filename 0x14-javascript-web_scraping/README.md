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



File: `0-readme.js`

1. Write me 



File: `1-writeme.js`

2. Status code 



File: `2-statuscode.js`

3. Star wars movie title




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