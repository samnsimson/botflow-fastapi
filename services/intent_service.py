from sqlmodel import Session, select
from models.intent_model import Intent, IntentModel


class IntentService:
    def __init__(self) -> None:
        pass

    def get_all_intents(self, session: Session):
        statement = select(Intent)
        result = session.exec(statement).all()
        return result

    def get_intent_by_id(self, intent_id: str, session: Session):
        statement = select(Intent).where(Intent.id == intent_id)
        result = session.exec(statement).first()
        return result

    def get_all_intents_of_a_workflow(self, workflow_id: str, session: Session):
        statement = select(Intent).where(Intent.workflow_id == workflow_id)
        result = session.exec(statement).all()
        return result

    def create_intent(self, intent_data: IntentModel, session: Session):
        intent = Intent(**intent_data.model_dump())
        session.add(intent)
        session.commit()
        session.refresh(intent)
        return intent


intent_service = IntentService()
