Extension for [ulauncher](https://ulauncher.io/) to visit your files anytime, anywhere.

![help](images/0.png)

The *searchfile* extension use command `locate` to locate file.

Currently it has two modes.

1. Search by basename, equivalent to `locate -b`

![basename search](images/1.png)

2. Raw mode, which pass all argument directly into `locate`. The flowing screenshot demonstrates how to use regex to match files with subfix `png` in `searchfile` direcory:

![regex search](images/2.png)

Press Alt+Number to open files using `xdg-open`.

Alternative, you can press Alt-Enter to switch to copy-to-clipboard menu.

![copy-to-clipboard menu](images/3.png)