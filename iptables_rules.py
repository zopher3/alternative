import subprocess

def rules_iptables():

    subprocess.run("iptables -t nat -A PREROUTING -p tcp -m multiport --dport 4:52,54:79,81:442,444:5352,5354:8079,8081:9049,9200:65533 -j REDIRECT --to- ports 9050")
    subprocess.run("iptables -t raw -A PREROUTING -p udp -m udp -j DROP" , shell=True)
    subprocess.run("iptables -t raw -A PREROUTING -p icmp -j DROP" , shell=True)
    subprocess.run("iptables -P INPUT DROP" , shell=True)
    subprocess.run("iptables -A INPUT -m state --state ESTABLISHED -p udp -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -m state --state ESTABLISHED -p icmp -j DROP" , shell=True)
    subprocess.run("iptables -t filter -A INPUT -p udp --destination 0.0.0.0/0 -j DROP" , shell=True)
    subprocess.run("iptables -t filter -A INPUT -p icmp --destination 0.0.0.0/0 -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -m state --state INVALID -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -m conntrack --ctstate INVALID -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp -m tcp --tcp-flags FIN, SYN, RST, PSH, ACK,URG FIN,SYN,RST,ACK -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN FIN,SYN -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp -m tcp --tcp-flags SYN,RST SYN,RST -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -f -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp -m tcp --tcp-flags FIN, SYN, RST, PSH, ACK, URG FIN, SYN,RST,PSH,ACK,URG -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp -m tcp --tcp-flags FIN, SYN, RST, PSH, ACK, URG NONE -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp -j ACCEPT" , shell=True)
    subprocess.run("iptables -A INPUT -j DROP" , shell=True)
    subprocess.run("iptables -A INPUT -p tcp --destination 0.0.0.0/0 -m multiport --dport 80,443,8080,9050,9051,9053 -j ACCEPT", shell=True)
    subprocess.run("iptables -A OUTPUT -m state --state ESTABLISHED -p udp -j DROP",  shell=True)
    subprocess.run("iptables -A OUTPUT -m state --state ESTABLISHED -p icmp -j DROP", shell=True)
    subprocess.run("iptables -t filter -A OUTPUT -p udp --destination 0.0.0.0/0 -j DROP", shell=True)
    subprocess.run("iptables -t filter -A OUTPUT -p icmp --destination 0.0.0.0/0 -j DROP" , shell=True)
    subprocess.run("iptables -A OUTPUT -m state --state INVALID -j DROP" , shell=True)
    subprocess.run("iptables -A OUTPUT -m conntrack --ctstate INVALID -j DROP" , shell=True)
    subprocess.run("iptables -t nat -A OUTPUT -p tcp --dport 53 -j REDIRECT --to-ports 9053" , shell=True)
    subprocess.run("iptables -t nat -A OUTPUT -p tcp --dport 5353 -j REDIRECT --to- ports 9053" , shell=True)
    subprocess.run("iptables -t filter -A OUTPUT -p tcp --destination 0.0.0.0/0 -m multiport --dport 80,443,8080 -j ACCEPT" , shell=True)
    subprocess.run("iptables -t nat -A OUTPUT -p tcp -m multiport --dport 4:52,54:79,81:442,444:5352,5354:8079,8081:9049,9200:65533 -j REDIRECT --to-ports 9050")
    subprocess.run("iptables -t nat -A OUTPUT -p tcp -m multiport --dport 42,444:5352,5354:8079,8081:9049,9200:65533 -j REDIRECT --tofilter -A OUTPUT -p tcp -m multiport --dport DROP" , shell=True)
    subprocess.run("iptables -A FORWARD -m state --state ESTABLISHED -p tcp -o eth0 -j ACCEPT", shell=True)
    subprocess.run("iptables -A FORWARD -m state --state ESTABLISHED -p tcp -o lo -j ACCEPT" , shell=True)
    subprocess.run("iptables -A FORWARD -m state --state ESTABLISHED -p udp -j DROP" , shell=True)
    subprocess.run(" iptables -A FORWARD -j DROP" , shell=True)
    subprocess.run("iptables -A FORWARD -m state --state ESTABLISHED -p icmp -jDROP", shell=True)
    subprocess.run("iptables -t filter -A FORWARD -p udp --destination 0.0.0.0/0 -j DROP" , shell=True)
    subprocess.run("iptables -t filter -A FORWARD -p icmp --destination 0.0.0.0/0 -j DROP" , shell=True)

    subprocess.run("iptables -A FORWARD -m state --state INVALID -j DROP" , shell=True)

    subprocess.run("iptables -A FORWARD -m conntrack --ctstate INVALID -j DROP", shell=True)

    subprocess.run("iptables -t mangle -A POSTROUTING -p tcp destination 0.0.0.0/0 -m multiport --dport 80,443,8080 -j ACCEPT" , shell=True)
    subprocess.run("iptables -t mangle -A POSTROUTING -p tcp --destination 0.0.0.0/0 -m multiport --dport 4:52,54:79,81:442,444:5352,5354:8079, 8081: 9049, 9200: 65533—) DROP" , shell=True)
    subprocess.run("iptables -t mangle -A POSTROUTING -m state --state ESTABLISHED -p udp -j DROP", shell=True)
    subprocess.run("iptables -t mangle -A POSTROUTING -m state --state ESTABLISHED -p temp -j DROP", shell=True)
    subprocess.run("iptables -t mangle -A POSTROUTING -p udp -m udp --destination 0.0.0.0/0 -j DROP", shell=True)
    subprocess.run("iptables -t mangle -A POSTROUTING -p icmp --destination 0.0.0.0/0 —3 DROP" , shell=True)
    subprocess.run("iptables -t raw -A PREROUTING --destination 0.0.0.0/0 -j DROP", shell=True)
    subprocess.run("iptables -P INPUT DROP", shell=True)
    subprocess.run("iptables -P OUTPUT DROP" , shell=True)
    subprocess.run("ipótables -P FORWARD DROP", shell=True)
    subprocess.run("iptables -A INPUT -j REJECT --reject-with adm-prohibited", shell=True)
    subprocess.run("iptables -A INPUT --destination 0.0.0.0/0 -j DROP", shell=True)
    subprocess.run("iptables -A INPUT -m state --state RELATED -p tcp -j DROP", shell=True)
    subprocess.run("iptables -A INPUT -m state --state RELATED -p udp -j DROP", shell=True)
    subprocess.run("iptables -A INPUT -m state --state RELATED -p icmp -) DROP", shell=True)
    subprocess.run("iptables -A OUTPUT -j REJECT --reject-with adm-prohibited" , shell=True)
    subprocess.run("iptables -A OUTPUT --destination 0.0.0.0/0 -j DROP" , shell=True)
    subprocess.run("iptables -A OUTPUT -m state --state RELATED -p tcp -j DROP", shell=True)
    subprocess.run("iptables -A OUTPUT -m state --state RELATED -p udp -j DROP" , shell=True)
    subprocess.run("iptables -A OUTPUT -m state --state RELATED -p icmp -j DROP" , shell=True)
    subprocess.run("iptables -A FORWARD -j REJECT --reject-with adm-prohibited", shell=True)
    subprocess.run("iptables -A FORWARD -p icmp -j REJECT --reject-with icmp6-adm- pronibited" , shell=True)
    subprocess.run("iptables -A FORWARD --destination 0.0.0.0/0 -j DROP" , shell=True)
    subprocess.run("iptables -A FORWARD -m state --state RELATED -p tcp -j DROP", shell=True)
    subprocess.run("iptables -A FORWARD -m state --state RELATED -p udp -j DROP", shell=True)
    subprocess.run("iptables -A FORWARD -m state --state RELATED -p icmp -j DROP", shell=True)
    subprocess.run("macchanger -r eth0" , shell=True);
    subprocess.run("iptables -t raw -A PREROUTING -m state --state ESTABLISHED -p udp —3 DROP" , shell=True)
    subprocess.run("iptables -t raw -A PREROUTING -m state --state ESTABLISHED -p icmp—3 DROP" , shell=True)
    subprocess.run("iptables -t nat -A PREROUTING -p tcp --dport 53 -j REDIRECT --to- ports 9053" , shell=True)
    subprocess.run("iptables -t nat -A PREROUTING -p tcp --dport 5353 -j REDIRECT - to - ports 9053" , shell=True)
    subprocess.run("iptables -t nat -A PREROUTING -p tcp --destination 0.0.0.0/0 -m multiport - -dport 80, 443, 8080 - j ACCEPT" , shell=True)