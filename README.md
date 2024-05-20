# 1337ness

1337ness is an all-in-one password list generator, to be used for CTF password cracking

## Changelog

v0.3 - Added more leetscript variations, change them in the options menu!

## Installation

Clone the repo

```bash
git clone https://github.com/BrohdeXC/1337ness.git
```

Navigate into the directory
```bash
cd 1337ness
```
Add permissions to the files
```bash
chmod +x 1337NESS LeetSpeakEasy.py LeetSpeakMedium.py LeetSpeakHard.py
```
Optional - Move all files to /usr/bin/local for global access
```bash
mv ../1337ness/* /usr/local/bin/ && cd .. && rm -r 1337ness/
```

## Usage

Go into the folder and run the command
```bash
./1337NESS
```
Choose one of the options and follow the prompts to get a wordlist
```bash
 ____________ ________________________  ___________ _________ _________
/_   \_____  \\_____  \______  \      \ \_   _____//   _____//   _____/
 |   | _(__  <  _(__  <   /    /   |   \ |    __)_ \_____  \ \_____  \ 
 |   |/       \/       \ /    /    |    \|        \/        \/        \
 |___/______  /______  //____/\____|__  /_______  /_______  /_______  /
            \/       \/               \/        \/        \/        \/ 
Version 0.3                                                By: BrohdeXC
-----------------------------------------------------------------------
    1) Leet a Word
    2) Leet a List
    3) Leet w/ CeWL (By Robin Wood AKA Digininja)
    4) Append Wordlists
    5) Permutate Wordlists
    6) Options
    7) Exit
-----------------------------------------------------------------------
Please make a selection:
```

## Known Issues and Planned Updates
Issues:  No current known issues  
Planned: Make more user friendly by adding protections against already created files  
Planned: Make an installer script for easier download so you can get to cracking faster

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
