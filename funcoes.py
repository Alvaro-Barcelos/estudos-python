def exibir_conteudo(conteudo):
    print(f"Este é o {conteudo.lower().strip()}")

exibir_conteudo("     Varivavel de Ambiente!")


def retorna_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor(numero=10))


def salvar_requisicao(id, descricao, grupo_designado,data_final):
    print(f"""
            ------------------------------
            - {id} - {grupo_designado}   -
            ------------------------------
            - {descricao}                -
            -              {data_final}  -
            ------------------------------
          """)

salvar_requisicao("GD32456", "Favor enviar material sdt", "MKT", "22-03-2025")