# -*- coding: utf-8 -*-
#
#   live-magic - GUI frontend to create Debian LiveCDs, etc.
#   Copyright (C) 2007-2008 Chris Lamb <chris@chris-lamb.co.uk>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk
import gobject

class MainView(object):
    def __init__(self):
        self.controller.view = self

    def __getitem__(self, key):
        widget = self.xml.get_widget(key)
        if widget is None:
            raise KeyError, "Widget not found: %s" % key
        return widget

    def __contains__(self, key):
        try:
            _ = self[key]
        except KeyError:
            return False
        return True
