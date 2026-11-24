FROM maven:3.9-eclipse-temurin-17
WORKDIR /app
COPY pom.xml .
COPY src/ src/
RUN mvn -B -ntp package > build.log && java -jar target/maven-demo-1.0.jar check > build-result.txt && mvn --version > maven-version.txt
ENV PORT=10000
EXPOSE 10000
CMD ["java","-Xms32m","-Xmx96m","-jar","target/maven-demo-1.0.jar"]
