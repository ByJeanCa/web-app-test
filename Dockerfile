FROM redhat/ubi9-minimal

WORKDIR /tests

COPY app.py install_dependencies.sh test_app.py ./
COPY public/ public/

RUN chmod +x install_dependencies.sh && ./install_dependencies.sh

EXPOSE 5000

CMD ["python3", "app.py"]
