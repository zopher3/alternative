import stem.process
from stem import Signal
def circuite_max():
    # Caminho para o arquivo de configuração do Tor
    torrc_path = "/etc/tor/torrc"  # Altere o caminho conforme necessário

    # Defina a nova configuração MaxCircuitDirtiness (10 minutos)
    new_max_circuit_dirtiness = "MaxCircuitDirtiness 10 minutes"

    try:
        # Inicialize o processo Tor com o arquivo de configuração
        tor_process = stem.process.launch_tor_with_config(
            torrc_path=torrc_path,
        )

        # Crie um controlador para interagir com o Tor
        with tor_process.controller as controller:
            # Defina a nova configuração MaxCircuitDirtiness
            controller.set_conf("MaxCircuitDirtiness", new_max_circuit_dirtiness)

            # Envie um sinal para recarregar a configuração
            controller.signal(Signal.HUP)

            print("A configuração MaxCircuitDirtiness foi definida para 10 minutos.")
    except Exception as e:
        print(f"Erro: {e}")

