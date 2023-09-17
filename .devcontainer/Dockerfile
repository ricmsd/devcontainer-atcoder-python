FROM pypy:3.10-7.3.12

ENV PATH /opt/pypy/bin:$PATH

# install commands and libraries
WORKDIR /build
COPY requirements.txt requirements.txt
RUN apt update && \
    apt install -y sudo gfortran libopenblas-dev libgeos-dev nodejs npm time && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    pypy3 get-pip.py && \
    pip3 install -r requirements.txt && \
    pip3 install git+https://github.com/not522/ac-library-python && \
    pip3 install online-judge-tools && \
    npm install -g atcoder-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* requirements.txt

# new user
ARG USERNAME=atcoder
ARG UID=10000
ARG GROUPNAME=atcoder
ARG GID=10000
ARG HOMEDIR=/home/${USERNAME}
RUN groupadd -g ${GID} ${GROUPNAME} && \
    useradd -d ${HOMEDIR} -s /bin/bash -g ${GROUPNAME} -u ${UID} -m ${USERNAME} && \
    echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

# change default timezone
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# setup for AtCoder competition
WORKDIR ${HOMEDIR}
COPY bash_aliases .bash_aliases
COPY main.py .config/atcoder-cli-nodejs/python/main.py
COPY template.json .config/atcoder-cli-nodejs/python/template.json
RUN chown -R ${USERNAME}.${GROUPNAME} . && \
    chmod 700 .config

USER ${USERNAME}
RUN acc config default-task-choice all && \
    acc config default-template python
