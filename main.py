from huepy import *
from resolve_dns import dens_resolve
from preload_proxy import proxy_chains
from iptables_rules import rules_iptables
from transparente_proxy import iptables_proxy
from max_circuite import circuite_max

print(""" 

   ▄▄▄· ▄▄▌  ▄▄▄▄▄▄▄▄ .▄▄▄   ▐ ▄  ▄▄▄· ▄▄▄▄▄▪   ▌ ▐·▄▄▄ .
▐█ ▀█ ██•  •██  ▀▄.▀·▀▄ █·•█▌▐█▐█ ▀█ •██  ██ ▪█·█▌▀▄.▀·
▄█▀▀█ ██▪   ▐█.▪▐▀▀▪▄▐▀▀▄ ▐█▐▐▌▄█▀▀█  ▐█.▪▐█·▐█▐█•▐▀▀▪▄
▐█ ▪▐▌▐█▌▐▌ ▐█▌·▐█▄▄▌▐█•█▌██▐█▌▐█ ▪▐▌ ▐█▌·▐█▌ ███ ▐█▄▄▌
 ▀  ▀ .▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀▀▀ █▪ ▀  ▀  ▀▀▀ ▀▀▀. ▀   ▀▀▀ 


  """)

print(good("Este é um script para anonimizar requisições via terminal"))

print(""" O que ele faz:
0 - Configura proxy como preload
1 - Utiliza um proxy transparente com iptables para rotear todo o tráfego de saída por meio de um proxy
2 - Usa tor para resolver consultas de DNS
3 - Configura max circuito, para controlar o tempo que cada circuito demora leva
4 - Regras Iptables para bloquear saida de pacotes indesejados que acabam expondo seu IP em cada requisição.



""")

question = input(("ESTE SCRIPT PODE AFETAR O DESEMPENHO DO SEU SISTEMA, DESEJA CONTINUAR?""[YES/NO]"))
if question == "YES":
    iptables_proxy()
    proxy_chains()
    dens_resolve()
    rules_iptables()
    circuite_max()

else:
    print("OPERAÇÃO CANCELADA")