from datetime import datetime

from prettytable import PrettyTable
from sqlalchemy import and_, or_, func, case

from models.admin import *

begin = datetime.now().replace(microsecond=0)

subquery = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                            case([
                                (
                                    and_(or_(Lotacao.lot_desc.like('PRG%'), Lotacao.lot_desc.like('GT%')),
                                         CargoFuncao.car_desc.like('SECRETARIO%')),
                                    7 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    and_(or_(Lotacao.lot_desc.like('PRG%'), Lotacao.lot_desc.like('GT%')),
                                         CargoFuncao.car_desc.like('MEMBRO%')),
                                    12 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    and_(or_(Lotacao.lot_desc.like('PRG%'), Lotacao.lot_desc.like('GT%')),
                                         CargoFuncao.car_desc.like('ASSESSOR%')),
                                    16 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    and_(or_(Lotacao.lot_desc.like('PRG%'), Lotacao.lot_desc.like('GT%')),
                                         CargoFuncao.car_desc.like('COORDENADOR%')),
                                    10 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    and_(or_(Lotacao.lot_desc.like('PRG%'), Lotacao.lot_desc.like('GT%')),
                                         CargoFuncao.car_desc.like('SUPERVISOR%')),
                                    10 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    CargoFuncao.car_desc.like('SECRETARIO%'),
                                    3 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    CargoFuncao.car_desc.like('MEMBRO%'),
                                    4 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    CargoFuncao.car_desc.like('ASSESSOR%'),
                                    10 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    CargoFuncao.car_desc.like('COORDENADOR%'),
                                    7 - func.count(Cadastro.cad_matr)
                                ),
                                (
                                    CargoFuncao.car_desc.like('SUPERVISOR%'),
                                    5 - func.count(Cadastro.cad_matr)
                                )
                            ]).label('available'),
                            func.count(Cadastro.cad_matr).label('allocated')) \
    .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
    .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
    .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
    .filter(
    and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
         CargoFuncao.car_ativo == 'S',
         HistoricoFuncao.hst == 'S')) \
    .group_by(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc) \
    .order_by(CargoFuncao.car_desc, Lotacao.lot_desc).subquery()

query = db.session.query(
    func.sum(case([(and_(subquery.c.lot_desc.like('PRG%'), subquery.c.available < 0), 1)], else_=0)).label('prg_ex'),
    func.sum(case([(and_(subquery.c.lot_desc.like('PRG%'), subquery.c.available > 0), 1)], else_=0)).label('prg_np'),
    func.sum(case([(and_(subquery.c.lot_desc.like('PRG%'), subquery.c.available == 0), 1)], else_=0)).label('prg_pr'),

    func.sum(case([(and_(subquery.c.lot_desc.like('GT%'), subquery.c.available < 0), 1)], else_=0)).label('gt_ex'),
    func.sum(case([(and_(subquery.c.lot_desc.like('GT%'), subquery.c.available > 0), 1)], else_=0)).label('gt_np'),
    func.sum(case([(and_(subquery.c.lot_desc.like('GT%'), subquery.c.available == 0), 1)], else_=0)).label('gt_pr'),

    func.sum(case([(and_(subquery.c.lot_desc.like('SG%'), subquery.c.available < 0), 1)], else_=0)).label('sg_ex'),
    func.sum(case([(and_(subquery.c.lot_desc.like('SG%'), subquery.c.available > 0), 1)], else_=0)).label('sg_np'),
    func.sum(case([(and_(subquery.c.lot_desc.like('SG%'), subquery.c.available == 0), 1)], else_=0)).label('sg_pr'),

    func.sum(case([(and_(subquery.c.lot_desc.like('SUBPRG%'), subquery.c.available < 0), 1)], else_=0)).label(
        'subprg_ex'),
    func.sum(case([(and_(subquery.c.lot_desc.like('SUBPRG%'), subquery.c.available > 0), 1)], else_=0)).label(
        'subprg_np'),
    func.sum(case([(and_(subquery.c.lot_desc.like('SUBPRG%'), subquery.c.available == 0), 1)], else_=0)).label(
        'subprg_pr')
).first()

t = PrettyTable(
    ['PRG EX.', 'PRG NP.', 'PRG Pquery.', 'GT EX.', 'GT NP.', 'GT Pquery.', 'SG EX.', 'SG NP.', 'SG Pquery.',
     'SUBPRG EX.', 'SUBPRG NP.', 'SUBPRG Pquery.'])
# t = PrettyTable(['Cargo Cód.', 'Cargo', 'Lotação Cód.', 'Lotação', 'Disponível', 'Alocado'])

# for r in query:
t.add_row([query.prg_ex, query.prg_np, query.prg_pr, query.gt_ex, query.gt_np, query.gt_pr, query.sg_ex, query.sg_np,
           query.sg_pr, query.subprg_ex, query.subprg_np, query.subprg_pr])

print(t)

end = datetime.now().replace(microsecond=0)

print('\n Time elapsed: {}'.format(end - begin))
