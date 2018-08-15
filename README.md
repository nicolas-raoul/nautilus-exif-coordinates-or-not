# nautilus-commons-upload

Do you upload images to Commons? Do you use Nautilus (or Nemo or Caja)?
Then why not have your file browser tell you what files have been uploaded already?

`nautilus-commons-upload` overlays emblems saying whether files are modified,
added, untracked etc, with a high level of detail showing the exact status of
the file including both staged and unstaged changes separately. It marks git
repos as such and displays icons on them showing whether they have changed
files, unpushed commits, etc.

## Installation

`nautilus-commons-upload` also supports Nemo and Caja. To install it for Nemo or Caja,
replace "nautilus" everywhere it appears below with "caja" or "nemo". Everything is
exactly the same since nemo and caja are forks of Nautilus that have not changed
anything relevant to this extension.

`nautilus-commons-upload` requires `python-gi`, `python-nautilus` (or `python-nemo` or
`python-caja`), the python `pathlib` library and the python `enum34` library. On Ubuntu
these are installable with: `sudo apt-get install python-gi python-pathlib
python-nautilus python-enum34`

To install `nautilus-commons-upload`, put the single python file `git-nautilus-
icons.py` in `~/.local/share/nautilus-python/extensions`, and put the icons
folder `hicolor` in `~/.icons/`. These directories might not exist, in which
case create them. You can use the following commands to do so:

```bash
cd /tmp
git clone https://github.com/nicolas-raoul/git_nautilus_icons
cd git_nautilus_icons/
mkdir -p ~/.icons
cp -r icons/hicolor ~/.icons
mkdir -p ~/.local/share/nautilus-python/extensions
cp nautilus-commons-upload.py ~/.local/share/nautilus-python/extensions
```

Then restart Nautilus with `nautilus -q` and the plugin will be loaded next time
a Nautilus window is opened.

To uninstall, simply delete `nautilus-commons-upload.py` and the `hicolor` icons
folder.

## Notes

Icons are updated every time you browse to a directory, but whilst in a
directory, Nautilus doesn't ask the extension for new icons unless it sees a
file change on disk. Tap F5 in Nautilus to force a refresh.
