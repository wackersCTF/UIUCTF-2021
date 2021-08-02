# dhke_adventure
Solved By: RJCyber

# Description:
Za smoother warudo. nc dhke-adventure.chal.uiuc.tf 1337

Attachment: https://uiuc.tf/files/9865d770d8dd75a2ffa05834e26fffd4/dhke_adventure.py?token=eyJ1c2VyX2lkIjoyNDAsInRlYW1faWQiOjI2LCJmaWxlX2lkIjoxOH0.YQgy0w.b3KjsBoVgjt_bCtO_8oGCknuccU

# How to "Capture the Flag":
Looking at the name of the challenge gives us a bit of a hint. DHKE stands for Diffie Hellman Key Exchange. After downloading the attached python file, we see that the flag is indeed being encrypted using DHKE (Dio and Jotaro are used instead of Alice and Bob).

This script can be used to decrypt the flag:

```
while b"uiuctf" not in ctext:
    print(ctext[:100])
    for i in range(len(ALPHABET)):
    try:
        newctext = base_n_decode(ctext,i)
        if all([c in ALPHABET for c in newctext[:100]]) or b"uiuctf" in newctext:
            ctext = newctext
        except:
            pass
    print(ctext)
```
# Flag:
```uiuctf{give_me_chocolate_every_day_7b8b06}```
