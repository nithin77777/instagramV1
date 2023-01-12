
FROM python:latest
LABEL Maintainer="Nithin98"

WORKDIR /Users/nithinsaikrishna/Downloads
COPY docker/docker_assignment/hello.py ./
COPY requirements.txt ./
#COPY /Users/nithinsaikrishna/PycharmProjects/pythonProject/instagram/get_long_lived_token.py ./
COPY debug_access_token.py ./
COPY defines.py ./
RUN python -m pip install --upgrade pip
RUN pip --version
RUN pip install -r requirements.txt
CMD ["python", "./defines.py"]
CMD ["python", "./debug_access_token.py"]
#CMD ["python", "get_user_pages.py"]
#CMD ["python","./hello.py"]


