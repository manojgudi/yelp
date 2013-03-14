yelp!!
======
<br>
### If you are Not Manoj:

You are in a wrong space-time-repo; there is nothing useful here.

<br>
### If you are Manoj who has done time travel to future:

Hi Manoj, this script is a small, trivial python script to clean up scilab script.<br>
Also, you might want to know how to use this-

Currently supports multi-line un/commmenting in scilab
For help:<br>
`./yelp -h`

#### Multi-line un/commenting
Multi-line commenting in Scilab has been a huge pain since they believe commenting is *bad*. <br>
Anyway, *yelp* solves this problem. For multi-line commenting, place markers "##" before start of comment line and end of it.<br>
Here's one example of multi-line comment in commented_file.sci ->

<i>## Sample<br>
line<br>
to be<br>
commented ## <br>
 ## another sample<br>
line to be commented ## <br>
<br></i>
Now use yelp to add comment-<br>
`./yelp -dcf commented_file.sci`

It will output this: **check options section for more**<br>
![Commenting](https://raw.github.com/manojgudi/yelp/master/screenshots/commenting.png)

You can uncomment file commented by yelp to revert changes.<br>
`./yelp -duf commented_file` <br>
![UNCOMMENTING](https://raw.github.com/manojgudi/yelp/master/screenshots/uncommenting.png)

For experimenting, check sample.sci how to use comment_markers;

#### Options
* ***-f*** forces the script to modify the given file in argument.
* ***-c*** is for multi-line commenting
* ***-u*** is for multi-line uncommenting scilab-script which was previously commented by yelp.
* ***-d*** shows you diff of what is being added/modified

<br>
#### Single Occurence of function or variable:
I have strong belief that a single occurence of any variable or function in a document is **evil** 
Mostly, a single occurence of variable or function implies =>

1. That variable/function is *redundant* since its never used
2. Or worse that variable/function is a *typo*

This usually means hours of clueless debugging(and worse scilab is interpreted, so debugging one by one error)... **yelp** can save you from that.
Also one may cleverly think, what if my function is declared in some other header file, and I am using it just once in my *xyz.sci* (say). Don't worry, Manoj, yelp takes care of that too.
Usage (NO options should be passed):

`./yelp xyz.sci` <br>

#### Function Ouput arguments with NO return values
In scilab, we write function like this ->

`function [my_output_args] = myfunction(input_args)`<br>
`// statements`<br>
`endfunction`

now somewhere in *statements* ideally, I've to return output_args, but scilab does NOT check if all output_args have got a return value

*for example*

`function [arg1,arg2] = myfunc(data1)`<br>
`      arg1 = 1;`<br>
`endfunction`<br>

This code shouldnt work since **only** arg1 is being returned... <br>
but Scilab misses this unless arg2 is specifically called for so if i call myfunction

`some_variable = myfunc(25)    // THIS Executes`

`[var1, var2] = myfunc(25)    // THIS gives error: no variable called arg2`

Some may call this *feature*; I call it bad programming practice...


![DEBUGGING](https://raw.github.com/manojgudi/yelp/master/screenshots/debugging.png) 

For experimentation purposes, use sample.sci

PS: Manoj, finally thank **@kushalbhabra** for his immense contribution/support for choosing right regex statements;<br>and in case Manoj of future, if you think you are smarter than me, then send me suggestions/improvements here.
