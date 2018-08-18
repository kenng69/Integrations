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
import subprocess


def cloneGit(url: str, branch_id: str):
    branch_id = branch_id[5:]  # Remove "refs/"

    if branch_id.startswith("pull/"):
        # This is a pull request
        subprocess.check_call(["git", "clone", url, "--single-branch"])
        subprocess.check_call(["git", "fetch", "origin", branch_id + ":pr"])
        subprocess.check_call(["git", "checkout", "pr"])
    else:
        # This is a normal branch
        subprocess.check_call(["git", "clone", url,
                               "-b", branch_id.replace("heads/", ""), "--single-branch"])


fredboatBranch = os.getenv("FREDBOAT_BRANCH", "refs/heads/development")
lavalinkBranch = os.getenv("LAVALINK_BRANCH", "refs/heads/dev")

cloneGit("https://github.com/Frederikam/FredBoat", fredboatBranch)
cloneGit("https://github.com/Frederikam/Lavalink", lavalinkBranch)
