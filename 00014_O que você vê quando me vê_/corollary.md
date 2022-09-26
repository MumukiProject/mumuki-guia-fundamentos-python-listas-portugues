Por que tivemos que colocar as expressões nessa ordem específica?

* Se perguntássemos primeiro a posição da série no ranking e a série não estivesse na lista, nosso código explodiria.  :boom:
* Por outro lado, como fizemos, se a série não estiver no ranking (`not serie in ranking`) não é necessário perguntar a posição, pois já sabemos que toda essa expressão é verdadeira.

Lembre-se que para o operador `or` retornar `True` basta que uma das condições seja verdadeira. Se a primeira condição for verdadeira, para que perguntar sobre a segunda? :sweat_smile:                             