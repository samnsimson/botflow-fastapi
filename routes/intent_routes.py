from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from database import get_session
from models.intent_model import Intent, IntentModel
from typing import List, Optional
from constants import intent_workflow_id_description
from services.intent_service import intent_service

router = APIRouter(tags=['Intent'])


@router.get("/", response_model=List[Intent])
def get_all_intents_of_a_worflow(workflow_id: Optional[str] = Query(None,  description=intent_workflow_id_description), session: Session = Depends(get_session)):
    return intent_service.get_all_intents(session) if workflow_id is None else intent_service.get_all_intents_of_a_workflow(workflow_id, session)


@router.get('/{intent_id}', response_model=Intent)
def get_intent_by_id(intent_id: str, session: Session = Depends(get_session)):
    return intent_service.get_intent_by_id(intent_id, session)


@router.post('/', response_model=Intent)
def create_intent(intent_data: IntentModel, session: Session = Depends(get_session)):
    return intent_service.create_intent(intent_data, session)
