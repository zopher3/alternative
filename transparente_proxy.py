import subprocess
def iptables_proxy():
    pergunta = input("DIGITE SEU SERVIDOR PROXY: ")
    pergunta_um = input("DIGITE A PORTA DO SEU SERVIDOR: ")
    pergunta_dois = input("DIGITE A SUA INTERFACE DE REDE: ")

    subprocess.run(f"iptables -t nat -A OUTPUT -p tcp -o {pergunta_dois} -j DNAT --to {pergunta}:{pergunta_um}", shell=True)


