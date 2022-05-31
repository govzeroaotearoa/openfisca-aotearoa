FROM python:3-stretch
WORKDIR /openfisca

RUN pip install --upgrade pip && \
    pip install -e .
    
EXPOSE 5000

CMD [ "/usr/local/bin/openfisca", "serve", "-b", "0.0.0.0:5000" ]
