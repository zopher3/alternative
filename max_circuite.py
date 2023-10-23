import stem.process

# Caminho para o arquivo de configuração do Tor
torrc_path = "/etc/tor/torrc"  # Altere o caminho conforme necessário

# Defina a nova configuração MaxCircuitDirtiness (10 segundos)
new_max_circuit_dirtiness = "MaxCircuitDirtiness 10 seconds"

try:
    # Inicialize o processo Tor com o arquivo de configuração
    tor_process = stem.process.launch_tor_with_config(
        torrc_path=torrc_path,
    )

    print(f"A configuração MaxCircuitDirtiness foi definida para {new_max_circuit_dirtiness}.")
except Exception as e:
    print(f"Erro: {e}")
