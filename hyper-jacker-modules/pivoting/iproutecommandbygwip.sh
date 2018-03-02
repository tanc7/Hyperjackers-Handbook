subnet=192.168.122.0/24
gwip=192.168.122.1
ip route add $subnet via $gwip
