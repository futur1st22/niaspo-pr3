FROM couchbase:community-7.6.2
USER root
RUN apt-get update && apt-get install -y --no-install-recommends python3 && rm -rf /var/lib/apt/lists/*
COPY app.py /opt/pr3/app.py
ENV PORT=10000
ENV ERL_FLAGS="+S 1:1 +A 2"
EXPOSE 10000
ENTRYPOINT ["python3","-u","/opt/pr3/app.py"]
