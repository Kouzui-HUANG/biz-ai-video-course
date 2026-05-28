# Git & GitHub Pusher 技能指南

這項技能的目的是協助自動化將本地專案上傳（Push）到遠端 GitHub 數據庫的流程。

## 執行流程

當系統被觸發（例如你輸入「push」、「上傳github」或類似需求）時，AI 會執行以下標準與自動化流程：

1. **檢查與初始化 Git**：確保目前的專案目錄擁有 Git 版本控制。如果找不到 `.git`，AI 會自動為你執行 `git init` 並完成 `Initial commit`。如已有未提交的變更，也會一併幫你提交。
2. **確認或要求提供遠端網址（Remote URL）**：如果發現本地端尚未連結到任何遠端 `origin`，AI 會直接請你先至 GitHub 建立一個空專案，並將遠端的網址貼上。
3. **解決遠端衝突與無關的歷史紀錄**：如果你在 GitHub 建立專案時，不小心勾選了建立 README 或 LICENSE，AI 會自動執行 `--allow-unrelated-histories` 抓取內容並幫助你解決檔案的合併衝突。
4. **一鍵推播 (Push)**：最後自動執行 `git push -u origin main`。系統會在背景確認推播成功，並向你回報已完成上傳任務。
