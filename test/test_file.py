import pandas as pd
import pytest
from django.urls import reverse
from django.test import Client

from load_csv.models import Documents


def test_is_csv(name='obfuscated.csv'):
    assert name.endswith('.csv') is True, f'error not csv file'


def test_is_csv2(name='obfuscated.xls'):
    assert name.endswith('.csv') is not True, f'error not csv file'


@pytest.mark.django_db
def test_document_create():
    Documents.objects.create(NUMDOS='HA954028', NUMDOSVERLING='HA954028', ANCART='A09343', FILIERE='FRA', ETAPE=99.60,
                             VERLING='F', FORMAT='PDFI')
    assert Documents.objects.count() == 1


@pytest.mark.django_db
def test_view(client):
    url = reverse('csv_upload')
    response = client.get(url)
    assert response.status_code == 200


client = Client()
print(client.get('/document-support/', {'NUMDOS': 'DD241051'}))


