from datetime import datetime

from prettytable import PrettyTable
from sqlalchemy import and_

from models.admin import *

begin = datetime.now().replace(microsecond=0)

matricula = '002968'

consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                            Cadastro.cad_matr, Cadastro.cad_nome) \
    .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
    .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
    .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
    .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
    .filter(
    and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
         Financeiro.fin_folha == '03',
         CargoFuncao.car_ativo == 'S',
         HistoricoFuncao.hst == 'S',
         Financeiro.fin_sit == 1,
         Cadastro.cad_matr == matricula)) \
    .order_by(CargoFuncao.car_desc, Lotacao.lot_desc)

t = PrettyTable(['Cód. Cargo', 'Cargo', 'Cód. Lotação', 'Lotação', 'Matrícula', 'Nome'])

for r in consulta:
    t.add_row([r.car_cod, r.car_desc, r.lot_cod, r.lot_desc, r.cad_matr, r.cad_nome])

print(t)

end = datetime.now().replace(microsecond=0)

print('\n Time elapsed: {}'.format(end - begin))
