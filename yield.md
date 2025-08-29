# Funções Geradoras e a Palavra-Chave `yield`

As funções geradoras são uma forma elegante e eficiente de criar iteradores.  
A principal diferença entre uma função normal e uma função geradora reside na palavra-chave `yield`.

---

## Função Normal vs. Função Geradora

- **Função Normal**:  
  Quando uma função normal é chamada, ela executa todo o seu código, armazena o resultado e o retorna de uma só vez usando a palavra-chave `return`.  
  Depois de retornar, a função é encerrada e seu estado (variáveis locais, etc.) é perdido.

- **Função Geradora**:  
  Uma função geradora, por outro lado, usa a palavra-chave `yield` para produzir uma sequência de valores.  
  Em vez de retornar um valor e terminar a execução, `yield` **pausa** a função, retorna o valor e mantém seu estado.  
  Quando a função é chamada novamente (para obter o próximo valor), ela continua a execução exatamente de onde parou.  

Essa **avaliação preguiçosa** (*lazy evaluation*) é o que torna os geradores tão poderosos.

---

## Para que servem os geradores?

Geradores são especialmente úteis para:

- **Economizar memória**:  
  Em vez de gerar e armazenar uma lista inteira na memória de uma vez, um gerador produz os valores *sob demanda*.  
  Isso é crucial ao lidar com grandes conjuntos de dados (como um arquivo de log enorme ou dados de um banco de dados) ou sequências infinitas.

- **Sequências infinitas**:  
  Como os geradores não precisam armazenar todos os elementos na memória, eles podem representar sequências de dados infinitas.  
  Um exemplo clássico é a sequência de **Fibonacci**.

- **Pipelining de dados**:  
  Geradores podem ser encadeados para criar *pipelines* de processamento de dados, onde cada gerador filtra ou transforma o valor do gerador anterior.

---

## Consumo de Valores com `next()` e `for`

Uma função geradora, ao ser chamada, não executa seu código imediatamente.  
Em vez disso, ela retorna um **objeto gerador**.  

Para consumir os valores gerados, você pode usar:

- **`next()`**:  
  A função embutida `next()` chama o gerador, fazendo-o executar até a próxima instrução `yield`.  
  Cada vez que você chama `next()`, ele retorna o próximo valor.  
  Quando não há mais valores para serem gerados, uma exceção `StopIteration` é lançada.

- **`for` loop**:  
  A forma mais comum e elegante de consumir um gerador é usando um `for` loop.  
  O loop `for` lida com toda a lógica de chamar `next()` e capturar a exceção `StopIteration` automaticamente, tornando o código mais limpo e legível.
