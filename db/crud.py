from sqlmodel import select
from fastapi import HTTPException

def insert_row(row,session,table):
    new_row=table.model_validate(row)
    session.add(new_row)
    session.commit()
    session.refresh(new_row)
    return new_row

def select_rows(session,table):
    return session.exec(select(table)).all()

def select_row(id,session,table):
    row=session.get(table,id)
    if row is None:
            raise HTTPException(status_code=404,detail='not found')
    return row

def delete_row(id,session,table):
    row=session.get(table,id)
    session.delete(row)
    session.commit()


def update_row(id,session,table,updated_row):
    row=session.get(table,id)
    data_row=updated_row.model_dump(exclude_unset=True)
    row.sqlmodel_update(data_row)
    session.commit()
    session.refresh(row)