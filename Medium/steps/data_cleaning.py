import pandas as pd

def cleanig_data(data: pd.DataFrame):
    # Aplicando filtro de situação de Voo
    data = data[data["Situação Voo"] == "REALIZADO"]

    # Aplicando filtro de valores vazios, nulos, inexistêntes em Datas
    data = data[
        #Selecionando colunas de data
        data[["Partida Prevista", "Partida Real", "Chegada Prevista", "Chegada Real"]]
        # Verificando se não são nulos
        .notna()
        # Valida linha por linha se são todas true
        .all(axis=1)
        ]
    
    # Carregando base de dados de ICAOs
    icaoDataFrameObject = pd.read_csv(
        "./data/airport-codes.csv",
        sep=",",
        dtype={
            "ident": "string",
            "type": "category",
            "name": "string",
            "elevation_ft": "Int64",
            "continent": "category",
            "iso_country": "category",
            "iso_region": "string",
            "municipality": "string",
            "icao_code": "string",
            "iata_code": "string",
            "gps_code": "string",
            "local_code": "string",
            "coordinates": "string"
        })

    # Criando Series de mapeamento ICAO -> País
    icaoDataToCountry = icaoDataFrameObject.set_index("ident")["iso_country"]

    # Criando os valores da nova coluna ICAO Destino / Origem
    iso_pais_origem = data["ICAO Aeródromo Origem"].map(icaoDataToCountry)
    iso_pais_destino = data["ICAO Aeródromo Destino"].map(icaoDataToCountry)

    # Adicionado novas colunas ICAO Destino / Origem ao DataFrame
    data["ISO Aeródromo País Origem"] = iso_pais_origem
    data["ISO Aeródromo País Destino"] = iso_pais_destino

    data = data[
        (data["ISO Aeródromo País Destino"] == "BR") &
        (data["ISO Aeródromo País Origem"] == "BR")
    ]

    data["Código Tipo Linha"] = data["Código Tipo Linha"].where(
    data["Código Tipo Linha"].isin(["N", "C", "I", "G"]),
        other="D"
    )

    # Aplicando filtro de valores válidos para Código Autorização (DI)
    data = data[data["Código Autorização (DI)"].isin(["0", "2", "3", "4", "7", "9", "E"])]

    # Aplicando filtro de Voos Atrasados
    data = data[data["Partida Prevista"] < data["Partida Real"]]

    return data