WORKDIR=$PWD
supervisord -n -c $WORKDIR/etc/supervisord.conf
