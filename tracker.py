import csv
import os.path
import re


class MarvelTracker(object):
    """This class keeps track of your watching"""
    """of content in the marvel cinemtatic universe"""

    def __init__(self, csvName):
        super(MarvelTracker, self).__init__()
        self.csvName = self.add_csv(csvName)
        self.copyName = self.add_csv(csvName + "_begun")
        self.trackedFile = []
        self.regexes = [
            {
                "regex": re.compile('(next)( +)([0-9]+)( +)(item)'),
                "function": self.get_next_n_items
            },
            {
                "regex": re.compile('(watch(?:ed)?)( +)([0-9]+)( +)(item)'),
                "function": self.mark_watch_n_items
            },
            {
                "regex": re.compile('(unwatch(?:ed)?)( +)([0-9]+)( +)(item)'),
                "function": self.unwatch_n_items
            },
            {
                "regex": re.compile('(help)'),
                "function": self.help
            },
            {
                "regex": re.compile('(get info)'),
                "function": self.get_info
            },
            {
                "regex": re.compile('(get categories)'),
                "function": self.get_categories
            }
        ]
        if not os.path.isfile("./" + self.copyName):
            file = open(self.csvName, 'rb')
            read_orig = csv.reader(file)
            self.make_copy(read_orig)
        else:
            file = open(self.copyName, 'rb')
            read_copy = csv.reader(file)
            self.trackedFile = list(read_copy)
        self.available_categories = set(
            [t[2].lower() for t in self.trackedFile[1:] if t[2] is not ''])
        self.current_categories = self.available_categories
        temp = '(' + '|'.join(map(lambda x: x,
                                  self.available_categories)) + ')'
        set_reg = '(set categories)( +)(' + temp + ',)*' + temp + '$'
        self.regexes.append({
            "regex": re.compile(set_reg),
            "function": self.set_categories
        })

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.copyName, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(self.trackedFile)

    def __enter__(self):
        return self

    def make_copy(self, orig):
        allData = []
        row = next(orig)
        row.append("watched")
        allData.append(row)
        for row in orig:
            row.append(False)
            allData.append(row)
        self.trackedFile = allData

    def add_csv(self, csvName):
        return csvName + ".csv"

    def str2bool(self, v):
        if isinstance(v, bool):
            return v
        return v.lower() in ("yes", "true", "t", "1")

    def matchesCategories(self, i):
        return self.trackedFile[i][2].lower() in self.current_categories

    def get_next_n_items(self, n):
        cur = 0
        i = 1
        print("==========NEXT {0} ITEMS==========".format(n))
        while cur < n and self.guard_bounds(i):
            if not self.str2bool(self.trackedFile[i][3]) and \
                    self.matchesCategories(i):
                cur += 1
                print("{0}:\t{1}".format(cur, self.trackedFile[i][0]))
            i += 1
        print("==========NEXT {0} ITEMS==========".format(n))

    def mark_watch_n_items(self, n):
        cur = 0
        i = 1
        while self.guard_bounds(i):
            if not self.str2bool(self.trackedFile[i][3]) and cur < n and \
                    self.matchesCategories(i):
                self.trackedFile[i][3] = True
                cur += 1
            i += 1

    def unwatch_n_items(self, n):
        cur = 0
        i = len(self.trackedFile) - 2
        while i > 1 and self.guard_bounds(i):
            if self.str2bool(self.trackedFile[i][3]) and \
                    not self.str2bool(self.trackedFile[i + 1][3]) and \
                    self.matchesCategories(i):
                break
            i -= 1
        while cur < n and self.guard_bounds(i) and \
                self.matchesCategories(i):
            self.trackedFile[i][3] = False
            i -= 1
            cur += 1

    def set_categories(self, user_input):
        self.current_categories = [
            t for t in self.available_categories if t in user_input]

    def guard_bounds(self, n):
        return n < len(self.trackedFile) and n >= 0

    def get_categories(self, _):
        print("==========GET Categories==========")
        print("Current Categories:")
        print(','.join(self.current_categories))
        print("Available Categories:")
        print(','.join(self.available_categories))
        print("==========GET Categories==========")

    def get_info(self, _):
        print("==========GET INFO==========")
        watched = [t for t in self.trackedFile if self.str2bool(t[3])]
        unwatched = [t for t in self.trackedFile if not self.str2bool(t[3])]
        minutes = sum([int(t[1]) for t in watched if t[1].isdigit()])
        minutesTotal = sum([int(t[1]) for t in unwatched if t[1].isdigit()])
        print("\t{0} pieces of content".format(len(watched)))
        print("\t{0} minutes of content".format(minutes))
        print("\t{0} pieces of content left".format(
            len(self.trackedFile) - len(watched)))
        print("\t{0} minutes of content left".format(
            minutesTotal - minutes))
        print("==========GET INFO==========")

    def help(self, _):
        print("==========HELP==========")
        print("Available commands")
        print("\t* Help")
        print("\t\t* Get the available commands")
        print("\t* Next n items")
        print("\t\t* Display the next {n} items you need to watch")
        print("\t* Watched n items")
        print("\t\t* Mark that you watched {n} items")
        print("\t* Unwatched n items")
        print("\t\t* Unmark that you watched {n} items," +
              "maybe you want to rewatch some more, or you messed up marking")
        print("\t* Get info")
        print("\t\t* Get some basic metadata")
        print("\t* Get categories")
        print("\t\t* Get avaialble categories for filtering")
        print("\t* Set categories (comma seperated categories)")
        print("\t\t* Set avaialble categories to filter")
        print("\t\t* Example: Movie,Tv,Other")
        print("\t* Exit")
        print("\t\t* Self explanatory")

    def get_action(self, user_input):
        nums = [int(s) for s in user_input.split() if s.isdigit()]
        for r in self.regexes:
            if r["regex"].match(user_input):
                r["function"](nums[0] if len(nums) > 0 else user_input)


if __name__ == '__main__':
    with MarvelTracker("InitialSheet") as tracker:
        print("Welcome to your marvel tracker!!!")
        user_input = ""
        while user_input != "exit":
            user_input = raw_input("What action would you like to do?\n> ")
            tracker.get_action(user_input.lower())
