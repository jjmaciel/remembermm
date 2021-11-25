from django.shortcuts import render

from remembermm.forms.form_personal_data import FormPersonalData
from remembermm.entity.entity_personal_data import EntityPersonalData
from remembermm.services.services_personal_data import addPersonalData, getPersonalDataAll

"""
A função home carrega o formulário (FormPersonalData) e busca na base de de dados
todos os cadastros já realizados (getPersonalDataAll).
Com o formulário preenchido, cria-se uma instância de EntityPersonalData com seus devidos atributos.
Esta instância é envaido para o service fazer o cadastro na base de dados.
"""

def home(request):
    data = {}

    """ acessa se a requisição for do tipo POST, ou seja, quando o botão salvar dados for pressionado
    e os dados estiverem devidamente preenchidos. Em seguida o formulário é validado e então os dados
    são extraidos e persistido no banco de dados.
    """
    if request.method == "POST":
        data_input = FormPersonalData(request.POST)

        if data_input.is_valid():
            name = data_input.cleaned_data['name']
            email = data_input.cleaned_data['email']
            phone = data_input.cleaned_data['phone']

            # momento que uma intância EntityPersonalData é criada e os dados persistidos. 
            personal_data_entity = EntityPersonalData(name, email, phone)
            addPersonalData(personal_data_entity)           

    # instâncias do formulário e dados cadstrados no DB criada no dicionário data para ser enviado ao html
    data['form_personal_data'] = FormPersonalData()
    data['personal_data_all'] = getPersonalDataAll()
            
    return render(request, 'remembermm/home.html', data)
