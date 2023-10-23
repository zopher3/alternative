import subprocess
import os
def dens_resolve():

    # Verifica se o usuário possui privilégios de administrador
    if os.geteuid() != 0:
        print("Este script deve ser executado com privilégios de administrador (sudo).")
        exit(1)

    # Configura o systemd-resolved para usar o Tor como provedor de DNS
    resolved_conf = "/etc/systemd/resolved.conf"
    dns_config = "DNS=127.0.0.1\nDomains=~."

    with open(resolved_conf, "w") as conf_file:
        conf_file.write(dns_config)

    # Reinicia o serviço systemd-resolved
    subprocess.call(["systemctl", "restart", "systemd-resolved"])

    # Inicia o serviço Tor (se ainda não estiver em execução)
    subprocess.call(["systemctl", "start", "tor"])

    print("Configuração completa. Consultas de DNS redirecionadas para o Tor.")
