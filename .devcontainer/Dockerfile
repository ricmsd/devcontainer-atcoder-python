FROM ubuntu:22.10

ARG USERNAME=vscode
ARG UID=10000
ARG GROUPNAME=vscode
ARG GID=10000
ARG HOMEDIR=/home/${USERNAME}

RUN apt update && \
    apt install -y sudo && \
    groupadd -g ${GID} ${GROUPNAME} && \
    useradd -d ${HOMEDIR} -s /bin/bash -g ${GROUPNAME} -u ${UID} -m ${USERNAME} && \
    echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

WORKDIR /build

RUN apt install -y software-properties-common wget && \
    add-apt-repository ppa:pypy/ppa && \
    apt update && \
    apt install -y pypy3 && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    pypy3 get-pip.py && \
    apt install -y python3-pip && \
    python3 -m pip install --upgrade pip

RUN apt install -y nodejs npm time && \
    pip3 install online-judge-tools && \
    npm install -g atcoder-cli

# for p2cpp.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && \
    apt install -y gcc-9 g++-9 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 10 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 10
ENV OPENAI_API_KEY=YOUR_API_KEY

# change default timezone
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR ${HOMEDIR}

COPY bash_aliases .bash_aliases
COPY main.py .config/atcoder-cli-nodejs/python/main.py
COPY template.json .config/atcoder-cli-nodejs/python/template.json
COPY p2cpp.py .local/bin/p2cpp.py
RUN chown -R ${USERNAME}.${GROUPNAME} . && \
    chmod 700 .config

USER ${USERNAME}
RUN acc config default-task-choice all && \
    acc config default-template python
