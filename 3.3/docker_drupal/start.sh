#!/bin/sh
set -eu
cd /opt/drupal
mkdir -p web/sites/default/files
if [ ! -f web/sites/default/files/site.sqlite ]; then
  password="$(php -r 'echo bin2hex(random_bytes(24));')"
  vendor/bin/drush site:install standard --db-url=sqlite:///opt/drupal/web/sites/default/files/site.sqlite --site-name='NIASPO Drupal' --account-name=student --account-pass="$password" --yes --quiet
  vendor/bin/drush php:eval '$n=\Drupal\node\Entity\Node::create(["type"=>"page","title"=>"Drupal в Docker — практика 3.3","body"=>["value"=>"<p>Кузнецов Максим Дмитриевич, ИКБО-15-25.</p><p>Эта страница создана как материал Drupal и хранится в базе SQLite. Это работающая CMS.</p>","format"=>"basic_html"],"status"=>1]);$n->save();\Drupal::configFactory()->getEditable("system.site")->set("page.front","/node/".$n->id())->save();' --quiet
fi
chown -R www-data:www-data web/sites/default
sed -i "s/^Listen 80$/Listen ${PORT:-10000}/" /etc/apache2/ports.conf
sed -i "s/:80>/:${PORT:-10000}>/" /etc/apache2/sites-available/000-default.conf
exec apache2-foreground
