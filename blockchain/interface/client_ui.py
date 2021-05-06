from blockchain.client import Client


class ClientUI:
    def __init__(self):
        self.client = Client()
        self.info = self.output_client_info()

    def output_client_info(self):
        """Outputs the clients public key and client_id"""

        with open('private_key.json', 'w') as s_file:
            s_file.write(self.client._Client__private_key.exportKey().decode())
            s_file.close()

        print('Public key is:\n', self.client.public_key.exportKey().decode())
        print('\n')
        print('Client ID is:\n', self.client.client_id)
        return 0
