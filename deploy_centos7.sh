echo -e ""
echo [+] - Welcome To Aero-Tools!
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
echo -e ""
echo [+] - Updating RHEL7/Centos7...
echo -e ""
yum -y update
echo -e ""
echo [+] - Installing Python3.6 For RHEL7/Centos7...
echo -e ""
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u
yum -y install python36u-pip
echo -e ""
echo [+] - Installing Python3.6 Dependencies For Aero-Tools...
echo -e ""
yum -y install screen
pip3.6 install requests
pip3.6 install discord
echo -e ""
echo [+] - Setup Complete! Running Aero-Tools...
echo -e ""
screen python3.6 open_aero.py
