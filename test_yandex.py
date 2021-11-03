from yandex_create_folder import ya_token, yandex_create_folder, yandex_delete_folder

class TestCreateFolder:

    def test_yandex_create_folder(self):
        assert yandex_create_folder(ya_token, 'new_folder').status_code == 201
        yandex_delete_folder(ya_token, 'new_folder')

    def test_wrong_token(self):
        assert yandex_create_folder('wrong token', 'new_folder').status_code == 401

    def test_folder_already_exist(self):
        yandex_create_folder(ya_token, 'already_exist')
        assert yandex_create_folder(ya_token, 'already_exist').status_code == 409
        yandex_delete_folder(ya_token, 'already_exist')
