from fastapi import APIRouter, Depends
from models.workflow_model import WorkflowModel, Workflow
from sqlmodel import Session
from database import get_session
from services.workflow_services import workflow_service
from typing import List
from uuid import UUID

router = APIRouter(tags=['Workflow'])


@router.get('/', response_model=List[Workflow])
def get_all_workflow(session: Session = Depends(get_session)):
    return workflow_service.get_all_workflow(session)


@router.get('/execute/{workflow_id}')
def execute_workflow(workflow_id: UUID, session: Session = Depends(get_session)):
    return workflow_service.execute_workflow(workflow_id, session)


@router.post('/', response_model=Workflow)
def create_workflow(data: WorkflowModel, session: Session = Depends(get_session)):
    return workflow_service.create_workflow(data, session)
