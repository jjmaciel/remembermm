from remembermm.models import PersonalData

###################################### FUNÇÃO PARA ADICIONAR

# função para adicionar um novo registro no banco de dados
def addPersonalData(personal_data):
    return PersonalData.objects.create(
        name = personal_data.name,
        email = personal_data.email,
        phone = personal_data.phone
    )


###################################### FUNÇÃO PARA EDITAR

# função para editar um registro existente no banco de dados
# o Django cria uma instância dos dados originais, os dados originais são substituidos
# e então é feito o update 
def editPersonalData(personal_data_origin, personal_data_edit):
    personal_data_origin.name = personal_data_edit.name
    personal_data_origin.email = personal_data_edit.email
    personal_data_origin.phone = personal_data_edit.phone
    personal_data_origin.save(force_update=True)


###################################### FUNÇÕES DE GET

# busca todos os registros cadastrados no banco de dados
def getPersonalDataAll():
    return PersonalData.objects.all()


# busca um registro específico através do ID
def getPersonalDataById(id):
    return PersonalData.objects.get(id=id)

# buca registros pelo nome. É verificado se o texto digitado contem
# em alguma linha da coluna nome da tabela PersonalData
def getPersonalDataByName(name):
    return PersonalData.objects.filter(name__icontains=name)


###################################### FUNÇÃO DE DELETE

# remove um registro do banco de dados . A função recebe uma instância e então deleta
def removePersonalData(personal_data):
    personal_data.delete()