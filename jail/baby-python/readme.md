# Baby_Python
author: tow_nater
## Description
here's a warmup jail for you :) Python version is 3.8.10 and flag is at /flag

Note: this chal is not actually broken, just thought it would be a funny joke

nc baby-python.chal.uiuc.tf 1337
## Solution (s)
I wasn't able to solve this challenge during the ctf, but found it pretty interesting. Apparently, there were a couple of ways to do this:

### Solution 1
Apparently, the payload ```from code import interact as exit``` gives you a terminal where you could run ```cat flag.txt``` though I wasn't able to get this working, probably because the ctf ended a while ago and the server isn't running this challenge anymore.

