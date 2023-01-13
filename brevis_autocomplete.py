import sublime
import sublime_plugin
from .completion_db import CLASSES

class BrevisCompletions(sublime_plugin.EventListener):
    def __init__(self):
        self.class_completions = [("%s \tBrevis Class" % s, s) for s in CLASSES]

    def on_query_completions(self, view, prefix, locations):
        current_scope = view.scope_name(locations[0]).strip()
        if "string.quoted" in current_scope and "text.html" in current_scope:

            # place search cursor one word back
            cursor = locations[0] - len(prefix) - 1

            # dont start with negative value
            start = max(0, cursor - 250)

            # get part of buffer
            line = view.substr(sublime.Region(start, cursor))

            # split attributes
            parts = line.split('=')

            # is the last typed attribute a class attribute?
            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        else:
            return []
