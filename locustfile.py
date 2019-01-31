from locust import HttpLocust, TaskSet, task

class UserBehaviour(TaskSet):

    @task
    def get_tests(self):
        self.client.post("/test_get_questions/", {
            "test_id": 30
            })


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour


        
