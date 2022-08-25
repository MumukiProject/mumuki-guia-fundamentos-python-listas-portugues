Assim como existe uma função para descobrir em que posição um elemento está, também pode acontecer que queiramos saber o contrário: qual elemento está em determinada posição. :open_mouth:

Para descobrir podemos usar o **operador de indexação**, escrevendo após a coleção e entre colchetes `[]` a posição que queremos descobrir:

```python
ム meses_do_ano[0] # lembre de que o primeiro item está na posição 0
"Janeiro"
ム ["esse", "cachorro", "tem", "o", "rabo", "peludo"][1]
"cachorro"
```

Atenção! O número que você passa, formalmente chamado de **índice**, deve ser menor que o tamanho da lista, ou coisas ruins podem acontecer. :astonished:

> Teste no console: o que acontece se você solicita o item 0 a uma lista vazia? Ou se você pede o item 48 aos  `meses_do_ano`?
>
> Quando tiver terminado as provas, escreva `pronto()`.
