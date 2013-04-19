apt-get update
apt-get install software-properties-common
apt-get install python-software-properties python g++ make
add-apt-repository ppa:chris-lea/node.js
apt-get update
apt-get install mysql-server mysql-client python-virtualenv libmysqlclient-dev nodejs php5-fpm php5-xmlrpc php5-xcache php5-mysql php5-mcrypt php5-json php5-imagick php5-gd php5-curl git nginx vsftpd libjpeg-dev libpng-dev yui-compressor jpegoptim optipng slimit python-dev libpng12-dev zlib1g-dev  memcached 

wget http://npmjs.org/install.sh
sh install.sh 
npm install -g less

sudo pip install virtualenvwrapper

mkdir /www

easy_install -U distribute


# AS USER
mkvirtualenv pomysl
mkdir pomysl
git init
git remote add origin git@mgjt.tk:pomyslnadzis.git

