from tkinter import filedialog, messagebox
from .predict_audio import predict_audio
from .create_spectrogram_image import create_spectrogram_image
from .create_waveform_image import create_waveform_image

def open_file(result_label, spectrogram_label, waveform_label):
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if file_path:
            print(f'Arquivo selecionado: {file_path}')
            result = predict_audio(file_path)
            if result:
                result_label.config(text=f'Classificação: {result}')
                
                # Criar e exibir a imagem do espectrograma
                spectrogram_img = create_spectrogram_image(file_path)
                if spectrogram_img:
                    spectrogram_label.config(image=spectrogram_img)
                    spectrogram_label.image = spectrogram_img  # Mantenha uma referência da imagem
                
                # Criar e exibir a imagem da forma de onda
                waveform_img = create_waveform_image(file_path)
                if waveform_img:
                    waveform_label.config(image=waveform_img)
                    waveform_label.image = waveform_img  # Mantenha uma referência da imagem
            else:
                result_label.config(text='Erro ao fazer a previsão.')
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        messagebox.showerror("Erro", f"Erro ao abrir o arquivo: {e}")


# #modelo/views/open_file
# from tkinter import filedialog, messagebox
# from .predict_audio import predict_audio
# from .create_spectrogram_image import create_spectrogram_image
# from .create_waveform_image import create_waveform_image

# # Função chamada quando o botão de abrir arquivo é clicado
# def open_file():
#     try:
#         file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
#         if file_path:
#             print(f'Arquivo selecionado: {file_path}')
#             result = predict_audio(file_path)
#             if result:
#                 result_label.config(text=f'Classificação: {result}')
                
#                 # Criar e exibir a imagem do espectrograma
#                 spectrogram_img = create_spectrogram_image(file_path)
#                 if spectrogram_img:
#                     spectrogram_label.config(image=spectrogram_img)
#                     spectrogram_label.image = spectrogram_img  # Mantenha uma referência da imagem
                
#                 # Criar e exibir a imagem da forma de onda
#                 waveform_img = create_waveform_image(file_path)
#                 if waveform_img:
#                     waveform_label.config(image=waveform_img)
#                     waveform_label.image = waveform_img  # Mantenha uma referência da imagem
#             else:
#                 result_label.config(text='Erro ao fazer a previsão.')
#     except Exception as e:
#         print(f"Erro ao abrir o arquivo: {e}")
#         messagebox.showerror("Erro", f"Erro ao abrir o arquivo: {e}")