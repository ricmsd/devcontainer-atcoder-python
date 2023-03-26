FROM ubuntu:22.10

ARG USERNAME=vscode
ARG UID=10000
ARG GROUPNAME=vscode
ARG GID=10000
ARG HOMEDIR=/home/${USERNAME}

RUN apt update && \
    groupadd -g ${GID} ${GROUPNAME} && \
    useradd -d ${HOMEDIR} -s /bin/bash -g ${GROUPNAME} -u ${UID} -m ${USERNAME}

RUN apt install -y sudo && \
    echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

WORKDIR /build

RUN apt install -y software-properties-common && \
    add-apt-repository ppa:pypy/ppa && \
    apt update && \
    apt install -y wget pypy3 && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    pypy3 get-pip.py && \
    apt install -y pypy3-dev && \
    apt install -y gcc g++ gfortran libopenblas-dev liblapack-dev pkg-config && \
    apt install -y libgeos-dev

RUN apt install -y python3-pip nodejs npm && \
    python3 -m pip install --upgrade pip

#COPY requirements.txt .
#RUN pip3 install -r requirements.txt
RUN pip3 install online-judge-tools && \
    npm install -g atcoder-cli

RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR ${HOMEDIR}

COPY bash_aliases .bash_aliases
COPY main.py .config/atcoder-cli-nodejs/python/main.py
COPY template.json .config/atcoder-cli-nodejs/python/template.json
RUN chown -R ${USERNAME}.${GROUPNAME} . && \
    chmod 700 .config

USER ${USERNAME}
RUN acc config default-task-choice all && \
    acc config default-template python
