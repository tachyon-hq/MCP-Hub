# MCP Hub Pull_Request 컨벤션

이 문서는 MCP Hub 프로젝트의 Pull Request(PR)에 대한 컨벤션을 정의합니다.

## 1. Pull Request (PR) 컨벤션

### PR 제목

PR 제목은 `Conventional Commits` 표준을 따르며, 최종적으로 Squash & Merge 될 때의 커밋 메시지가 됩니다.

**`<type>(<scope>): <subject>`**

### PR 본문

PR을 생성할 때, 자동으로 적용되는 `.github/PULL_REQUEST_TEMPLATE.md`의 모든 항목을 아래 형식에 맞춰 성실하게 작성해야 합니다.

- **문제 정의:** 이 PR이 해결하려는 문제나 목표를 명확히 기술합니다.
- **해결 방안:** 문제를 어떤 방식으로 해결했는지 구체적인 구현 내용을 설명합니다.
- **근거:** 이 해결 방안을 선택한 기술적 배경이나 이유를 제시합니다.
