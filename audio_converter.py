
from librosa import load
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

class AudioConverter:

    #construtor da funcao, os parametros são o caminho do arquivo e a taxa de amostragem para qual haverá a conversão
    def __init__(self,file_path,new_sample_rate=16000):
        self._file_path=file_path
        self._file_name=self.__name_from_path(file_path)
        self._new_sample_rate=new_sample_rate

    # funcao que carrega o arquivo em mp3
    def load_mp3(self):
        data,sample_rate=load(self._file_path)        
        self._data=data
        self._sample_rate=sample_rate
        self.__set_audio_segment(data,self._new_sample_rate)
        print(f'Signal Shape {data.shape}')
        print(f'Sample Rate {sample_rate}')
        print('MP3 File Was Loaded')

    
    #retorna o atributo sample rate original
    @property
    def sample_rate(self):
        return self._sample_rate

    #retorna os dados do audio
    @property
    def data(self):
        return self._data
    #retorna o nome do arquivo que será salvo e foi carregado
    @property
    def file_name(self):
        return self._file_name

    #retorna a taxa de amostragem do arquivo original
    @property
    def sample_rate(self):
        return self._sample_rate

    #define um novo nome para o arquivo
    @file_name.setter
    def file_name(self,file_name):
        self._file_name=file_name
    
    #funcao que muda o volume em decibeis
    def change_volume(self,decibel):
        audio=self._audio.apply_gain(decibel) 
        self._audio=audio
        print(f'The New dBFS Is {audio.dBFS}')

    #função que salva o arquivo em wav
    def save_wav(self):
        audio=self._audio
        name=self._file_name+'.wav'
        audio.export(name,format='wav')
        print(f'The File Named {name} Was saved')


    #Função que gera o gráfico da transformada de fourier dos dados
    def get_fft(self):
        fft=np.fft.fft(self._data)
        n=len(self._data)
        modulte_fft=((fft*np.conj(fft)).real)**0.5
        fft_freq=np.fft.fftfreq(n,1/self._sample_rate)

        fft_freq=fft_freq/10**3
        dB_fft=10*np.log10(modulte_fft)

        fig,ax=plt.subplots(1,1,figsize=(12,8))
        ax.plot(fft_freq[:n//2],dB_fft[:n//2],label="FFT's Module ",color='dodgerblue')
        ax.set_xlabel('KHz')
        ax.set_ylabel('dB',fontsize=15)
        fig.suptitle('Original Audio\nFast Fourier Transform',fontsize=20)
        ax.legend(frameon=False)
        ax.grid()
        plt.show()   
    
    #Função que gera um espectograma 
    def get_spectogram(self):
        fig,ax=plt.subplots(1,1,figsize=(12,8))
        ax.specgram(a1._data/10**3,Fs=a1._sample_rate)
        ax.set_title('Original Audio\nSpectogram',fontsize=20)
        ax.set_xlabel('Time [s]',fontsize=15)
        ax.set_ylabel('Frequency [kHz]',fontsize=15)
        plt.show()

    # funcao que extrai o nome orignal do arquivo. Não foi obtido exatamente o nome pois a ideia é que o novo arquivo seja salvo no mesmo lugar
    def __name_from_path(self,file_path):
        file_name=file_path.split('.mp3')[0]
        return file_name

    #função que converte os arquivos carregados utilizando librosa em um AudioSegment do pydub
    def __librosa_to_pydub(self,y,sr):
        y = np.array(y * (1<<15), dtype=np.int16)
        audio_segment = AudioSegment(
            y.tobytes(), 
            frame_rate=sr,
            sample_width=y.dtype.itemsize, 
            channels=1
            )
        return audio_segment
    
    #Função que cria um AudioSegment do pydub
    def __set_audio_segment(self,data,sample_rate):
        self._audio=self.__librosa_to_pydub(data,sample_rate)
        
