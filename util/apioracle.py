import requests
from json import dumps


class Acts:
    def __init__(self):
        self.base = 'http://apioracle.al.ce.gov.br/'
        self.key = '$2y$14$mssekBgJ/dhLafs6/H8xpufALWgvpujtWz2m/DNbjs9PhM2KeMlD2'

    def create(self, register):
        url = '{base}/gera_numero_ato.php?matr={register}&token={key}' \
            .format(base=self.base, register=register, key=self.key)
        response = requests.get(url)

        if response.text == '1':
            return True
        else:
            return False, response.text

    def list(self):
        url = '{base}/atos_lista.php?token={key}'.format(base=self.base, key=self.key)
        response = requests.get(url)
        code = False

        if response.text == '4':
            rs = 'TOKEN não passado pela aplicação requerente ou passado de forma incorreta.'
        elif response.text == '3':
            rs = 'TOKEN inexistente ou falso.'
        elif response.text == '2':
            rs = 'Falha na conexão.'
        elif response.text == 'false':
            rs = 'Não existem números de ATOS cadastrados!'
        else:
            rs = eval(response.text.replace('null', '\"\"'))
            code = True

        data = {'code': code, 'result': rs}

        return data


if __name__ == '__main__':
    # Create Act
    # create = Acts().create(register='031669')

    # if create:
        # List Acts
        acts = Acts().list()
        list_of_acts = []
        # Registrations of DRH people
        registrations = ['025164', '030108', '004018', '002968', '031669']

        if acts['code']:
            for act in acts['result']:
                if act['ATO_MATR'] in registrations:
                    print(dumps(act, indent=4))
                    list_of_acts.append('{num}/{ano}'.format(num=act['ATO_NUM'].zfill(4), ano=act['ATO_ANO']))

            print('\n{} ({})'.format(list_of_acts, len(list_of_acts)))
            print(max(list_of_acts))
    # else:
    #     print(create[1])
