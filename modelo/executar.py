import tkinter as tk
import os
from views.open_file import open_file

def main():
    global result_label, spectrogram_label, waveform_label
    
    root = tk.Tk()
    root.title("Reconhecimento de Ruído")
    
    # Passa os labels para a função open_file como argumentos
    open_button = tk.Button(root, text="Selecionar Arquivo", command=lambda: open_file(result_label, spectrogram_label, waveform_label))
    open_button.pack(pady=20)
    
    result_label = tk.Label(root, text="Nenhuma previsão")
    result_label.pack(pady=10)
    
    spectrogram_label = tk.Label(root)
    spectrogram_label.pack(pady=20)
    
    waveform_label = tk.Label(root)
    waveform_label.pack(pady=20)
    print("Diretório de trabalho atual:", os.getcwd())
    root.mainloop()

if __name__ == '__main__':
    main()


# import tkinter as tk
# import os
# from views.open_file import open_file

# # Função principal para criar e exibir a interface Tkinter
# def main():
#     global result_label, spectrogram_label, waveform_label
    
#     root = tk.Tk()
#     root.title("Reconhecimento de Ruído")
    
#     open_button = tk.Button(root, text="Selecionar Arquivo", command=open_file)
#     open_button.pack(pady=20)
    
#     result_label = tk.Label(root, text="Nenhuma previsão")
#     result_label.pack(pady=10)
    
#     spectrogram_label = tk.Label(root)
#     spectrogram_label.pack(pady=20)
    
#     waveform_label = tk.Label(root)
#     waveform_label.pack(pady=20)
#     print("Diretório de trabalho atual:", os.getcwd())
#     root.mainloop()

# if __name__ == '__main__':
#     main()
