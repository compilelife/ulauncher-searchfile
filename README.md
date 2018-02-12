Extension for [ulauncher](https://ulauncher.io/) to visit your files anytime, anywhere.

![help](images/0.png)

The *searchfile* extension use command `locate` to locate file.

Currently it has two modes.

Firstly, search by basename, equivalent to `locate -b`

![basename search](images/1.png)

Secondly, raw mode, which pass all argument directly into `locate`. The flowing screenshot demonstrates how to use regex to match files with subfix `png` in `searchfile` direcory:

![regex search](images/2.png)