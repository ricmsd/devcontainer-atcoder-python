# devcontainer-atcoder-python
A VSCode DevContainers setup for joining AtCoder contests and solving problems, using Python3 and PyPy3. 
Also, there is a command using ChatGPT to convert Python code to C++, allowing you to write code in Python and submit it in C++.

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
For the meanings of 'o', 'test', and 'sb', please refer to the bash_aliases file.

## Python to C++ conversion
For cases where you can't avoid TLE/MLE in Python or PyPy, we added a way to change Python code to C++ and try submitting it. We use ChatGPT to convert from Python to C++, so you need to set some environment variables in the container to use this feature. (Please create your own API key on the OpenAI website.)

```
$ export OPENAI_API_KEY=XXXXXXXXXX...
```

After that, you can convert (and compile), test, and submit your code like this:
```
$ acc new abc295
$ cd abc295/a
$ o              # edit .py file
$ test           # test .py file
$ c              # .py to .cpp with ChatGPT(gpt-3.5-turbo model) and output execution file (a.out)
$ test3          # test a.out file
$ sb3            # submit .cpp file to atcoder.jp
```
The conversion often fails, but we hope it will improve with the release of GPT-4 and beyond!

## Acknowledgment
This project is based on the [gomatofu/atcoder_python](https://github.com/gomatofu/atcoder_python) repository. Many thanks for the inspiration and guidance.
