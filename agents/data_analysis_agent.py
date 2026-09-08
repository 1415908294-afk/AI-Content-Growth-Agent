class DataAnalysisAgent:

    def analyze(self, views, likes, comments):

        engagement_rate = 0

        if views > 0:
            engagement_rate = (likes + comments) / views

        return {
            "engagement_rate": engagement_rate,
            "suggestion": "根据数据优化下一轮选题"
        }
