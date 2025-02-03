import time
from my_code import long_running_function

def test_long_running_function_performance():
    tempo_inicial = time.time()
    long_running_function()
    tempo_final = time.time()
    duration = tempo_final - tempo_inicial
    assert duration < 5, f"A função demorou {duration}, mais do que o esperado"

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_20\test_performance.py