# Feedback Survey
Solved By: RJCyber

# Description:
CS1 ciphers go brrrrr
Attachment: https://uiuc.tf/files/7702cafa765d3b0197d7b9a084393d40/chal?token=eyJ1c2VyX2lkIjoyNDAsInRlYW1faWQiOjI2LCJmaWxlX2lkIjozOX0.YQgUlg._uXiJIBCynikh3OynqDRY0Lde60

# How to "Capture the Flag":
After downloading the file provided in the description, we can run the command ```strings chal | grep flag```. By doing this, we can see that the flag is encrypted in Caeser Cipher (by the shift of 12): ```azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o```. By decrypting this, we get: ```onsider_the_question_can_machines_thinki_propose_to_c```. We can break this up into two parts (```onsider_the_question_can_machines_think``` and ```i_propose_to_c```). By putting the second part in front of the first part, we get the flag.

# Flag:
```uiuctf{i_propose_to_consider_the_question_can_machines_think}```
