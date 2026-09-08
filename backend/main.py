from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Content Growth Agent",
    description="AI short video operation assistant"
)


class ContentRequest(BaseModel):
    industry: str
    platform: str
    audience: str
    duration: str


@app.get("/")
def home():
    return {
        "message": "AI Content Growth Agent Running"
    }


@app.post("/generate")
def generate_content(request: ContentRequest):

    result = {
        "topic": f"{request.industry}爆款短视频选题",
        "script": "0-3秒：吸引用户注意\n3-30秒：核心内容输出\n30-40秒：互动引导",
        "storyboard": [
            "Scene 1: 开场场景",
            "Scene 2: 展示内容",
            "Scene 3: 用户互动"
        ]
    }

    return result
