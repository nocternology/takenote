# Takenote
Takenote is a CLI utility to take notes without leaving your terminal !

Takenote will automatically create a DB file in your home directory. 
You can add, remove and list notes for now.

Any help, comments or PR are welcome :)

# Install
Clone the repo somewhere on your computer
```
git clone https://github.com/nocternology/takenote.git
```
Make the 'takenote' script executable
```
chmod +x takenote
```
Drop a link into one of your path's directories
```
ln -s /where/you/cloned/the/repo/takenote /one/of/your/path's/directories/takenote
```
for example : 
```
ln -s /home/user/takenote/takenote /usr/bin/takenote
```

# Use examples
## Listing your notes
```
takenote list # Lists all of your notes
takenote list -c TODO # Lists all notes under the "TODO" category
```
## Adding a note
```
takenote add Merge branch "dev" with "master" after fixing the typo # Adds a note under the "DEFAULT" category
takenote add -c TODO Do the stuff about the thing # Adds the note under the given category (TODO)
```
## Deleting a note
```
takenote del -c TODO # Delete all notes under the "TODO" category
takenote add -n 19 # Delete the note with the ID 19 (IDs are listed with the list command)
```


# License
The MIT License (MIT)

Copyright (c) 2015 nocternology

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
