#!/usr/bin/env python3

from sys import argv
from os import path
from dataclasses import dataclass
from datetime import datetime, date, timedelta
from glob import glob

from common import CALENDAR_DIR

@dataclass
class DatetimeNote:
    title: str
    date: date
    next_date: date

    def __str__(self) -> str:
        def f(d):
            day = datetime.strftime(d, "%-d %B")
            return datetime.strftime(d, f"%9A, {day:>11s} %Y")
        date_str = f(self.date)
        return f"{date_str}: {self.title}" + ("" if self.next_date is None else f" (next in {self.next_date})")

def parse_datetimenote(filename: str) -> date:
    title = None
    date = None
    new_date = None
    with open(filename, "r") as fd:
        for line in map(lambda x: x.strip(), fd):
            if line.startswith("# "):
                title = line[2:]
            elif line.startswith("Date: "):
                date_str = line[len("Date: "):]
                date = datetime.strptime(date_str, "%d.%m.%Y")
            elif line.startswith("Period: "):
                period_str = line[len("Period: "):]
                period_cnt, period_size = int(period_str[:-1]), {
                    'y': lambda d: datetime(day=d.day, month=d.month, year=d.year+1),
                    'm': lambda d: datetime(day=d.day, month=d.month+1, year=d.year),
                    'w': lambda d: datetime(day=d.day+7, month=d.month, year=d.year),
                    'd': lambda d: datetime(day=d.day+1, month=d.month, year=d.year),
                }[period_str[-1]]
                #new_date = date
                #for _ in range(period_cnt):
                #    new_date = period_size(new_date)
                # TODO: advance
    if title is None or date is None:
        raise ValueError()
    return DatetimeNote(
        title=title,
        date=date,
        next_date=new_date
    )

def take_while(p, xs):
    for x in xs:
        if p(x):
            yield x
        else:
            break

datetimenotes = sorted(
    [parse_datetimenote(f) for f in glob(path.join(CALENDAR_DIR, "*.md"))],
    key=lambda dn: dn.date
)

tomorrow_datetime = datetime.fromordinal(date.today().toordinal()) + timedelta(days=1)

if len(argv) > 1:
    # TODO: open file/advance
    iterr = take_while(lambda dtn: dtn.date < tomorrow_datetime, datetimenotes)
else:
    iterr = datetimenotes
for line in iterr:
    print(line)
