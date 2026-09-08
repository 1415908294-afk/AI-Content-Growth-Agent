class ScriptAgent:

    def generate_script(self, topic):

        return {
            "hook": "你知道这个知识吗？",
            "body": topic,
            "ending": "评论告诉我你想学什么"
        }
