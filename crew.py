from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
from typing import List

# Output Schema for Basic Validation
class FAQItem(BaseModel):
    question: str
    answer: str

class FAQSchema(BaseModel):
    faqs: List[FAQItem]

@CrewBase
class FaqGeneratorCrew():
    """FAQ Generator Crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def analyzer(self) -> Agent:
        return Agent(config=self.agents_config['analyzer'], verbose=True)

    @agent
    def faq_writer(self) -> Agent:
        return Agent(config=self.agents_config['faq_writer'], verbose=True)

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'])

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            output_json=FAQSchema 
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
