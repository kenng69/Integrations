#
# MIT License
#
# Copyright (c) 2017 Frederik Mikkelsen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import sys
import requests

url = "https://ci.fredboat.com/app/rest/buildQueue"

payload = '''
<build>
    <buildType id="FredBoat_Integration"/>
    <comment><text>Integration build triggered by {}</text></comment>
    <properties>
        <property name="env.{}" value="{}"/>
    </properties>
</build>
'''

projName = os.environ["TEAMCITY_PROJECT_NAME"]

payload = payload.format(projName,
                         projName.upper() + "_BRANCH",
                         os.environ["BRANCH"])

headers = {
    'content-type': "application/xml",
}

username = os.environ["INTEGRATION_USER"]
password = os.environ["INTEGRATION_PASSWORD"]

response = requests.request("POST", url, data=payload, headers=headers, auth=(username, password))

print(response.text)

if response.status_code < 200 | response.status_code > 299:
    sys.exit(-1)
