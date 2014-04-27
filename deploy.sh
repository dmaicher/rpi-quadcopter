sshpass -p 'root' scp src/* root@192.168.0.106:/home/rpi-qaudcopter
sshpass -p 'root' ssh root@192.168.0.106 "cd /home/rpi-qaudcopter && python2.7 app.py"

