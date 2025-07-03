from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# GitHub API 토큰 설정 (환경 변수에서 로드)
github_token = os.getenv("GITHUB_TOKEN")
g = Github(github_token) if github_token else Github()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    servers = []
    try:
        # "mcp-server" 키워드를 포함하는 모든 공개 리포지토리 검색
        # in:name은 리포지토리 이름에서만 검색하도록 제한합니다.
        # PyGithub의 search_repositories는 기본적으로 공개 리포지토리를 검색합니다.
        for repo in g.search_repositories(query="mcp-server in:name"):
            servers.append({
                "name": repo.full_name,
                "url": repo.html_url
            })
    except Exception as e:
        print(f"Error searching GitHub repositories: {e}")
        # 에러 발생 시 빈 목록과 에러 메시지를 전달
        return templates.TemplateResponse("index.html", {"request": request, "servers": [], "error": str(e)})

    return templates.TemplateResponse("index.html", {"request": request, "servers": servers})
