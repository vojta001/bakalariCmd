# bakalariCmd
*A simple command line interface to Bakaláři software using its mobile API*

## Info
* Written in Python (both 2 and 3 is supported)
	* Tested on 2.7 and 3.6
* Mostly written in one day as a reaction to forcing Bakálaři next interface, thus making our JS [BakalariMagicActions](https://github.com/vojta001/BakalariMagicActions) (fork of [FHR's repo](https://github.com/FHRNet/BakalariMagicActions)) useless
* Uses [BakalariPy](https://github.com/vojta001/BakalariPy) (fork of [FHR's repo](https://github.com/FHRNet/BakalariPy)) for making API calls. (**Thanks FHR**)
* Opensource
	* See `LICENSE` for details

## Instalation
### The easy way
*WIP* :(
### The difficult, bad and unrecommended way
1. Install Python
	* It is probably installed
	* Python2 should be fine, but Python3 is recommended
	* `apt install python` `pacman -Syu python`...
2. Clone this repo
	* If you don't have git, install it (see the first step)
	* `git clone --recurse-submodules https://github.com/vojta001/bakalariCmd`
	* `git clone --recurse-submodules git@github.com:vojta001/bakalariCmd.git`
3. Run the main file
	* `cd /path/to/bakalariCmd && python main.py`
	
## Configuration
If you don't want to type all the details for `login` command, you may pass the in an environment variable. In turn you store your credentials on your drive, which is not very secure.
### Less recommended (and secure) method
Add any of theese into your `.bashrc` file:
```
export bakalariUrl=<url (usually <name>.bakalari.cz/[bakalari])>
export bakalariUsr=<username>
export bakalariPas=<password>
```
### More recommended (and secure) method
1. Choose a directory (depending on your distribution, `~/.bin`, `~/.local.bin` or similar may be a good choice)
2. Create a file there (name it however you want to call this script in the future)
```
#!/bin/bash
(cd "/path/to/bakalariCmd" && bakalariUrl="<url (usually <name>.bakalari.cz/[bakalari])>" bakalariUsr="<username>" bakalariPas="<password>" python "$PWD/main.py")
```
3. Make it executable
	* `chmod u+x <fileName>`
4. Make it unreadable by others (because it contains your credentials)
	* `chmod go-rwx
5. Update your `$PATH`.
Insert this into your `.bashrc`
```
export PATH="/chosen/dir:$PATH"
6. Relogin
7. The name of the file from step 2 can be used to run this script
	* If a named it `bakalari` (e.g. ~/.local/bin/bakalari), I may just type `$ bakalari`
```
## Bugs
* It is not a proper Python package. You gotta run it from its directory
* Its feature set is poor
* No error handling
	* Network timeout causes it to fail completely
