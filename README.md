# Tema1LFA
##### Pentru un automat finit determinist şi un cuvānt dat, să se determine dacă acel cuvânt este acceptat de către automat (dacă aparține sau nu limbajului recunoscut de automat). Dacă acesta este acceptat, se va afişa drumul folosit pentru acceptare, alternativ se va afişa un mesaj corespunzator.

## Teste
#### 1. bbabbabba 
###### Acceptat! Drumul este: 
###### 0b :  0b :  0a :  1b :  2b :  3a :  4b :  4b :  4a :  4


###### AFD: 
- {'b': 0, 'a': 1}
- {'a': 1, 'b': 2}
- {'a': 1, 'b': 3}
- {'b': 1, 'a': 4}
- {'a': 4, 'b': 4}


#### 2. abbabba
###### Acceptat! Drumul este:
0a :  1b :  2b :  3a :  4b :  4b :  4a :  4


###### AFD: 
- {'b': 0, 'a': 1}
- {'a': 1, 'b': 2}
- {'a': 1, 'b': 3}
- {'b': 1, 'a': 4}
- {'a': 4, 'b': 4}
- 
#### 3. ababababababaaaaaba
###### Neacceptat!

###### AFD: 
- {'b': 0, 'a': 1}
- {'a': 1, 'b': 2}
- {'a': 1, 'b': 3}
- {'b': 1, 'a': 4}
- {'a': 4, 'b': 4}
#### 4. bbbbbbaaaaabbbabbaaaaaaab
###### Acceptat! Drumul este:
0b :  0b :  0b :  0b :  0b :  0b :  0a :  1a :  1a :  1a :  1a :  1b :  2b :  3b :  1a :  1b :  2b :  3a :  4a :  4a :  4a :  4a :  4a :  4a :  4b :  4

###### AFD: 
- {'b': 0, 'a': 1}
= {'a': 1, 'b': 2}
- {'a': 1, 'b': 3}
- {'b': 1, 'a': 4}
- {'a': 4, 'b': 4}
