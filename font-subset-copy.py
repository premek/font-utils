#!/usr/bin/python

import fontforge
import sys

# source file
f = fontforge.open(sys.argv[1])
# another file for comparsion
old = fontforge.open(sys.argv[2])


fglyphs = set(map(lambda g: g.unicode, f.glyphs()))
# glyphs in the old file
oldglyphs = set(map(lambda g: g.unicode, old.glyphs()))
# intersection - glyphs available in both fonts
commonglyphs = fglyphs & oldglyphs

print len(fglyphs)
print len(oldglyphs)
print len(commonglyphs)

# for each glyph in the edited file:
for g in f.glyphs():
  # if not present in the second fontfile:
  if not g.unicode in oldglyphs:
    # remove it
    g.clear()

# save the new font - also removing some metadata to save space
f.generate(sys.argv[3], flags=('omit-instructions', 'no-hints', 'round', 'short-post'))

