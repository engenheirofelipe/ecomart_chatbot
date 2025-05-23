# Refatorando o modelo

1. Adicionando p modelo gpt-4-1106-preview no arquivo assistente_ecomart
2.  Criar uma lista de ids 

    def criar_lista_ids()
        lista_ids_arquivos = []

        file_ids = cliente.files.create(
            file = open("dados/dados_ecomart.txt", "rb")
            purpose="assistant"
        )
        lista_ids_arquivos.append(file_ids.id)

        file_politicas = cliente.files.create(
            file=open("dados/políticas_ecomart", "rb")
            purpose="assistant"
        )
        lista_ids_arquivos.append(file_politicas.id)

        produtos_file = cliente.files.create(
            file=open("dados/produtos_ecomart.txt","rb")
            purpose="assistant"
        )
        lista_ids_arquivos.append(produtos_file.id)

3.  Garantir que esses arquivos sejam adicionados aos assistentes

        def pegar_json():

            filename = "assistentes.json"

            if not in os.path.exists(filename)
                thread_id = criar_thread()
                file_id_list = criar_lista_ids()
                assistant_id = criar_assistente(file_id_list)

                data = {
                    "assistant_id":assistant_id.id,
                    "thread_id":thread_id.id,
                    "file_ids":file_id_list
                }