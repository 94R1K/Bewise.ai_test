from datetime import datetime
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import (Boolean, Column, DateTime, Integer, String,
                        create_engine)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "postgresql://postgres_user:postgres_password@postgres/postgres"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(
        String,
        index=True,
        unique=True
    )
    answer_text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


class QuestionCreate(BaseModel):
    questions_num: int


@app.post("/get_questions/")
async def get_questions(questions_data: QuestionCreate):
    questions_num = questions_data.questions_num
    counter = 0

    db_session = SessionLocal()

    try:
        while counter < questions_num:
            response = requests.get(
                f"https://jservice.io/api/random?count={questions_num}"
            )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=500,
                    detail=f"Ошибка при запросе к API: {response.status_code}!"
                )

            data = response.json()

            if data:
                question_data = data[0]
                question_text = question_data["question"]
                answer_text = question_data["answer"]

                existing_question = db_session.query(Question).filter_by(
                    question_text=question_text
                ).first()

                if not existing_question:
                    try:
                        db_question = Question(
                            question_text=question_text,
                            answer_text=answer_text
                        )

                        db_session.add(db_question)
                        db_session.commit()

                        counter += 1

                    except IntegrityError:
                        db_session.rollback()
                else:
                    continue

    except Exception as e:
        db_session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        last_question = db_session.query(Question).order_by(
            Question.created_at.desc()).first()
        db_session.close()

        if not last_question:
            return {}
        return {"last_question": last_question.question_text}
