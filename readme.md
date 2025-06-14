# Desafio comparador-de-arquivos

## descrição do desafio

- Criar um script em python que leia dois arquivos distitos, chamados abaixo de arquivo_a.txt e arquivo_b.txt
- O script deve comparar os dois arquivos de entrada e gerar um terceiro de saída
- Para todas as linhas lidas nos dois arquivos, apenas adiciona-las ao arquivo de saída
- Para as linhas encontradas somente em "arquivo_a.txt", adicoinar um + à frente da linha
- Para as linhas encontradas somente em "arquivo_b.txt", adicionar um - à frente da linha

arquivo_a_.txt
```
Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
sed do eiusmod tempor incididunt ut  
Lorem ipsum sit amet,  
```

arquivo_b_.txt
```
Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
labore et dolore magna aliqua. Ut enim  
Lorem ipsum dolor sit amet,  
```

# saída:

arquivo_c_.txt
```
Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
+ sed do eiusmod tempor incididunt ut  
- labore et dolore magna aliqua. Ut enim  
+ Lorem ipsum dolor sit amet,  
- Lorem ipsum sit amet,  
```
