from models.workflow_model import WorkflowModel, Workflow
from sqlmodel import Session, select
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Dict, Any
from uuid import UUID
from services.traverse import Traverse


class WorkflowServiceHelper:
    def __init__(self) -> None:
        pass

    def create_graph(self, nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]]):
        graph = {node['id']: [] for node in nodes}
        node_map = {node[id]: node for node in nodes}
        for edge in edges:
            if edge['target'] in node_map:
                node_item = {edge['target']: node_map[edge['target']]}
                graph[edge['source']].append(node_item)
        return graph


class WorkflowServices(WorkflowServiceHelper):
    def __init__(self) -> None:
        super().__init__()
        self.traverse = Traverse()

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

    def get_all_workflow(seld, session: Session) -> List[Workflow]:
        try:
            statement = select(Workflow)
            result = session.exec(statement).all()
            return result
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error fetching workflow: {e}")
            return None

    def get_workflow_by_id(self, id: UUID, session: Session) -> Workflow:
        try:
            statement = select(Workflow).where(Workflow.id == id)
            result = session.exec(statement).first()
            return result
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating workflow: {e}")
            return None

    def execute_workflow(self, id: UUID, session: Session):
        workflow = self.get_workflow_by_id(id, session)
        nodes, edges = workflow.nodes, workflow.edges
        graph = self.create_graph(nodes, edges)
        start_node = None
        for node in nodes:
            if node.get("type") == "START":
                start_node = node
                break
        if start_node is None:
            raise ValueError("No start node found in the workflow")
        return self.traverse.dfs(graph, start_node.get('id'))


workflow_service = WorkflowServices()
