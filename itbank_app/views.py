from django.shortcuts import render
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modules'))

# import get_html_table from queries
from .modules.queries import get_html_table

def home(request):

    # se obtiene el query de la pagina
    if request.method == 'POST': 

        # se genera la tabla de html con el input del usuario
        tipo_operacion = request.POST.get('sql_query')

        # convertir el tipo de operacion a string
        tipo_operacion = str(tipo_operacion)

        # # se genera el archivo en base al query
        table_data = get_html_table(tipo_operacion)

        # returns the html template
        return render(request, 'index.html', {'table_data': table_data, 'tipo_operacion': tipo_operacion})

    return render(request, "index.html")
