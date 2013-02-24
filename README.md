yelp!!
======
<br>
### If you are Not Manoj:

You are in a wrong space-time-repo; there is nothing useful here.

<br>
### If you are Manoj who has done time travel to future:

Hi Manoj, this script is a small, trivial python script to clean up scilab scri$
Also, you might want to know how to use this-

Currently supports multi-line un/commmenting in scilab
For help:<br>
`./yelp -h`

For commenting, check sample.sci how to use comment_markers; after which run th$
`./yelp -fc sample.sci`

#### Single Occurence of function or variable:<br>
I have strong belief that a single occurence of any variable or function in a document is **evil** 
Mostly, a single occurence of variable or function implies =>

1. That variable/function is *redundant* since its never used
2. Or worse that variable/function is a *typo*

This usually means hours of clueless debugging(and worse scilab is interpreted, so debugging one by one error)... **yelp** can save you from that.
Also one may cleverly think, what if my function is declared in some other header file, and I am using it just once in my *xyz.sci* (say). Don't worry, Manoj, yelp takes care of that too.
Usage:

`./yelp xyz.sci`


#### Options
* ***-f*** forces the script to modify the sample.sci (that is given file in *a$
* ***-c*** is for multi-line commenting
* ***-u*** is for multi-line uncommenting scilab-script which was previously co$
* ***-d*** shows you diff of what is being added/modified

PS: Manoj, finally thank @kushalbhabra for his immense contribution/support for choosing right regex statements