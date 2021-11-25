from django.shortcuts import redirect, render

from remembermm.forms.form_personal_data import FormPersonalData
from remembermm.entity.entity_personal_data import EntityPersonalData
from remembermm.services.services_personal_data import getPersonalDataAll, getPersonalDataById, editPersonalData


"""
A função editData carrega o formulário (FormPersonalData) e busca na base de de dados
todos os cadastros já realizados (getPersonalDataAll) e o cadastro em específico através do ID getPersonalDataById
Com o formulário editado, cria-se uma instância de EntityPersonalData com seus devidos atributos.
Esta instância é envaido para o service fazer o update na base de dados e então a aplicação é
redirecionada para a página home
"""

def editData(request, id):
    data = {}

    personal_data_db = getPersonalDataById(id)

    """ acessa se a requisição for do tipo POST, ou seja, quando o botão salvar dados for pressionado
    e os dados estiverem devidamente preenchidos. Em seguida o formulário é validado e então os dados
    são extraidos e edidato na base de dados.
    """
    if request.method == "POST":
        data_input = FormPersonalData(request.POST)

        if data_input.is_valid():
            name = data_input.cleaned_data['name']
            email = data_input.cleaned_data['email']
            phone = data_input.cleaned_data['phone']

            # cria uma entidade EntityPersonalData e depois chama o service editPersonalData 
            # para fazer o update na base de dados
            personal_data_entity = EntityPersonalData(name, email, phone)
            editPersonalData(personal_data_db, personal_data_entity) 

            return redirect('home')      

    else:

        # se a requisição não for do tipo POST, então o formulário retorna preenchido para
        # a página home.html com os dados que deverão ser editados
        data['form_personal_data'] = FormPersonalData(request.POST or None, instance=personal_data_db)

    data['personal_data_all'] = getPersonalDataAll()
            
    return render(request, 'remembermm/home.html', data)