#!/bin/bash
dnf install -y httpd git curl tar gzip grep
cd && git clone https://github.com/ProfessionalLinuxUsersGroup/lac && cd $HOME/lac
VERSION=$(curl -sL https://github.com/rust-lang/mdBook/releases/latest | grep -Po -m 1 'v(?:\d\.){2}\d+')
curl -sLO "https://github.com/rust-lang/mdBook/releases/download/${VERSION}/mdbook-${VERSION}-x86_64-unknown-linux-gnu.tar.gz"
tar xfz mdbook-${VERSION}-x86_64-unknown-linux-gnu.tar.gz
rm -f mdbook-${VERSION}-x86_64-unknown-linux-gnu.tar.gz
systemctl enable --now httpd
$PWD/mdbook build -d /var/www/html
systemctl restart httpd
unset VERSION
