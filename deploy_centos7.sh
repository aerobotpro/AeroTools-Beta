#! /bin/bash
echo -e ""
echo API Dependencies installer by DevilsExploits
echo -e ""
#RHEL/CENTOS 7.X TESTED!
#Setup:
#EDIT SOURCE [open_aero.py] First!!
#Then drop it in /root/
#FILE LOCATIONS:
#Bot Server:
#/root/open_aero.py
#/root/admins.txt
#/root/update_log.txt
cd ~/
yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u
yum -y install python36u-pip
yum -y install screen
pip3.6 install requests
pip3.6 install discord
echo Running Aero-Tools!
screen python3.6 open_aero.py
