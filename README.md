# devcontainer-atcoder-python
A VSCode DevContainers setup for joining AtCoder contests and solving problems, using Python3 and PyPy3.

## Tested Environment
The following environment has been tested and confirmed to work with this project.

- Client
  - Windows 10 Pro
    - Visual Studio Code
      - Visual Studio Code Remote - SSH
      - Visual Studio Code Dev Containers
      - Python extension for Visual Studio Code
- Server
  - Ubuntu 22.04.2 LTS
    - Docker Community Edition
- Container
  - Check `.devcontainer/Dockerfile`.

## Setup
1. First, log in to the server using VSCode's Remote - SSH feature.
1. Open the cloned file with VSCode and change to the Dev Container environment.
   ```
   $ git clone https://github.com/ricmsd/devcontainer-atcoder-python.git
   $ code devcontainer-atcoder-python
   ```
1. Click 'Reopen in Container' to launch the container environment.
1. Open a new Terminal and enter 'login'.
1. Enter your AtCoder username and password as you will be asked twice.

## Usage
```
$ acc new abc295 # download contest data
$ cd abc295/a
$ o              # edit .py file
$ test           # test .py file with contest data
$ sb             # submit .py file to atcoder.jp
```

## Acknowledgment
This project is based on the [gomatofu/atcoder_python](https://github.com/gomatofu/atcoder_python) repository. Many thanks for the inspiration and guidance.
