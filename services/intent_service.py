from sqlmodel import Session, select
from models.intent_model import Intent


class IntentService:
    def __init__(self) -> None:
        pass

    def get_all_intents(self, session: Session):
        statement = select(Intent)
        result = session.exec(statement).all()
        return result

    def get_all_intents_of_a_workflow(self, workflow_id: str, session: Session):
        statement = select(Intent).where(Intent.workflow_id == workflow_id)
        result = session.exec(statement).all()
        return result


intent_service = IntentService()
