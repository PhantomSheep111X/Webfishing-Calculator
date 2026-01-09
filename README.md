# Webfishing Calculator

A Webfishing calculator for getting the chances of catching certain fish at a specific rarity, with a specific bait (or without one).

All data used in this project is taken from https://webfishing.wiki.gg/
. Visit it for more information.

This script is very simple to use: just run it and select what you want to calculate.

This is an example of how you could use it to calculate the chances of getting the Leedsichthys fish at Alpha rarity:

<img width="839" height="282" alt="Screenshot 2026-01-09 081524" src="https://github.com/user-attachments/assets/82189d78-a6d8-4bb0-9063-d6c784e40e2f" />

Here is the first step. You need to select the bait you want to use, or use the "Auto" option (the option I used for this tutorial) to automatically select the best bait for a certain rarity that we will choose later.
To select an option, type the number related to that option or type the name of the option.

<img width="363" height="729" alt="Screenshot 2026-01-09 082200" src="https://github.com/user-attachments/assets/9282f877-c516-4ef5-a01d-a9796cd4842e" />

This is the second step, where you need to select which fish you want to catch, also showing the fish tier. The selection method is the same as in the previous step.
This step also limits the available fish depending on the bait you chose. For example, selecting the "Worm" will only show Tier 1 and 2 fish, while all other baits show all fish due to not having restrictions.

<img width="137" height="160" alt="Screenshot 2026-01-09 083824" src="https://github.com/user-attachments/assets/decb4e91-f5ef-4790-916f-8e3601290f47" /> <img width="488" height="124" alt="Screenshot 2026-01-09 083331" src="https://github.com/user-attachments/assets/d3e549c9-35e7-4de6-9cff-c47b789afac5" />

This is the last and final step, where you select the rarity you want to get. In this step, there is also an error message in case the bait you chose cannot get a certain rarity (for example, trying to use Crickets to get an Alpha rarity fish).

<img width="1410" height="240" alt="Screenshot 2026-01-09 083253" src="https://github.com/user-attachments/assets/f4dd67fd-529e-45c5-9471-d4c165b502f6" />

This is the result of your calculation, and for some fish there is also a note to guide you on how to get them!

# Mod Usage

This project is very customizable, so using it with mods that add different fish, baits, and/or rarities is very easy!

You can add different fish, baits, and/or rarities simply by modifying the data.json file:

<img width="612" height="26" alt="Screenshot 2026-01-09 084838" src="https://github.com/user-attachments/assets/45bc2f94-c73b-4e43-b966-1092bfa0c803" />

Modify this section to add new rarities (make sure to adjust the chance of each bait accordingly, including the vanilla ones).

<img width="201" height="99" alt="Screenshot 2026-01-09 085413" src="https://github.com/user-attachments/assets/d8b2e525-95fc-4948-8e14-3f259f182d50" />

Modify this section to add new baits. You can change the chances of each bait and even select which tiers are allowed.
If there is no allowed_tiers field inside a bait definition, it will be considered as allowing all tiers.
The chances must be listed in the same order as the rarity field (make sure to adjust the chances and allowed tiers of each bait accordingly, including the vanilla ones).

<img width="212" height="174" alt="Screenshot 2026-01-09 090246" src="https://github.com/user-attachments/assets/e501a94d-21eb-4f53-ad53-5bb95baf6b65" />

Modify this section to add new fish. You can also change the chances and tiers of vanilla fish and/or add notes to them!

# Things I Want to Say

If you read through all of this, I want to say thanks for taking some of your time to check out my project.
This is a personal project that I made very quickly just so I could get all achievements, so it is probably not perfect. However, I am willing to update it (from time to time).

I am also planning a web version so you won’t need to install the application to use it.
I hope you enjoy it! ❤️
