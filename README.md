# repobee-timestamp
A simple plugin that hooks into the `repobee clone` command and extracts the
timestamp of the latest commit in the cloned student repos.

## Install
You can install the latest version directly from the repo with `pip`:

```
$ python3 -m pip install --user --upgrade git+https://github.com/slarse/repobee-timestamp.git
```

The same command can be used to upgrade to a new version.

## Usage
After installing, you can activate `timestamp` when running the `clone` command.

```
$ repobee -p timestamp clone ...
```

It will produce output on the following form:

```
hook results for slarse-task-2

timestamp: SUCCESS
'Fri Sep 6 15:52:01 2019 +0200'
```

# License
See [LICENSE](LICENSE) for details.
