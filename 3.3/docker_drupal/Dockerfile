FROM drupal:11-apache
WORKDIR /opt/drupal
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN composer require drush/drush:^13 --no-interaction --no-progress
COPY start.sh /usr/local/bin/pr3-start
RUN chmod +x /usr/local/bin/pr3-start
ENV PORT=10000
EXPOSE 10000
CMD ["/usr/local/bin/pr3-start"]
