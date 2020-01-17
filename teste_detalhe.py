from prettytable import PrettyTable
from sqlalchemy import and_, func
from datetime import datetime

from models.admin import *

begin = datetime.now().replace(microsecond=0)

# SELECT FF1.*
# FROM ZEUS.TB_FICFIN FF1
# RIGHT JOIN (SELECT FIC_MATR, MAX(FIC_CODFP) ULTIMA
#         FROM ZEUS.TB_FICFIN
#         GROUP BY FIC_MATR) FF2
# ON FF1.FIC_MATR = FF2.FIC_MATR AND FF1.FIC_CODFP = FF2.ULTIMA
# WHERE FF1.FIC_COD IN ('109', '139')
#     AND FF1.FIC_MATR = '018420'

# query = query.outerjoin(
#     sub_query, and_(
#         sub_query.c.personId == CalendarEventAttendee.personId,
#         sub_query.c.eventId == CalendarEventAttendee.eventId)
#     )

ff2 = db.session.query(FichaFinanceira.fic_matr, func.max(FichaFinanceira.fic_codfp).label('ultima')) \
    .group_by(FichaFinanceira.fic_matr).subquery()

ff1 = db.session.query(FichaFinanceira.fic_matr, FichaFinanceira.fic_valor) \
    .join(ff2, and_(ff2.c.fic_matr == FichaFinanceira.fic_matr, ff2.c.ultima == FichaFinanceira.fic_codfp)) \
    .filter(FichaFinanceira.fic_cod.in_(['109', '139'])).subquery()

consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                            Lotacao.lot_desctot, Lotacao.lot_ato, Cadastro.cad_matr, Cadastro.cad_nome,
                            ff1.c.fic_valor) \
    .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
    .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
    .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
    .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
    .join(ff1, ff1.c.fic_matr == Cadastro.cad_matr) \
    .filter(
    and_(CargoFuncao.car_cod == 'G004',
         Lotacao.lot_cod == 'GT38160',
         Financeiro.fin_folha == '03',
         CargoFuncao.car_ativo == 'S',
         Financeiro.fin_sit == 0,
         HistoricoFuncao.hst == 'N')) \
    .order_by(Cadastro.cad_nome)

t = PrettyTable(['Matrícula', 'Nome', 'Função', 'Lotação', 'Valor'])

for r in consulta:
    t.add_row([r.cad_matr, r.cad_nome, r.car_desc, r.lot_desc, r.fic_valor])

print(t)

end = datetime.now().replace(microsecond=0)

print('\n Time elapsed: {}'.format(end - begin))
