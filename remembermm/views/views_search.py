from django.shortcuts import render

from remembermm.forms.form_personal_data import FormPersonalData
from remembermm.entity.entity_personal_data import EntityPersonalData
from remembermm.services.services_personal_data import getPersonalDataByName

"""
A função search carrega o formulário (FormPersonalData) mas exibe somente o input name.
Com o input name preenchido e ao clicar em Pesquisar uma requisição POST é feita, o formulário
é valido, os dados são extraidos a função getPersonalDataByName de service é invocada e os dados são
enviados para o search.html
"""

def search(request):
    data = {}

    if request.method == "POST":
        data_input = FormPersonalData(request.POST)

        if data_input.is_valid():
            name = data_input.cleaned_data['name']
            # busca pelo texto digitado no input name. Se encontrdo, data['personal_data']
            # é preenchido e enviado para o search.html
            personal_data = getPersonalDataByName(name)
            data['personal_data'] = personal_data
            
    # instancia do formulário criada no dicionário data para ser enviado ao html
    data['form_personal_data'] = FormPersonalData()
            
    return render(request, 'remembermm/search.html', data)
