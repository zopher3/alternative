import stem.process

def circuite_max():
torrc_path = "/etc/tor/torrc"  # Altere o caminho conforme necessário

new_max_circuit_dirtiness = "MaxCircuitDirtiness 10 seconds"

try:
    tor_process = stem.process.launch_tor_with_config(
        torrc_path=torrc_path,
    )

    print(f"A configuração MaxCircuitDirtiness foi definida para {new_max_circuit_dirtiness}.")
except Exception as e:
    print(f"Erro: {e}")
