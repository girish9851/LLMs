from locust import HttpUser, task, between

class AgentUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def send_query(self):
        self.client.get("/run", params={"query": "Tell me something interesting about AI"})
