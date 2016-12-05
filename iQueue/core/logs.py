import logging

from colorlog import ColoredFormatter


log_colors = {
    'DEBUG':    'cyan',
    'INFO':     'green',
    'WARNING':  'yellow',
    'ERROR':    'red',
    'CRITICAL': 'bold_red',
}


class NewColoredFormatter(ColoredFormatter):

    def __init__(self, format, datefmt=None,
                 log_colors=log_colors, reset=True, style='%'):

        super(NewColoredFormatter, self).__init__(
            format, datefmt=datefmt, log_colors=log_colors,
            reset=reset, style=style)


class CustomLogger(logging.getLoggerClass()):

    def makeRecord(self, name, level, fn, lno, msg, args,
                   exc_info, func=None, extra=None):
        rv = logging.LogRecord(name, level, fn, lno, msg, args, exc_info, func)
        pathname = rv.pathname
        filepath = '/'.join(pathname.split('/')[-2:])
        rv.__dict__.update({'filepath': filepath})

        if extra is not None:
            for key in extra:
                if (key in ["message", "asctime"]) or (key in rv.__dict__):
                    raise KeyError(
                        "Attempt to overwrite %r in LogRecord" % key)
                rv.__dict__[key] = extra[key]

        return rv
