# Webfishing-Calculator
A Webfishing calculator for getting the chances of getting certain fishes at certain rarity with a specific bait (or not).

All data used in this project is taken from https://webfishing.wiki.gg/, visit for more info.

This script is very simple to use, just run it and select what you want to calculate.

This is an exemple of how you could use it to calculate getting the Leedsichthys fish at the Alpha rarity:

<img width="839" height="282" alt="Screenshot 2026-01-09 081524" src="https://github.com/user-attachments/assets/82189d78-a6d8-4bb0-9063-d6c784e40e2f" />

Here is the first step, you need to select the bait you want to use, or use the "Auto" option (the option I used for this tutorial) for selecting the best bait for a certain rarity that we will select later. To select and option type the number related to that option or type the name of the option.

<img width="363" height="729" alt="Screenshot 2026-01-09 082200" src="https://github.com/user-attachments/assets/9282f877-c516-4ef5-a01d-a9796cd4842e" />

This is the second step, where you will need to select wich fish you want to catch, also showing the fish tier. The selection method is the same as previous step. This step also limits the choices of fishes depending on the bait you chose, for example, selecting the "Worm" will only show you Tier 1 and 2 fishes, while all other show all fishes due to not having restrictions.

<img width="137" height="160" alt="Screenshot 2026-01-09 083824" src="https://github.com/user-attachments/assets/decb4e91-f5ef-4790-916f-8e3601290f47" />
<img width="488" height="124" alt="Screenshot 2026-01-09 083331" src="https://github.com/user-attachments/assets/d3e549c9-35e7-4de6-9cff-c47b789afac5" />

This is the last and final step, where you select the rarity that you want to get, in this step it also have an error in case the bait you chose can not get a certain rarity (for example trying to use crickets to get an Alpha rarity fish).

<img width="1410" height="240" alt="Screenshot 2026-01-09 083253" src="https://github.com/user-attachments/assets/f4dd67fd-529e-45c5-9471-d4c165b502f6" />

This is the result of your calculation, and for some fishes it also have a note to guide you into getting it!


# Mod Usage
This project is very customizible, so using it with mods that adds different fishes, baits and/or rarities is very easy!

You can add different fishes, baits and/or rarities just by modifing the data.json file:

<img width="612" height="26" alt="Screenshot 2026-01-09 084838" src="https://github.com/user-attachments/assets/45bc2f94-c73b-4e43-b966-1092bfa0c803" />

Modify this to add new rarities (make sure to change accordingly the chance of each bait, even the vanilla ones).

<img width="201" height="99" alt="Screenshot 2026-01-09 085413" src="https://github.com/user-attachments/assets/d8b2e525-95fc-4948-8e14-3f259f182d50" />

Modify this to add new baits, you can modify the chances of each bait and even select tiers that are allowed, if there is no "allowed_tiers" fields within the bait field, it will be considered as allowing all tiers. The chances must be put in order related to the rarity field (make sure to change accordingly the chance and allowed tiers of each bait, even the vanilla ones).

<img width="212" height="174" alt="Screenshot 2026-01-09 090246" src="https://github.com/user-attachments/assets/e501a94d-21eb-4f53-ad53-5bb95baf6b65" />

Modify this to add new fishes, you can also modify chances and tiers of vanilla fishes and/or add notes to them!

# Things I want to say

If you read trough all of this I want to say thanks for taking some of your time to see my project, this is a personal project I did very fast just so I could get all acheivments, so it is probably not perfect, but I am willing to update it (sometimes), I am also planing a web version so you don't have to install the application to use it, I hope you enjoy it!

