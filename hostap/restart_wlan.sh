service hostapd stop
sudo nmcli nm wifi off
sudo rfkill unblock wlan
sleep 1
sudo ifconfig wlan0 192.168.0.1 up
service dnsmasq restart
iptables -t nat -A POSTROUTING -o  eth0  -j MASQUERADE
