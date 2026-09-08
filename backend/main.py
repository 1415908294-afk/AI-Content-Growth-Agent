from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="AI Content Growth Agent",
    description="AI short video operation assistant"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ContentRequest(BaseModel):
    industry: str
    platform: str
    audience: str
    duration: str

@app.get("/")
def home():
    return {"message": "AI Content Growth Agent Running"}

@app.post("/generate")
def generate_content(request: ContentRequest):
    return {
        "topic": f"{request.industry}爆款短视频选题",
        "script": "0-3秒：制造冲突吸引注意\n3-30秒：输出核心内容\n30-40秒：评论互动引导",
        "storyboard": [
            "Scene 1: 黄金3秒开场",
            "Scene 2: 内容展示与案例",
            "Scene 3: 用户互动转化"
        ],
        "translation": "Generate overseas English version",
        "analysis": "根据数据表现持续优化内容"
    }
