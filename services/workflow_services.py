from models.workflow_model import WorkflowModel, Workflow
from sqlmodel import Session
from sqlalchemy.exc import SQLAlchemyError


class WorkflowServices:
    def create_workflow(self, data: WorkflowModel, session: Session) -> Workflow:
        try:
            workflow = Workflow(**data.model_dump())
            session.add(workflow)
            session.commit()
            session.refresh(workflow)
            return workflow
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating workflow: {e}")
            return None


workflow_service = WorkflowServices()
