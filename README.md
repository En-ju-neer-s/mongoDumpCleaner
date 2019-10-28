# mongoDumpCleaner
With this code you can clean a mongo dump to make it openrefine readable


## How to use

In the folder you have the script pulled make a directorty with all your dumped json. Give the name of the directory to the code and try to make up a funny for a folder for the clean json. The moment you run this script all the dumped data will be cleaned and put in the clean folder.

## TODO

rewrite the part where we store eveything in one var. Keep track of the object and when the object is done then write it to the file so we write a object to the instead everything at ones.

By doing this we can also easily write a check were we can look if the object is the same and throw away the old object if it isnt correct and throw it away if it isnt correct.
