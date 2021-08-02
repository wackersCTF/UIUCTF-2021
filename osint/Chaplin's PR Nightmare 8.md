# Chaplin's PR Nightmare 8
Solved By: RJCyber

## Description:
Straightup doxx Charlie by finding the email he set all these accounts up with, and investigate it.

The inner content of this flag begins with "b0"

## How to "Capture the Flag":
Using the GitHub found in Chaplin's PR Nightmare 7, we can find Charlie's email by looking into the C3D-Official repository. By looking at the commit history of this repository, we can see that there is a deleted file called security.txt (https://github.com/charliechaplindev/C3D-Official/commit/ce81ede5ab18b6f4ca32ace4359c5570954dfc9b). By loading the diff of this deleted file, we get Charlie's email (charliechaplin.dev@gmail.com). Then, by taking a closer look at the description, we see that we are supposed to doxx Charlie for the flag. So, we come up with this command (using his email): ```python3 ghunt.py email charliechaplin.dev@gmail.com```. Then, we can see that there is an image, which displays the flag.

# Flag:
```uiuctf{b0rk_b0rk_1_l0v3_my_d0g<3}```
