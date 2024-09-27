from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from database import get_session
from models.intent_model import Intent
from typing import List, Optional
from constants import intent_workflow_id_description
from services.intent_service import intent_service

router = APIRouter(tags=['Intent'])


@router.get("/", response_model=List[Intent])
def get_all_intents_of_a_worflow(workflow_id: Optional[str] = Query(None,  description=intent_workflow_id_description), session: Session = Depends(get_session)):
    return True if workflow_id is None else False
