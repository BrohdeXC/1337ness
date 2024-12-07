# 1337ness

1337ness is an all-in-one password list generator, to be used for CTF password cracking

## One Line Installation

Get the installer script, give it permissions, and run 
```bash
wget https://github.com/BrohdeXC/1337ness/raw/refs/heads/main/installer.sh && chmod +x installer.sh && ./installer.sh
```
If you don't trust it, you can go look at the installer.sh file

## Usage

Run the command  
```bash
1337NESS
```

Choose one of the options and follow the prompts to get a wordlist
```bash
 ____________ ________________________  ___________ _________ _________
/_   \_____  \\_____  \______  \      \ \_   _____//   _____//   _____/
 |   | _(__  <  _(__  <   /    /   |   \ |    __)_ \_____  \ \_____  \ 
 |   |/       \/       \ /    /    |    \|        \/        \/        \
 |___/______  /______  //____/\____|__  /_______  /_______  /_______  /
            \/       \/               \/        \/        \/        \/ 
Version 0.4.7                                              By: BrohdeXC
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
Options
```bash
-----------------------------------------------------------------------
    1) UL Case - Upper and lowercase substitutions (Fastest)
    2) Easy   - Common single letter substitutions (Default)
    3) Medium - Uncommon single letter substitutions
    4) Hard   - All possible leetspeak substitutions (Slow, Long List)
    5) Return
                Currently Selected: Easy
-----------------------------------------------------------------------
```

## Video
[![1337ness0.4.1](https://img.youtube.com/vi/QfFK4R9JtvI/0.jpg)](https://www.youtube.com/watch?v=QfFK4R9JtvI)

## Notes and Tips
If permutate has problems with certain text files, check to make sure the file does not have CRLF line terminators.  
```bash
$ file <file.txt>
Good: <file.txt>: ASCII text
Bad: <file.txt>: ASCII text, with CRLF line terminators
```
To get rid of them in vim:  
```vim
:set fileformat=unix
:w
```

## Known Issues and Planned Updates
Issue: CRLF line terminators cause problems when permutating certain text files  
Planned: Add a back key within the file selection menus  
Planned: Advanced Settings for instant hashing  
Planned: Get column size at beginning and format output accordingly  
Planned: Add an option to format wordlists and make them line by line  
Planned: Functionality for subtracting wordlists  
Planned: Integrate mp64 for masks

## Changelog
v0.4.9 - Allows the lines in the wordlist to have spaces  
v0.4.8 - Added a function to subtract lists from each other  
v0.4.7 - Added separator characters for permutations  
v0.4.6 - Progress bar is now hard coded and can work without the python module  
v0.4.5 - Temporarily removed progress bar, fixed file protection path when running globally  
v0.4.4 - Added protections for current files and checks if files exist before running  
v0.4.3 - Added progress bar and combined all python files  
v0.4.2 - Added file size to output confirmation  
v0.4.1 - Fixed an issue  
v0.4.0 - Added upper and lowercase only scripts  
v0.3.0 - Added more leetscript variations, change them in the options menu!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
