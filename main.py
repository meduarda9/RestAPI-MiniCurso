from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []

@app.get("/")
def root():
    return{"Hello": "World"} #É a nossa rota padrão

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item = items[item_id]
    return item

@app.get("/items")
def list_items(limite: int = 5): ##Utilizará 5 por padrão caso o limite não seja informado
    if len(items) > 0:
        return items[0:limite]
    else: 
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
@app.put("/item/{item_id}")
def update_item(item_id: int, new_item: str):
    if item_id <len(items):
        items[item_id] = new_item
        return{"msg": "Item atualizado", "items": items}
    else:
        raise HTTPException(status_code=404, detail="Item não encontrado")

@app.delete("/items/{item_id}")
def update_item(item_id: int):
    if item_id < len(items):
        removed_item = items.pop(item_id)
        items[item_id] = removed_item
        return {"msg": "Item removido", "item": removed_item}
    else:
        raise HTTPException(status_code=404, detail="Item não encontrado")