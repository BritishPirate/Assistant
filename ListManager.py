from todoist_api_python.api import TodoistAPI
from datetime import datetime, date

class ListManager:
    
    api = TodoistAPI(token = 'fc9351fe2510c7430866145958c63e85b9fd602d')
    
    def addTask(self, content, description = None, projectId = None, sectionId = None, parentId = None, order = None, lables = None, priority = None, due = None):
        api = self.api
        api.add_task(
            content=content, 
            description = description,
            project_id = projectId,
            section_id = sectionId,
            parent_id = parentId,
            lables = lables,
            priority = priority,
            due_string = due if isinstance(due, str) else None,
            due_date = due.isoformat() if isinstance(due, date) else None,
            due_datetime = due.isoformat() if isinstance(due, datetime) else None,
            )

    def addSection(self, name, projectId, order = None):
        api = self.api
        api.add_section(
            name=name,
            project_id=projectId,
            order=order
        )

    def updateTask(self, taskId, content = None, description = None, lables = None, priority = None, due = None):
        api = self.api
        api.update_task(
            task_id = taskId,
            content=content, 
            description = description,
            lables = lables,
            priority = priority,
            due_string = due if isinstance(due, str) else None,
            due_date = due.isoformat() if isinstance(due, date) else None,
            due_datetime = due.isoformat() if isinstance(due, datetime) else None,
        )

    def updateSection(self, sectionId, name):
        api = self.api
        api.update_section(section_id=sectionId, name=name)

    def completeTask(self, taskId):
        api = self.api
        api.close_task(task_id = taskId)

    def deleteTask(self, taskId):
        api = self.api
        api.delete_task(task_id=taskId)

    def deleteSection(self, sectionId):
        api = self.api
        api.delete_section(section_id=sectionId)

    #region get stuff
    def getProjects(self):
        api = self.api
        try:
            projects = api.get_projects()
            return projects
        except Exception as error:
            print(error)
    
    def getLables(self):
        api = self.api
        lists = api.get_labels()
        return
    
    def getSections(self, projectId):
        api = self.api
        sections = api.get_sections()

    def getTasks(self, projectId = None, sectionId = None):
        api = self.api
        tasks = api.get_tasks(project_id = projectId if projectId else None, section_id = sectionId if sectionId else None)
        return tasks
    #endregion