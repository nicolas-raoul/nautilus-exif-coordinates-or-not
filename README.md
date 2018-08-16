# nautilus-exif-coordinates-or-not

This extension shows a small "+" overlay icon on the lower-right of pictures that have GPS coordinates.

GPS signal comes and go, sometimes even when taking 3 pictures of the same thing only 1 will have coordinates.
If you consider latitude/longitude information a positive thing, then now you can easily see which picture to choose.

It is rather fast, but still slows down Nautilus when browsing folders with many pictures. Pull requests welcome! :-)

## Installation

`nautilus-exif-coordinates-or-not` also supports Nemo and Caja. To install it for Nemo or Caja,
replace "nautilus" everywhere it appears below with "caja" or "nemo". Everything is
exactly the same since nemo and caja are forks of Nautilus that have not changed
anything relevant to this extension.

`nautilus-exif-coordinates-or-not` requires `python-gi`, `python-nautilus` (or `python-nemo` or
`python-caja`), and the python libraries `pathlib`, `enum34`, `exif` library. On Ubuntu
these are installable with: `sudo apt-get install python-gi python-pathlib
python-nautilus python-enum34 python-exif`

To install `nautilus-exif-coordinates-or-not`, put the single python file `git-nautilus-
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
cp nautilus-exif-coordinates-or-not.py ~/.local/share/nautilus-python/extensions
```

Then restart Nautilus with `nautilus -q` and the plugin will be loaded next time
a Nautilus window is opened.

To uninstall, simply delete `nautilus-exif-coordinates-or-not.py` and the `hicolor` icons
folder.

## Notes

Icons are updated every time you browse to a directory, but whilst in a
directory, Nautilus doesn't ask the extension for new icons unless it sees a
file change on disk. Tap F5 in Nautilus to force a refresh.
