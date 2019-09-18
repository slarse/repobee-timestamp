"""A RepoBee plugin that extracts the timestamp of the last commit in cloned
student repos.
"""
import pathlib
import subprocess
import sys
from typing import Union

import repobee_plug as plug

PLUGIN_NAME = "timestamp"
SYS_ENCODING = sys.getdefaultencoding()


@plug.repobee_hook
def act_on_cloned_repo(
    path: Union[str, pathlib.Path], api: plug.API
) -> plug.HookResult:
    """Extract the timestamp of the latest commit message in the student repo
    at path.

    Args:
        path: Path to the student repo.
        api: An API instance. Always None for this plugin, though.
    Returns:
        a plug.HookResult specifying the outcome.
    """
    cmd = 'git log --pretty=format:"%ad" -n 1'.split()
    proc = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=str(path)
    )
    output = proc.stdout.decode(encoding=SYS_ENCODING)
    status = plug.Status.SUCCESS if proc.returncode == 0 else plug.Status.ERROR
    return plug.HookResult(hook=PLUGIN_NAME, status=status, msg=output)
