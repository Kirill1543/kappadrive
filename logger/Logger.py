from .Level import Level
from .Mode import Mode
from .LevelError import LevelError
from .ModeError import ModeError
from .ErrorTexts import ErrorTexts


class Logger:
    def __init__(self, level=Level.OFF, file_path=None, mode=None):
        self._level = level
        self._buffer = ""
        self._buffer_max_size = 1000
        self._file_path = file_path
        self._file = None
        if mode is not None:
            self._mode = mode
        elif file_path is not None:
            self._mode = Mode.BOTH
        else:
            self._mode = Mode.CONS

    def set_file(self, path):
        self._file_path = path
        self._reset_file()
        self.turn_on_file()

    def turn_on_file(self):
        self._mode = min(Mode.BOTH, self._mode + Mode.FILE)

    def turn_on_console(self):
        self._mode = min(Mode.BOTH, self._mode + Mode.CONS)

    def turn_off_file(self):
        self._mode = max(Mode.NONE, self._mode - Mode.FILE)

    def turn_off_console(self):
        self._mode = max(Mode.NONE, self._mode - Mode.CONS)

    def console_is_on(self):
        return self._mode % 2 == 1

    def file_is_on(self):
        return self._mode // 2 == 1

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        if Mode.BOTH >= mode >= Mode.NONE:
            self._mode = mode
        else:
            raise ModeError(ErrorTexts.MODE_ERROR_TEXT)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if Level.OFF >= level >= Level.ALL:
            self._level = level
        else:
            raise LevelError(ErrorTexts.MODE_ERROR_TEXT)

    @property
    def buff_max_size(self):
        return self._level

    @buff_max_size.setter
    def buff_max_size(self, size):
            self._buffer_max_size = max(size, 0)

    @staticmethod
    def print_console(msg):
        print(msg)

    def _push_buffer(self):
        self._file = open(self._file_path, 'a')
        self._file.write(self._buffer)
        self._file.close()

    def print_file(self, msg):
        self._buffer += msg
        if len(self._buffer) >= self._buffer_max_size:
            self._push_buffer()
            self._buffer = ""

    def _reset_file(self):
        self._file = open(self._file_path, 'w')
        self._file.close()

    def log(self, msg):
        if self.console_is_on():
            self.print_console(msg)
        if self.file_is_on():
            self.print_file(msg)

    def filter(self, level):
        return self._level <= level

    def log_by_level(self, msg, level):
        if self.filter(level):
            self.log(msg)

    def fatal(self, msg):
        self.log_by_level(msg, Level.FATAL)

    def error(self, msg):
        self.log_by_level(msg, Level.ERROR)

    def warn(self, msg):
        self.log_by_level(msg, Level.WARN)

    def info(self, msg):
        self.log_by_level(msg, Level.INFO)

    def debug(self, msg):
        self.log_by_level(msg, Level.DEBUG)

    def trace(self, msg):
        self.log_by_level(msg, Level.TRACE)

    def all(self, msg):
        self.log_by_level(msg, Level.ALL)
