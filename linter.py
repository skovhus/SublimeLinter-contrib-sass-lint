#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Kenneth Skovhus
# Copyright (c) 2015 Kenneth Skovhus
#
# License: MIT
#

"""This module exports the sass-lint plugin linter class."""

import re

from SublimeLinter.lint import NodeLinter


class Sass(NodeLinter):

    """Provides an interface to the sass-lint executable."""

    cmd = ('sass-lint', '--verbose', '--no-exit', '--format', 'stylish')
    config_file = ('--config', '.sass-lint.yml', '~')
    npm_name = 'sass-lint'
    syntax = ('css', 'sass', 'scss', 'vue')
    regex = (
        r'^\s+(?P<line>\d+):(?P<col>\d+)'
        r'\s+((?P<error>error)|(?P<warning>warning))'
        r'\s+(?P<message>.+)'
    )
    regex_error_config = re.compile(
        r'^YAMLException: (?P<msg>.*)'
    )
    regex_error_sass_parse = re.compile(
        r'^Error: Parsing error at .*:(?P<msg>.*#(?P<line>\d*))'
    )
    regex_error = re.compile(
        r'^(\w*)Error: (?P<msg>.*)'
    )
    tempfile_suffix = '-'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.2.0'
    selectors = {
        'vue': 'source.sass.embedded.html'
    }

    def find_errors(self, output):
        """
        Parse errors from linter's output.

        We override this method to improve sass-lint error handling.
        """

        for line in output.splitlines():
            match = self.regex_error_sass_parse.match(line)
            if match:
                items = match.groupdict()
                try:
                    line = int(items['line']) - 1
                except ValueError:
                    line = 0
                return [(match, line, None, "Error", None, items['msg'], None)]

            match = self.regex_error_config.match(line)
            if match:
                msg = 'Config file invalid: {}'.format(match.group('msg'))
                return [(match, 0, None, "Error", "", msg, None)]

            match = self.regex_error.match(line)
            if match:
                msg = 'sass-lint failed: {}'.format(match.group('msg'))
                return [(match, 0, None, "Error", "", msg, None)]

        return super().find_errors(output)

    def tmpfile(self, cmd, code, suffix=''):
        """Run an external executable using a temp file to pass code and return its output."""
        # check if <style> tag exists
        match_style_open_tag = re.search(r'^\s*<style[^>]*>', code)
        if match_style_open_tag:
            open_tag = match_style_open_tag.group(0)

            # determine `suffix` by `lang` attribute
            match_lang = re.search(r'lang="([^"]+)"', open_tag)
            if match_lang:
                suffix = '.' + match_lang.group(1)

            # remove style tags
            code = re.sub(r'^\s*<style[^>]*>', '', code)
            code = re.sub(r'</style>\s*$', '', code)

        return super(Sass, self).tmpfile(cmd, code, suffix)

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method to make the message more compact.
        """
        match, line, col, error, warning, message, near = super().split_match(match)
        if message:
            words = message.split()
            message = '{}. ({})'.format(' '.join(words[:-1]), words[-1])

        return match, line, col, error, warning, message, near
