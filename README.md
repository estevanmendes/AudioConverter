# AudioConverter

Um guia de uso rápido:

```
audio=AudioConverter(path_do_arquivo) # inicia-se inserindo o caminho do arquivo 
audio.load_mp3() # o áudio é carregado
audio.change_volume(numero_de_decibeis)# Altera o volume na quantidade de decibéis dada, pode ser um inteiro positivo ou negativo.
audio.save_wav() # salva o arquivo em wav com a taxa de amostral de 16000

```

Outras funções foram adicionadas ao código. É possível obter um plot da FFT do áudio carregado por meio do método get_fft(). Também é possível obter um espectrograma utilizando o método get_spectogram().
