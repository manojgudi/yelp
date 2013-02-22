yelp!!
======

**If you are Not Manoj:**

You are in wrong space-time-repo; there is nothing useful here.


**If you are Manoj who has done time travel to future:**

Hi Manoj, this script is a small, trivial python script to clean up scilab scripts and check for nooby mistakes (which you do often).
Also, you might want to know how to use this-

Currently supports multi-line un/commmenting in scilab
For help:

`./yelp.py -h`

For commenting, check sample.sci how to use comment_markers; after which run this script
`./yelp -fc sample.sci`

*-f*  forces the script to modify the sample.sci; if not used it will write in sample_modified.sci
*-c*  is for multi-line commenting
*-u*  is for multi-line uncommenting scilab-script which was previously commented using yelp
*-d*  shows you diff of what is being added/modified

