
# OSINT The Creator 2
Solved By: RJCyber

## Description:
Wow Charlie even set up a linkedin account, but not well it is kind of a mess. Is the PR nightmare here??

The inner content of this flag begins with "pr"

## How to "Capture the Flag":
If we take a look at the website (from the previous Chaplin's PR Nightmare challenges): https://www.charliechaplin.dev/, we see that the Contact Us page says this, "You can also find us on Linkedin, but you will have to search for us I forget what our name is, either like "Charlie Chaplin Coding or Development" or "C3D" something like that." Using this as a hint, we find that his LinkedIn account is https://www.linkedin.com/in/charlie-chaplin-dev/. Then, we scroll down and see that he had an event called "Top Hat Development Night." After creating a personal LinkedIn account, we are able to search this event up. The page of the event (https://www.linkedin.com/events/6822753659445743616/) contains the flag.

# Flag:
```uiuctf{pr0f3s5iOn@l_bUs1n3sS_envIroNm3n7}```
