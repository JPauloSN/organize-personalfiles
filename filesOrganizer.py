# Importa funcionalidades para manipular arquivos do pc
import os
import shutil

# sintax para class
class filesOrganizer:

    # construct padrão para inicializar a classe
    def __init__(self, source_directory="", target_directory = ""):
        self.source_directory = source_directory
        self.target_directory = target_directory
        # note que não tem verificação em nenhuma função para o caso dos caminhos estarem vazios
        # fica de tarefa realizar a verificação depois

    # caso necessário checar apenas os números no arquivo
    # não foi feito o teste de integração com o restante do código 
    def format_filename_to_digit(self, filename):
        
        newFilename = ""

        # percorre cada caractere da string e verifica a condição
        for caractere in filename:
                if caractere.isdigit():
                    newFilename
        
        return newFilename
    
    # retorna o caminho de todos os arquivos em um diretorio e seus subdiretorios
    def scan_only_files(self):
        
        all_files = []
        
        for root, dirs, files in os.walk(self.source_directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                all_files.append(file_path)
        
        return all_files
    
    # move todos os arquivos que possuem o préfixo procurado para o alvo definido na inicialização da classe
    def move_folders_by_prefix_search(self, search):
        
        index = self.scan_only_files()
        
        for item in index:
            base = os.path.basename(item)
            
            if base.find(search) == 0:
                os.makedirs(self.target_directory, exist_ok=True)
                shutil.move(item, self.target_directory)