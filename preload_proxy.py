import os
import platform

def proxy_chains():
    # Detecta o sistema operacional e o shell padrão
    system = platform.system()
    shell = os.environ.get("SHELL", "")
    rc_file = os.path.expanduser("~/.bashrc" if "bash" in shell else "~/.zshrc")

    # Verifica se o arquivo de inicialização existe
    if not os.path.isfile(rc_file):
        print(
            f"O arquivo de inicialização {rc_file} não foi encontrado. Certifique-se de ter um shell válido configurado.")
        exit(1)

    # Adiciona "torsocks --quiet on" ao arquivo de inicialização
    with open(rc_file, "a") as file:
        if not any(line.strip() == "torsocks --quiet on" for line in file):
            file.write("torsocks --quiet on\n")
            print(f"'torsocks --quiet on' foi adicionado ao arquivo de inicialização ({rc_file}).")
        else:
            print("'torsocks --quiet on' já está configurado no arquivo de inicialização.")
