# RINA-ACC
Have not decided if rina-acc is short for rina-accessories or rina-accoutrement

## Forker beware!
Some things don't work even between Pythons locally (in-vs-out of a conda env)

### Included

**genfd.py**: **GEN**erates **F**ilename and **D**ate

**peanutbuttervibes.py**: GUI for creating posts (.md files) on local machine

**pbv2.py**: PeanutButterVibes version2 creates the GUI within its own class.  Also has some differences to make it work with `writepost.sh`

**writepost.sh**: This shell script runs pbv2 in an conda env (because that is the way my Python install is set up), and does the staging/committing/pushing of *only* the file made by running pbv2.

#### In beta

**almondbuttervibes.py**: Almond butter is like a fancier version of peanut butter.  Note for self: Tkinter doesn't support drag-and-drop from finder to get a file's path :(

### Ideas

OMG I can include an ASSET box in my GUI that I can copy to the public/post-assets directory.  i'm a genius this is how I can upload media (at least from desktop)

Next: Version of write-post I can write for script over SSH via iPhone