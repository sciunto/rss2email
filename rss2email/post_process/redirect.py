# Copyright (C) 2013 Francois Boulogne <fboulogne at april dot org>
#
# This file is part of rss2email.
#
# rss2email is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) version 3 of
# the License.
#
# rss2email is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# rss2email.  If not, see <http://www.gnu.org/licenses/>.

"""Remove redirections on the post URL.

Several websites use redirections (e.g. feedburner) for various reasons like
statistics. you may want to avoid this for privacy or for durability.

This hook finds and uses the real url behind redirections.
"""

import urllib
import re

def process(feed, parsed, entry, guid, message):
    # decode message
    encoding = message.get_charsets()[0]
    content = str(message.get_payload(decode=True), encoding)

    # Get the link
    link = entry['link']

    # Remove the redirection and modify the content
    direct_link = urllib.request.urlopen(link).geturl()
    content = re.sub(re.escape(link), direct_link, content, re.MULTILINE)

    message.set_payload(content, charset=encoding)

    return message
