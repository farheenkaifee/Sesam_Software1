#-*- coding:utf-8 -*-

"""
This file is part of openexp.

openexp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

openexp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with openexp.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.sketchpad_elements._base_element import base_element

class textline(base_element):

	"""
	desc:
		A text element for the sketchpad.
	"""

	def __init__(self, sketchpad, string):

		"""
		desc:
			Constructor.

		arguments:
			sketchpad:		A sketchpad object.
			string:			A definition string.
		"""

		defaults = [
			(u'x'			, 0),
			(u'y'			, 0),
			(u'text'		, None),
			(u'center'		, 1),
			(u'color'		, sketchpad.get(u'foreground')),
			(u'font_family'	, sketchpad.get(u'font_family')),
			(u'font_size'	, sketchpad.get(u'font_size')),
			(u'font_bold'	, sketchpad.get(u'font_bold')),
			(u'font_italic'	, sketchpad.get(u'font_italic')),
			(u'html'		, u'yes'),
			]
		super(textline, self).__init__(sketchpad, string, defaults=defaults)

	def draw(self):

		"""
		desc:
			Draws the element to the canvas of the sketchpad.
		"""

		properties = self.eval_properties()
		self.canvas.set_font(style=properties[u'font_family'],
			size=properties[u'font_size'],
			italic=properties[u'font_italic'] == 'yes',
			bold=properties[u'font_bold'] == 'yes')
		self.canvas.text(properties[u'text'],
			center=properties[u'center']==1,
			x=properties[u'x'], y=properties[u'y'],
			color=properties[u'color'],
			html=properties[u'html']==u'yes')
