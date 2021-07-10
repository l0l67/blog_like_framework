This is a dynamic, blog like framework based on [Tornado](https://www.tornadoweb.org/en/stable/)
It automatically adds href links for every existing file in sites/html to the index.html (you can define the location by putting this: ```<!--here-->``` in the index.html where the links should be added)

the .html files are located in sites/html/ and get updated everytime the index.html or any other .html are loaded so you dont need to restart the python script with every new file

```
root/
↳ main.py
↳ sites/
    ↳ css
      ↳ index.css
      ↳ 404.css
      ↳ you css files here... 
    ↳ html/
      ↳ index.html
      ↳ 404.html
      ↳ you html files here...
```

The port for the webserver can be changed by editing this line: ```app.listen(8888)```
