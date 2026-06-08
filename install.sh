RSA="\033[31m"
YSA="\033[1;93m"
CEA="\033[0m"
WHS="\033[0;97m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[-]"$WHS" [Errno 1] Failed to copy files: Operation not permitted"$CEA""
    exit
exit
fi

if [[ -d ~/GeoSpy ]]
then
cd ~/BINSpy
{
cp bin/binspy /usr/local/bin
chmod 777 /usr/local/bin/binspy
cp bin/binspy /bin
chmod 777 /bin/binspy
python -m pip install -r requirements.txt
} &> /dev/null
else
cd ~
{
git clone https://github.com/ALIF101XL/BINSpy.git
cd  ~/BINSpy
cp bin/binspy /usr/local/bin
chmod 777 /usr/local/bin/binspy
cp bin/binspy /bin
chmod 777 /bin/binspy
python -m pip install -r requirements.txt
} &> /dev/null
fi
