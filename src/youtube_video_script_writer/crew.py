from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from tools.custom_tool import ScriptReadTimeEstimator
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class YoutubeVideoScriptWriter():
    """YoutubeVideoScriptWriter crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def hook_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['hook_specialist'], # type: ignore[index]
            verbose=True
        )

    @agent
    def script_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['script_writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def title_thumbnail_copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config['title_thumbnail_copywriter'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def hook_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['hook_creation_task'], # type: ignore[index]
            output_file='hook_creation.md'
        )

    @task
    def script_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['script_writing_task'],
            tools=[ScriptReadTimeEstimator()],# type: ignore[index]
            output_file='full_script.md'
        )

    @task
    def title_thumbnail_task(self) -> Task:
        return Task(
            config=self.tasks_config['title_thumbnail_task'],  # type: ignore[index]
            output_file='title_thumbnail.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the YoutubeVideoScriptWriter crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
