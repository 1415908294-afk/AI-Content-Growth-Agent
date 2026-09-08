class StoryboardAgent:

    def generate_storyboard(self, script):

        return {
            "scenes": [
                {
                    "time": "0-3s",
                    "visual": "强吸引力开场画面",
                    "voice": "提出用户痛点"
                },
                {
                    "time": "3-30s",
                    "visual": "核心内容展示",
                    "voice": script
                },
                {
                    "time": "30-40s",
                    "visual": "互动引导画面",
                    "voice": "关注并评论"
                }
            ]
        }
