# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

"""Exceptions coverage.py can raise."""

from __future__ import annotations

class _BaseCoverageException(Exception):
    """The base-base of all Coverage exceptions."""
    pass


class CoverageException(_BaseCoverageException):
    """The base class of all exceptions raised by Coverage.py."""
    pass


class ConfigError(_BaseCoverageException):
    """A problem with a config file, or a value in one."""
    pass


class DataError(CoverageException):
    """An error in using a data file."""
    pass

class NoDataError(CoverageException):
    """We didn't have data to work with."""
    pass


class NoSource(CoverageException):
    """We couldn't find the source for a module."""
    pass


class NoCode(NoSource):
    """We couldn't find any code at all."""
    pass


class NotPython(CoverageException):
    """A source file turned out not to be parsable Python."""
    pass


class PluginError(CoverageException):
    """A plugin misbehaved."""
    pass


class _ExceptionDuringRun(CoverageException):
    """An exception happened while running customer code.

    Construct it with three arguments, the values from `sys.exc_info`.

    """
    pass


class CoverageWarning(Warning):
    """A warning from Coverage.py."""
    pass
