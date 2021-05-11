from blockchain.client import Client


class ClientUI(Client):

    def output_client_info(self):
        """Outputs the clients public key and client_id"""

        with open('private_key.pem', 'wb') as s_file:
            s_file.write(self._Client__private_key.export_key('PEM'))
            s_file.close()

        print('Public key is:\n', self.public_key.exportKey().decode())
        print('\n')
        print('Client ID is:\n', self.client_id)
        return 0
