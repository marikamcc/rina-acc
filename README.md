# RINA-ACC
Have not decided if rina-acc is short for rina-accessories or rina-accoutrement

## Forker beware!
Some things don't work well between my Pythons locally (ie, in-vs-out of a conda env)

## Included

**genfd.py**: **GEN**erates **F**ilename and **D**ate

**peanutbuttervibes.py**: GUI for creating posts (.md files) on local machine

**pbv2.py**: PeanutButterVibes version2 creates the GUI within its own class.  Also has some differences to make it work with `writepost.sh` including a (gasp!) global variable!

**writepost.sh**: This shell script runs pbv2 in an conda env (because that is the way my Python install is set up), and does the staging/committing/pushing of *only* the file made by running pbv2.  If you're using a Mac, you can even make a shortcut with this that lets you run it from the menu bar or from a keyboard shortcut.

**pouchpb.py**: Works with `mobile.sh` to create posts with user-provided title content only.  Filename and date are generated automatically.

**mobile.sh**: Handles posting via iPhone (through the Shortcuts app -> run script over SSH).  Can NOT handle the GitHub part, but iPhone hardware is not something I have influence over 😇

### In beta

**almondbuttervibes.py**: Almond butter is like a fancier version of peanut butter.  Note for self: Tkinter doesn't support drag-and-drop from finder to get a file's path :(

## Ideas

OMG I can include an ASSET box in my GUI that I can copy to the public/post-assets directory.  i'm a genius this is how I can upload media (at least from desktop)
