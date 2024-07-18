from fastapi import FastAPI,  Depends, HTTPException
from schemas.schemas import TodoBase
from models.models import Todo , SessionLocal
from config.database import connection
from sqlalchemy.orm import Session

app =FastAPI() 


def get_db(): 
    db = SessionLocal() 
    
    try: 
        yield db 
    finally : 
        db.close()


@app.get('/')
def root():
    return {'message':"Hello World"}

@app.get('/todos')
async def get_all_todo(db:Session = Depends(get_db)): 
    result = db.query(Todo).all()
    print(result)
    return  result

@app.get('/todos/{id}')
def get_todo(id, db:Session = Depends(get_db)): 
    result = db.query(Todo).filter(Todo.id==id).first()
    return result

@app.post('/create_todo/')
def create_todo(todo:TodoBase,db:Session = Depends(get_db)): 
    todo = Todo(description = todo.description, status = todo.status, )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    
    print(todo)
    return {"Message":"Todo created"}


@app.put('/update_todos/{id}')
def update_todos(id , todo:TodoBase,  db:Session =Depends(get_db)): 
    update_todo = db.query(Todo).filter(Todo.id==id).first()  
    
    if update_todo : 
        update_todo.description = todo.description
        update_todo.status      = todo.status
        
        db.commit() 
        db.refresh(update_todo)
        
        # update_todo = db.query(Todo).filter(Todo.id==id).first()  

        
        return update_todo
    else : 
        return {"Message":'Todo not found'}
    

@app.delete('/delete_todos/{id}')
def delete_todos(id , db:Session = Depends(get_db)): 
    deleted_todo = db.query(Todo).filter(Todo.id==id).first()
    if deleted_todo : 
        db.delete(deleted_todo)
        db.commit()
        return {"Message":'Todo Deleted'}
    else : 
        return  {"Message":'Todo not found'} 
    