

import sys
import time

## Função normal (não geradora)
def criar_lista_normal(max_value):
    """
    Função que cria e retorna uma lista de números.
    Esta função aloca toda a lista na memória antes de retornar.
    """
    print("--- Executando a função normal ---")
    lista = []
    for num in range(max_value):
        lista.append(num)
    return lista

## Função geradora
def criar_gerador_com_yield(max_value):
    """
    Função geradora que produz números usando `yield`.
    Os valores são gerados um por um, sob demanda, economizando memória.
    """
    print("--- Executando a função geradora ---")
    for num in range(max_value):
        yield num  # A função pausa aqui e retorna 'num'

# --- Comparando o consumo de memória ---
# Com um número grande, a diferença é significativa
print("### Comparação de Consumo de Memória ###")
tamanho = 10_000_000

# Usando a função normal
start_time = time.time()
lista_grande = criar_lista_normal(tamanho)
end_time = time.time()
print(f"Tempo da função normal: {end_time - start_time:.4f} segundos")
print(f"Tamanho da lista na memória: {sys.getsizeof(lista_grande) / 1024**2:.2f} MB")
print("-" * 30)

# Usando a função geradora
start_time = time.time()
gerador_grande = criar_gerador_com_yield(tamanho)
end_time = time.time()
print(f"Tempo da função geradora (retorno inicial): {end_time - start_time:.4f} segundos")
print(f"Tamanho do gerador na memória: {sys.getsizeof(gerador_grande) / 1024:.2f} KB")

# --- Consumo dos valores gerados ---
print("\n### Consumindo valores com `next()` e `for` ###")

# Criando um gerador pequeno para demonstração
gerador_pequeno = criar_gerador_com_yield(5)

# Consumindo com next()
print("\n--- Usando `next()` ---")
try:
    print(next(gerador_pequeno)) # Saída: 0
    print(next(gerador_pequeno)) # Saída: 1
    print(next(gerador_pequeno)) # Saída: 2
    print(next(gerador_pequeno)) # Saída: 3
    print(next(gerador_pequeno)) # Saída: 4
    print(next(gerador_pequeno)) # Gera a exceção StopIteration
except StopIteration:
    print("Fim do gerador. Exceção StopIteration capturada.")

# Criando um novo gerador para o loop `for`
gerador_for = criar_gerador_com_yield(5)

# Consumindo com for loop
print("\n--- Usando `for` loop ---")
for numero in gerador_for:
    print(numero)
