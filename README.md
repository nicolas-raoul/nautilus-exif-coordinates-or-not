# nautilus-commons-upload-status

Do you upload images to Commons? Do you use Nautilus (or Nemo or Caja)?
Then why not have your file browser tell you what files have been uploaded already?

`nautilus-commons-upload-status` overlays emblems saying whether a file
has been uploaded to Commons already or not.
This is implemented using Commons' REST API, so an Internet connection is required.

### WARNING: This is a prototype, and it is VEEEERY SLOW, especially in folders with more than 10 images.

Pull requests welcome! :-)

## Installation

`nautilus-commons-upload-status` also supports Nemo and Caja. To install it for Nemo or Caja,
replace "nautilus" everywhere it appears below with "caja" or "nemo". Everything is
exactly the same since nemo and caja are forks of Nautilus that have not changed
anything relevant to this extension.

`nautilus-commons-upload-status` requires `python-gi`, `python-nautilus` (or `python-nemo` or
`python-caja`), the python `pathlib` library and the python `enum34` library. On Ubuntu
these are installable with: `sudo apt-get install python-gi python-pathlib
python-nautilus python-enum34`

To install `nautilus-commons-upload-status`, put the single python file `git-nautilus-
icons.py` in `~/.local/share/nautilus-python/extensions`, and put the icons
folder `hicolor` in `~/.icons/`. These directories might not exist, in which
case create them. You can use the following commands to do so:

```bash
cd /tmp
git clone https://github.com/nicolas-raoul/nautilus_commons_upload_status
cd git_nautilus_icons/
mkdir -p ~/.icons
cp -r icons/hicolor ~/.icons
mkdir -p ~/.local/share/nautilus-python/extensions
cp nautilus-commons-upload-status.py ~/.local/share/nautilus-python/extensions
```

Then restart Nautilus with `nautilus -q` and the plugin will be loaded next time
a Nautilus window is opened.

To uninstall, simply delete `nautilus-commons-upload-status.py` and the `hicolor` icons
folder.

## Notes

Icons are updated every time you browse to a directory, but whilst in a
directory, Nautilus doesn't ask the extension for new icons unless it sees a
file change on disk. Tap F5 in Nautilus to force a refresh.
