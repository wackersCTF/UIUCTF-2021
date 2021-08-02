#  Pwn Warmup 
by Thomas
## Description
Hmm this time we arent just going to give you the flag like last year... What can you do?!

https://uiuc.tf/files/6f5b64a420c67f853fedfcd67aaf1b18/challenge?token=eyJ1c2VyX2lkIjo4OCwidGVhbV9pZCI6MjYsImZpbGVfaWQiOjM0fQ.YQbu5Q.mylq8rsOkuhaoqBol10tVwkm9oc

```nc pwn-warmup.chal.uiuc.tf 1337```

## Solution
Open the file they gave you with ghidra and see that this is a normal gets buffer overflow exploit challenge.

So there is a main function that makes a call to a vulnerable function and there is also a give_flag function which is where we want to get to.

Running the program shows us that it already gives us the memory address of give_flag so we just need to add it to an offset.

On ghidra, the offset says it was assigned 8 buffer size but we need to include the padding of 12 so our offset is 20.

Now we are going to make the exploit with pwntools.

Our main payload being sent will be: ```b'A'*20 + p64(memaddress)```

But now when we run the program from the netcat server they gave us, we realize that the memory address are always going to change so we have to find some way to take their memory address as a variable and resend it back.

To do that we need to take their input, split their output to us by spaces, and take the last item of the list.

Then we need to format it and change it back to hex from a string to send it back.

We get our flag when running the program!!

flag: ```uiuctf{k3b0ard_sp@m_do3snT_w0rk_anYm0r3}```

