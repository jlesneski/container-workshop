FROM centos:7

# Update OS and install Apache
#RUN yum -y update
#RUN yum -y install httpd
#RUN yum clean all
RUN yum -y update && yum -y install httpd && yum clean all

#Copy apache conf file
#COPY data/html.tar.gz /var/www/html/
#RUN tar -xvzf /var/www/html/html.tar.gz
#Copy HTML and untar
ADD data/html.tar.gz /var/www/html/

EXPOSE 80

ENV HOME /root

WORKDIR /root

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
#ENTRYPOINT ["ping"]
#CMD ["google.com"]