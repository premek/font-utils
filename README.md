font-subset-copy.py
==========
Utility script to decrease a size of a (e.g. Chinese) TTF etc. font file by subsetting it using another file as a reference. (Useful when you don't know which glyphs you want to remove.)

For example you have a font that have all the glyphs you need but looks ugly. You have a nicer font that have 20 000 symbols and is 20MB long. This script allows you to delete all the glyphs from the large file that are not available in the second one.

You need to install "fontforge" Python module
    
    sudo aptitude install python-fontforge
  
This script can also help as a quickstart for editing fonts using python-fonforge which is great fun! More documentation is available on fontforge site: http://fontforge.github.io/python.html#fontforge

Run the script like this:

    ./copysubset.py source  reference result
    ./copysubset.py huge-and-nice.ttf  small-and-ugly.ttf new-nice-and-small.ttf
