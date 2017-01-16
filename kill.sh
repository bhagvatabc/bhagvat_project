Process1=$(pgrep -f -x "python Local_tcpserver.py")
if [ ! -z "$Process1" -a "$Process1" != "" ]; then
   echo "Server is running"
   echo $Process1
   sudo kill -9 $Process1
else
   echo "process not running"
fi
