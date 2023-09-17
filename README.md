# devcontainer-atcoder-python
A VSCode DevContainers setup for joining AtCoder contests and solving problems, using PyPy3.10-7.3.12.

## Tested Environment
The following environment has been tested and confirmed to work with this project.

- Windows 11 Pro
  - Visual Studio Code
    - Extensions
      - Remote Development (WSL, DevContainers, etc. included)
  - WSL 2
    - Ubuntu 22.04.2 LTS ("atcoder" user created at installation)
  - Docker Desktop

For more information on WSL2 and Docker Desktop, see the following
- [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Get started with Docker remote containers on WSL 2](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)

## Setup
First, please do the following 1-5.
1. Log in as "atcoder" user to Ubuntu on WSL2.
1. Open the cloned file with VSCode and change to the Dev Container environment.
   ```
   $ git clone https://github.com/ricmsd/devcontainer-atcoder-python.git
   $ code devcontainer-atcoder-python
   ```
1. Click 'Reopen in Container' to launch the container environment. Then wait for the Docker image to finish building (first boot only. It took about 30 minutes on my Intel Core i7 12700F PC).
1. Open a new Terminal and enter 'login'.
1. Enter your AtCoder username and password as you will be asked twice.

Setup is complete when login is successfully completed. Next time you want to use it, just login to Ubuntu with "atcoder" and run `code devcontainer-atcoder-python`.

## Usage
For example, question A in AtCoder Beginner Contest 320 is submitted as follows
```
$ acc new abc320 # download contest data
$ cd abc320/a
$ o              # edit main.py file
$ test           # test main.py file with contest data
$ sb             # submit main.py file to atcoder.jp
```
For the meanings of 'o', 'test', and 'sb', please refer to the .devcontainer/bash_aliases file.

## Acknowledgment
This project is based on the [gomatofu/atcoder_python](https://github.com/gomatofu/atcoder_python) repository. Many thanks for the inspiration and guidance.
