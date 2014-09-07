#!/bin/sh

## define required variables
username=shack
password=shackit
baseurl=https://unifi.shack:8443

## include the API library
. /opt/printbon/unifi_sh_api

unifi_login
# unifi_authorize_guest <mac> <minutes> [up=kbps] [down=kbps] [bytes=MB]
unifi_create_voucher $1 $2
unifi_logout
