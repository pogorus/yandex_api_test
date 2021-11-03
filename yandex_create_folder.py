import requests

def yandex_create_folder(token, folder_name):
    headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'
    }
    return requests.put('https://cloud-api.yandex.net:443/v1/disk/resources', params={'path': folder_name}, headers=headers)

def yandex_delete_folder(token, folder_name):
    headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'
    }
    return requests.delete('https://cloud-api.yandex.net:443/v1/disk/resources', params={'path': folder_name}, headers=headers)

ya_token = ''
