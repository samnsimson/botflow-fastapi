from fastapi import APIRouter, Depends
from models.workflow_model import WorkflowModel
from sqlmodel import Session
from database import get_session
from services.workflow_services import workflow_service

router = APIRouter(tags=['Workflow'])


@router.post('/')
def create_workflow(data: WorkflowModel, session: Session = Depends(get_session)):
    return workflow_service.create_workflow(data=data, session=session)
