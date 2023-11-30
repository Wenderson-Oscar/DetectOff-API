from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from model.open_model import OffensiveTextClassifier
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./comments.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String)
    type = Column(String)

Base.metadata.create_all(bind=engine)

class TextInput(BaseModel):
    text: str

offensive_classifier = OffensiveTextClassifier('model/ML/offensive_tfidf_svm.pkl/offensive_tfidf_svm.pkl', 'model/ML/vectorizer.pkl')

with open("view/index.html", "r") as html_file:
    html_content = html_file.read()

@app.get("/", response_class=HTMLResponse)
def home():
    offensive_comments = grafic_offensive()
    return HTMLResponse(content=html_content)

@app.post("/comment/")
def predict(request: Request, text: str = Form(...)):
    prediction = offensive_classifier.predict_offensive_texts([text])
    if not prediction:
        raise HTTPException(status_code=500, detail="Erro ao fazer a previsão")
    result = f"Comentário: {text}, "
    if prediction[0][1] == 'nonoffensive':
        result += f"Resultado: Não Ofensivo"
        register_nonoffensive_comment(text)
    else:
        result += f"Resultado: Ofensivo"
        register_offensive_comment(text)
    return result 

def register_offensive_comment(comment):
    db = SessionLocal()
    db_comment = Comment(text=comment, type="offensive")
    db.add(db_comment)
    db.commit()
    db.close()

def register_nonoffensive_comment(comment):
    db = SessionLocal()
    db_comment = Comment(text=comment, type="nonoffensive")
    db.add(db_comment)
    db.commit()
    db.close()

@app.get("/grafic/offensive_comments")
def grafic_offensive():
    db = SessionLocal()
    offensive_comments = db.query(Comment).filter(Comment.type == 'offensive').all()
    db.close()
    return offensive_comments

@app.get("/grafic/nonoffensive_comments")
def grafic_nonoffensive():
    db = SessionLocal()
    nonoffensive_comments = db.query(Comment).filter(Comment.type == 'nonoffensive').all()
    db.close()
    return nonoffensive_comments
