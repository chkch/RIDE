#  Copyright 2008-2015 Nokia Solutions and Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# from robotide import robotapi
from robotide.lib.robot.running.arguments.embedded import EmbeddedArgumentParser


class EmbeddedArgsHandler(object):

    def __init__(self, keyword):
        if keyword.arguments:
            raise TypeError('Cannot have normal arguments')
        self.name_regexp, self.embedded_args = \
            EmbeddedArgumentParser().parse(keyword.name)
        if not self.embedded_args:
            raise TypeError('Must have embedded arguments')
