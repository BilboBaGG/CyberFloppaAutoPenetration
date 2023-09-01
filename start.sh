WORKDIR=$PWD
supervisord -c -n /etc/supervisord/conf.d/supervisord.conf
