#Image base Ubuntu
FROM ubuntu:latest
#Instalation des depots et dependances necessaires
RUN apt-get update && apt-get install -y python3 python3-pip
#Copie les fichier sh et py
COPY shifumi.sh /shifumi.sh
COPY Shifumi.py /Shifumi.py
#Permissions de avec chmod
RUN chmod +x /shifumi.sh
#execution
CMD ["/shifumi.sh"]
