As listas são muito úteis e podem conter vários itens. Mas há mais! Também podemos adicionar elementos na lista a qualquer momento, usando a função `list.append`, que utiliza dois parâmetros: a lista e o elemento. Por exemplo:



```python
ム discos = ["Serú Girán", "Artaud", "Almendra", "Quebrado"]
ム len(discos)
4
ム list.append(discos, "Vida")
ム len(discos)
5
```

Como podemos ver, `list.append` adiciona um elemento à lista, o que aumenta o tamanho dela. Mas onde na lista você deve adicionar? No princípio, final ou meio? :thinking:

> Descubra você mesmo: inspecione no console quais elementos contém `livros`, adicione `"Fundação"` e volte para inspecionar `livros` novamente.
>
> Há também uma função `list.remove`, que recebe uma lista e um elemento dela como parâmetro. Pesquise no console o que ela faz. :eyes:
>
> Quando você terminar, escreva `pronto()`.
