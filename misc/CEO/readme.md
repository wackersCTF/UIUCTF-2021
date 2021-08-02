# CEO
by Rohans885
## Description
You just wirelessly captured the handshake of the CEO of a multi-million dollar company! Use your password cracking skills to get the password! Wrap the password in the flag format. E.g: uiuctf{password}

https://uiuc.tf/files/d123b87f0f5bc197f73d66134874f1a4/megacorp-01.cap?token=eyJ1c2VyX2lkIjo4OCwidGVhbV9pZCI6MjYsImZpbGVfaWQiOjMxfQ.YQboTA.LZ8D1bRXJCHnb4L_NQyQTT7szLg

## Solution (by xenonminer)
The challenge description talks about wirelessly capturing a handshake.

Since we have the handshake we can use aircrack-ng on the packet capture file to get the password.

We will use rockyou.txt to crack the password.

Our command will be: ```aircrack-ng -w rockyou.txt megacorp-01.cap```

We get our flag!

flag: ```uiuctf{nanotechnology}```


