mysql -uroot -e "create database if not exists simpledb"
mysql -uroot -e "create user 'stalder'@'localhost' identified by 'Stalder525'"
mysql -uroot -e "grant all on simpledb.* to 'stalder'@'localhost'"
