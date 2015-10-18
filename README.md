SublimeLinter-contrib-sass-lint
================================

[![Build Status](https://travis-ci.org/skovhus/SublimeLinter-contrib-sass-lint.svg?branch=master)](https://travis-ci.org/skovhus/SublimeLinter-contrib-sass-lint)

This linter plugin for [SublimeLinter][docs] provides an interface to [sass-lint][sass-lint] (Node.js). It will be used with files that have Sass and SCSS syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `sass-lint` is installed on your system. To install `sass-lint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `sass-lint` globally by typing the following in a terminal:
   ```
   npm install -g sass-lint
   ```

**Note:** This plugin requires `sass-lint` 1.2.0 or later. Check your version with `sass-lint --version`.

### Linter configuration
In order for `sass-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `sass-lint`, you can proceed to install the `SublimeLinter-contrib-sass-lint` plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `sass-lint`. Among the entries you should see `SublimeLinter-contrib-sass-lint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure `sass-lint` options with a `.sass-lint.yml`. If a `.sass-lint.yml` file is not found in the file hierarchy starting with the linted file, your home directory will also be searched. For more information, see the [sass-lint page][sass-lint]. Default configuration file can be found [here][sass-lint-default-config].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[sass-lint]: https://github.com/sasstools/sass-lint
[sass-lint-default-config]: https://github.com/sasstools/sass-lint/blob/master/lib/config/sass-lint.yml
