# RINA-ACC
Have not decided if rina-acc is short for rina-accessories or rina-accoutrement

## Forker beware!
Some things don't work well between my Pythons locally (ie, in-vs-out of a conda env)

## Included

### db: accessories for databased version of providing blog content

**add-gooey-post.py**: GUI that adds content to database.  REQUIRES SOME OF THE `psycopg2` STUFF TO BE IMPORTED FROM ANOTHER FILE

**writetodb.sh**: Shell script that runs `add-gooey-post` in a conda env (because that is the way my Python install is set up).  Shouldn't have to do any other updates?

**updatelocal.py**: Uses my generic text box to to match my local db (PC) to prod for when I send in mobile posts

**localketchup.sh**: Script to run `updatelocal` (it makes it catch up!)

### md: accessories for version of site that scrapes markdown files for content

**genfd.py**: **GEN**erates **F**ilename and **D**ate

**peanutbuttervibes.py**: GUI for creating posts (.md files) on local machine

**pbv2.py**: PeanutButterVibes version2 creates the GUI within its own class.  Also has some differences to make it work with `writepost.sh` including a (gasp!) global variable!

**writepost.sh**: This shell script runs pbv2 in an conda env (because that is the way my Python install is set up), and does the staging/committing/pushing of *only* the file made by running pbv2.  If you're using a Mac, you can even make a shortcut with this that lets you run it from the menu bar or from a keyboard shortcut.

**pouchpb.py**: Works with `mobile.sh` to create posts with user-provided title content only.  Filename and date are generated automatically.

**mobile.sh**: Handles posting via iPhone (through the Shortcuts app -> run script over SSH).  Can NOT handle the GitHub part, but iPhone hardware is not something I have influence over 😇

**autoupdate.sh**: commits and pushes any modified files to GitHub


## In beta

**almondbuttervibes.py**: Almond butter is like a fancier version of peanut butter. 
