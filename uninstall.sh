RSA="\033[31m"
YSA="\033[1;93m"
CEA="\033[0m"
WHS="\033[0;97m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[-]"$WHS" [Errno 1] Failed to remove files: Operation not permitted"$CEA""
    exit
exit
fi

{
rm /bin/binspy
rm /usr/local/bin/binspy
rm -r ~/BINSpy
} &> /dev/null
