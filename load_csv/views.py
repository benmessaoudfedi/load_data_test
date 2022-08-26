from django.shortcuts import render
import csv, io
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.forms.models import model_to_dict
import json
from .models import Documents


def index(request):
    return render(request, 'home.html')


def is_csv(name):
    return name.endswith('.csv')


def is_empty(data_set):
    return True if sum(1 for column in csv.reader(data_set, delimiter='|')) == 0 else False


def is_equal_columns(dataset):
    return True if len(next(csv.reader(dataset, delimiter='|'))) == 7 else False


def import_csv_view(request):
    if request.method == 'GET':
        return render(request, 'import_csv_view.html')
    elif request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a csv file')
            return render(request, 'import_csv_view.html')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        if not is_equal_columns(io_string):
            messages.error(request, 'Wrong Number of columns')
            return render(request, 'import_csv_view.html')
        # if is_empty(io_string):
        #     messages.error(request, 'The file is empty')
        #     return render(request, 'import_csv_view.html')

        # next(io_string)

        for column in csv.reader(io_string, delimiter='|'):
            _, created = Documents.objects.update_or_create(
                NUMDOS=column[0],
                NUMDOSVERLING=column[1],
                ANCART=column[2],
                FILIERE=column[3],
                ETAPE=column[4],
                VERLING=column[5],
                FORMAT=column[6],

            )
        messages.success(request, 'Load Data Completed, You Can Load another CSV file')
        return render(request, 'import_csv_view.html')


def document_support(request, numdos):
    document = Documents.objects.get(NUMDOS=numdos)
    doc_dict = model_to_dict(document)
    doc_serialized = json.dumps(doc_dict)

    return HttpResponse(doc_serialized)
