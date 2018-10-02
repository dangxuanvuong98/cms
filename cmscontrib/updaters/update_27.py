#!/usr/bin/env python3

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2016 Amir Keivan Mohtashami <akmohtashami97@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A class to update a dump created by CMS.

Used by DumpImporter and DumpUpdater.

This updater just adds the default values for the new fields related to
analysis mode (Submission.official, Contest.analysis_*).

"""

from six import iteritems


class Updater(object):

    def __init__(self, data):
        assert data["_version"] == 26
        self.objs = data

    def run(self):
        for k, v in iteritems(self.objs):
            if k.startswith("_"):
                continue
            if v["_class"] == "Submission":
                v["official"] = True
            if v["_class"] == "Contest":
                v["analysis_enabled"] = False
                v["analysis_start"] = v["stop"]
                v["analysis_stop"] = v["stop"]
        return self.objs
