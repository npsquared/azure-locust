import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(0, 0)

    @task
    def ask_question(self):
        self.client.get("/", stream=True)
        #time.sleep(5)
        self.client.post(
            "/conversation",
            json={
                "messages": [
                    {
                        "content": random.choice(
                            [
                                "What is business analysis?",
                                "What is mind mapping?",
                                "What are some techniques published in the BABOK guide?",
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
#        time.sleep(5)
        self.client.post(
            "/conversation",
            json={
                "messages": [
                    {"content": "What is business analysis?", "role": "user"},
                    {
                        "content": "Business analysis is the practice of enabling change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders. It involves understanding the current state of the organization, identifying areas for improvement, and proposing changes to achieve desired outcomes . Business analysts are responsible for discovering, synthesizing, and analyzing information from various sources within an enterprise, including tools, processes, documentation, and stakeholders. They play a crucial role in aligning the designed and delivered solutions with the needs of stakeholders. The activities performed by business analysts include understanding enterprise problems and goals, analyzing needs and solutions, devising strategies, driving change, and facilitating stakeholder collaboration. Business analysis can be applied in various domains and industries, and it is not limited to a specific job title or organizational role.",
                        "role": "assistant",
                    },
                    {"content": "How can business analysis be applied to an organizational digital transformation?", "role": "user"},
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
