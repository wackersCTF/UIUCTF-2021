# Chaplin's PR Nightmare 8
Solved By: RJCyber

## Description:
Straightup doxx Charlie by finding the email he set all these accounts up with, and investigate it.

The inner content of this flag begins with "b0"

## How to "Capture the Flag":
Using the GitHub found in Chaplin's PR Nightmare 7, we can find Charlie's email by looking into the C3D-Official repository (https://github.com/charliechaplindev/C3D-Official). 

<img width="1430" alt="Screen Shot 2021-08-02 at 12 08 15 PM" src="https://user-images.githubusercontent.com/86359182/127911512-d992c651-4fb5-445d-b2e3-497b4f6ce2ca.png">

By looking at the commit history of this repository (https://github.com/charliechaplindev/C3D-Official/commits?author=charliechaplindev&since=2021-07-01&until=2021-08-01), we can see that there is a deleted file called security.txt (https://github.com/charliechaplindev/C3D-Official/commit/ce81ede5ab18b6f4ca32ace4359c5570954dfc9b). 

<img width="1397" alt="Screen Shot 2021-08-02 at 12 16 28 PM" src="https://user-images.githubusercontent.com/86359182/127912075-4e0b56be-4586-4978-9194-d9073df4a1e2.png">

By loading the diff of this deleted file, we get Charlie's email (charliechaplin.dev@gmail.com). Then, by taking a closer look at the description, we see that we are supposed to doxx Charlie for the flag. 

<img width="1440" alt="Screen Shot 2021-08-02 at 12 10 47 PM" src="https://user-images.githubusercontent.com/86359182/127911526-83817c5b-27e4-4e8b-b593-eed0c444fe9d.png">

Then, we come up with this command (using his email): ```python3 ghunt.py email charliechaplin.dev@gmail.com```. Then, we can see that there is an image, which displays the flag.

![osint8](https://user-images.githubusercontent.com/86359182/127911773-8bb371f6-d5a0-41f1-a464-20ba2d447a04.png)


# Flag:
```uiuctf{b0rk_b0rk_1_l0v3_my_d0g<3}```
