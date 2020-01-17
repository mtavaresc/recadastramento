from prettytable import PrettyTable
from sqlalchemy import and_, func
from datetime import datetime

from models.admin import *

begin = datetime.now().replace(microsecond=0)

# select f1.*
# from zeus.tb_fin f1
# right join (select fin_matr,
#                 max(fin_dtsai) as ultima_saida
#             from zeus.tb_fin
#             group by fin_matr) f2
# on f1.fin_matr = f2.fin_matr and f1.fin_dtsai = f2.ultima_saida
# where f1.fin_matr = '000034'
#     and f1.fin_sit = 0;
# .join(f1, f1.c.fin_matr == Cadastro.cad_matr)

f2 = db.session.query(Financeiro.fin_matr, func.max(Financeiro.fin_dtsai).label('saida')) \
    .group_by(Financeiro.fin_matr).subquery()

f1 = db.session.query(Financeiro.fin_matr, Financeiro.fin_dtsai) \
    .join(f2, and_(f2.c.fin_matr == Financeiro.fin_matr, f2.c.saida == Financeiro.fin_dtsai)).subquery()

ff2 = db.session.query(FichaFinanceira.fic_matr, func.max(FichaFinanceira.fic_codfp).label('ultima')) \
    .group_by(FichaFinanceira.fic_matr).subquery()

ff1 = db.session.query(FichaFinanceira.fic_matr, FichaFinanceira.fic_valor) \
    .join(ff2, and_(ff2.c.fic_matr == FichaFinanceira.fic_matr, ff2.c.ultima == FichaFinanceira.fic_codfp)) \
    .filter(FichaFinanceira.fic_cod.in_(['109', '139'])).subquery()

consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                            Cadastro.cad_matr, Cadastro.cad_nome) \
    .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
    .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
    .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
    .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
    .filter(
    and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
         Lotacao.lot_desc.like('GT%'),
         Lotacao.lot_cod.like('GT38%'),
         Financeiro.fin_folha == '03',
         CargoFuncao.car_ativo == 'S',
         HistoricoFuncao.hst == 'S',
         Financeiro.fin_sit == 1,
         func.extract('month', HistoricoFuncao.hdtini) == 5,
         func.extract('year', HistoricoFuncao.hdtini) == 2019
         )) \
    .order_by(CargoFuncao.car_desc, Lotacao.lot_desc)

# t = PrettyTable(['Matrícula', 'Nome', 'Função', 'Lotação', 'Valor'])
t = PrettyTable(['Matrícula', 'Nome', 'Funçao', 'Lotação'])

for r in consulta:
    # if r.cad_matr == '032504':
    # t.add_row([r.cad_matr, r.cad_nome, r.car_desc, r.lot_desc, r.fic_valor])
    t.add_row([r.cad_matr, r.cad_nome, r.car_desc, r.lot_desc])

print(t)

end = datetime.now().replace(microsecond=0)

print('\n Time elapsed: {}'.format(end - begin))
