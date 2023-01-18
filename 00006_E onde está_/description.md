Outra coisa que queremos fazer com as listas é saber em que posição um elemento está. Para fazer isso, usamos a função `list.index` da seguinte forma:

```python
ム list.index(["traçar", "de", "novo",  "a", "estrada"], "novo")
2
ム dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
ム list.index(dias_uteis, "segunda-feira")
0
```

Como você pode ver, o curioso dessa função é que ela parece sempre retornar um a menos do esperado. Por exemplo, a palavra `"novo"` aparece em terceiro lugar, não em segundo; e `"segunda-feira"` é o primeiro dia útil, não zero. Quem criou o Python estava errado? :confused:

Não! :sweat_smile: O ponto é que em Python, como em muitas linguagens, as posições das listas começam pelo 0: o primeiro elemento está na posição 0, o segundo na 1, o terceiro na 2 e assim por diante.


> E o que acontece se você passar um item que não existe por meio de um parâmetro à `list.index`? Descubra!
>
> Teste o seguinte:
>
> ```python
> ムlist.index(dias_úteis, "osvaldo")
> ```

