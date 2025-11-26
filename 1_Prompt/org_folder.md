# 任务：{文件夹} 归类 — 机器可识别版（供 cline 使用）
元数据
- name: folder-classify
- version: 1.0
- platform: windows
- encoding: utf-8
- input-param: {文件夹}  （Obsidian Vault 中的目标根文件夹路径，相对或绝对）

步骤说明（机器可执行）
1. 获取目录结构（内部记录，禁止直接向用户输出）
   - 描述：递归读取 {文件夹} 的完整目录结构（包含所有子文件夹）。
   - 输出文件（内部）：directory_tree.json
   - PowerShell 示例（推荐）：
     - 将 JSON 写入 UTF-8：
       - powershell -Command "Get-ChildItem -LiteralPath 'C:\\Users\\peijun.shui1\\OneDrive\\Personal\\myVault\\{文件夹}' -Recurse -Directory | Select-Object FullName,Name,Parent | ConvertTo-Json -Depth 10 | Out-File -FilePath directory_tree.json -Encoding utf8"
   - 约束：记录所有层级，但不对外输出结果（cline 内部使用）。

2. 读取收件箱内容（列出文件名）
   - 描述：读取 {文件夹}（含所有子文件夹）中所有文件的文件名与相对路径。
   - 输出文件：inbox_files.json
   - PowerShell 示例：
     - powershell -Command "Get-ChildItem -LiteralPath 'C:\\Users\\peijun.shui1\\OneDrive\\Personal\\myVault\\{文件夹}' -Recurse -File | Select-Object FullName,Name,DirectoryName,Extension | ConvertTo-Json -Depth 5 | Out-File -FilePath inbox_files.json -Encoding utf8"

3. 内容分析与分类规划（生成建议，但不移动）
   - 描述：基于文件名（和可选的前几行内容）判断主题/性质，按相关性高的原则为每个文件规划目标存放位置。目标目录结构深度不超过三级。
   - 输入：inbox_files.json（可选结合文件头 N 行）
   - 输出文件：classification_plan.json（结构化建议）
   - classification_plan.json 格式（示例）：
     - [
         {
           "filename": "2025-09-01 meeting.md",
           "source_path": "inbox/2025-09-01 meeting.md",
           "suggested_target": "Work/Meetings/2025",
           "reason": ["meeting","2025","work"]
         }, ...
       ]
   - 规则：
     - 子文件夹深度 ≤ 3（例如：Top/Second/Third）。
     - 优先按关键字分组（例如：meeting, project name, personal, archive）。
     - 同名冲突时建议添加后缀或按日期归档（在 classification_plan.json 中标注冲突策略）。

4. 生成移动脚本（待用户确认）
   - 描述：根据信息确认后，生成 Windows cmd 脚本（UTF-8）包含 move 命令但不自动执行。
   - 输出文件：apply_moves.cmd（UTF-8）
   - 脚本格式示例（每一条为一条 move 命令）：
     - move /Y "C:\path\to\vault\inbox\file.md" "C:\path\to\vault\Work\Meetings\file.md"
   - 生成时说明：
     - 使用绝对路径或相对 Vault 根路径（由用户选择）。
     - 若目标文件夹不存在，脚本应包含 mkdir 命令（mkdir "C:\path\to\vault\Work\Meetings"）或用 IF NOT EXIST 检查。
   - 示例脚本片段：
     - @echo off
       mkdir "C:\path\to\vault\Work\Meetings" 2>NUL
       move /Y "C:\path\to\vault\inbox\2025-09-01 meeting.md" "C:\path\to\vault\Work\Meetings\2025-09-01 meeting.md"

交互与确认流程（机器友好）
- cline 首先执行步骤 1 和 2，并产生 directory_tree.json 与 inbox_files.json（内部）。
- cline 运行分析模块生成 classification_plan.json，并将该文件提供给用户以供审核。
- 用户确认或编辑 classification_plan.json 后，cline 生成 apply_moves.cmd（UTF-8）供用户下载/检查。
- 在用户明确确认执行后，cline 可选择：
  - 输出 apply_moves.cmd 给用户并不执行；
  - 或以管理员权限在用户允许下执行该脚本。

附加注意事项（规范）
- 所有输出文件必须为 UTF-8 编码，不含 BOM（或按用户指定）。
- 目标文件夹层级不得超过 3 层（Top/Second/Third）。如分析建议超过 3 层必须自动合并到第三层。
- 不要删除原文件；只使用“move”或 Move-Item（PowerShell）进行移动。
- 任何自动操作需在获得用户确认后执行。

示例命令集合（快速参考）
- 列出文件并写入 inbox_files.json（PowerShell）：
  - powershell -Command "Get-ChildItem -LiteralPath 'C:\\path\\to\\vault\\{文件夹}' -Recurse -File | Select FullName,Name,DirectoryName | ConvertTo-Json -Depth 5 | Out-File inbox_files.json -Encoding utf8"
- 生成 moves 脚本（伪命令说明）：
  - For each item in classification_plan.json:
    - ensure target dir exists -> write mkdir command
    - write move /Y "source" "target"

结束语
- 本文件为机器优先格式，供 cline 解析与执行。所有移动操作在用户确认前仅输出脚本，不执行实际移动。