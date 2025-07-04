# Send Webhook Action

通过 Python 脚本发送自定义 webhook（支持飞书卡片消息）。

## 用法示例

```yaml
- name: 发送飞书Webhook
  uses: ./  # 或者你的仓库名@分支
  with:
    url: ${{ secrets.FEISHU_WEBHOOK_URL }}
    bot: feishu
    title: '通知标题'
    subtitle: '副标题'
    payload: '消息内容'
    msg_type: 'info'  # 可选: info|success|warning|error
```

## 输入参数
- `url`：Webhook 地址（必填）
- `bot`：机器人类型（如 feishu，默认 feishu）
- `title`：标题（必填）
- `subtitle`：副标题（可选）
- `payload`：内容（必填）
- `msg_type`：类型 info|success|warning|error（可选，默认 info）

## 说明
- 支持飞书 V2 卡片消息格式。
- 其他 bot 类型可自行扩展。 