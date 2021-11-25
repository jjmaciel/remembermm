from django.shortcuts import redirect, render

from remembermm.forms.form_personal_data import FormPersonalData
from remembermm.services.services_personal_data import getPersonalDataAll, getPersonalDataById, removePersonalData

"""
A função removeData busca na base de de dados todos os cadastros já realizados (getPersonalDataAll).
Busca também por um registro específico através do ID getPersonalDataById. Exibe na página home.html
uma mesagem de confirmação através do data['confirm_delete']. Se o usuário clicar em sim uma requisição
do tipo POST é feita e então é chamado a função removePersonalData enviando o objeto a ser deletado
Em seguida a aplicação é redirecionada para a página home
""" 
def removeData(request, id):
    data = {}
    personal_data_db = getPersonalDataById(id)
    
    if request.method == "POST":
        removePersonalData(personal_data_db)
        return redirect('home')

    else:
        # instâncias do formulário e dados cadstrados no DB criada no dicionário data para ser enviado ao html
        data['form_personal_data'] = FormPersonalData()
        data['personal_data'] = personal_data_db
        data['confirm_delete'] = True

    data['personal_data_all'] = getPersonalDataAll()
            
    return render(request, 'remembermm/home.html', data)