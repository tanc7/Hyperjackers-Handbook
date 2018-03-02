subnet=192.168.122.0/24
virface=virbr0
ip route add $subnet dev $virface
