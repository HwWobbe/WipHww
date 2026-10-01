#!/usr/bin/env python3
"""Generate a TiddlyWiki macro tiddler for Julian Date (JD) and Modified Julian Date (MJD)."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone


def gregorian_to_jd(dt: datetime) -> float:
    """Convert a UTC datetime to astronomical Julian Date."""
    year = dt.year
    month = dt.month
    day = dt.day + (
        dt.hour / 24
        + dt.minute / 1440
        + (dt.second + dt.microsecond / 1_000_000) / 86400
    )

    if month <= 2:
        year -= 1
        month += 12

    a = year // 100
    b = 2 - a + (a // 4)

    jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5
    return jd


def build_tiddler_text(now: datetime, title: str) -> str:
    jd = gregorian_to_jd(now)
    mjd = jd - 2400000.5
    created = now.strftime("%Y%m%d%H%M%S000")

    return f"""title: {title}
type: text/vnd.tiddlywiki
created: {created}
modified: {created}

\\define julianDate() {jd:.5f}
\\end

\\define modifiedJulianDate() {mjd:.5f}
\\end

''Julian Date:'' <<julianDate>>

''Modified Julian Date:'' <<modifiedJulianDate>>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--title",
        default="$:/macros/JulianDate",
        help="Tiddler title to generate (default: $:/macros/JulianDate)",
    )
    parser.add_argument(
        "--iso-utc",
        help="Optional UTC datetime in ISO format, e.g. 2026-04-25T12:00:00",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    now = (
        datetime.fromisoformat(args.iso_utc).replace(tzinfo=timezone.utc)
        if args.iso_utc
        else datetime.now(timezone.utc)
    )
    print(build_tiddler_text(now, args.title))


if __name__ == "__main__":
    main()
