FROM jenkins/jenkins:lts-jdk21
ENV JAVA_OPTS="-Xms64m -Xmx256m -Djenkins.install.runSetupWizard=false"
ENV JENKINS_OPTS="--httpPort=10000"
COPY seed.groovy /usr/share/jenkins/ref/init.groovy.d/seed.groovy
EXPOSE 10000
