import argparse
import json
import sys
import urllib.request

def build_feishu_card(args, template):
    return {
        "msg_type": "interactive",
        "card": {
            "schema": "2.0",
            "config": {
                "update_multi": True,
                "style": {
                    "text_size": {
                        "normal_v2": {
                            "default": "normal",
                            "pc": "normal",
                            "mobile": "heading"
                        }
                    }
                }
            },
            "body": {
                "direction": "vertical",
                "padding": "12px 12px 12px 12px",
                "elements": [
                    {
                        "tag": "markdown",
                        "content": f"{args.payload}",
                        "text_align": "left",
                        "text_size": "normal_v2",
                        "margin": "0px 0px 0px 0px"
                    }
                ]
            },
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": args.title
                },
                "subtitle": {
                    "tag": "plain_text",
                    "content": args.subtitle
                },
                "template": template,
                "padding": "12px 12px 12px 12px"
            }
        }
    }

def main():
    parser = argparse.ArgumentParser(description='发送自定义 Webhook')
    parser.add_argument('--url', required=True, help='Webhook 地址')
    parser.add_argument('--bot', default='other', help='feishu|other')
    parser.add_argument('--title', required=True, help='标题')
    parser.add_argument('--subtitle', default='', help='副标题')
    parser.add_argument('--payload', required=True, help='内容')
    parser.add_argument('--msg_type', default='info', help='类型 info|success|warning|error')
    args = parser.parse_args()

    # 日志类型与颜色映射
    template_map = {
        'info': 'blue',
        'success': 'green',
        'warning': 'orange',
        'error': 'red'
    }
    msg_type = args.msg_type.lower()
    template = template_map.get(msg_type, 'blue')

    if args.bot == 'feishu':
        data = build_feishu_card(args, template)
        body = json.dumps(data, ensure_ascii=False)
    else:
        body = args.payload

    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(args.url, data=body.encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            if 200 <= status < 300:
                print(resp.read())
                print('Webhook 发送成功')
            else:
                print(f'Webhook 发送失败: {status} {resp.reason}', file=sys.stderr)
                sys.exit(1)
    except Exception as e:
        print(f'Webhook 发送失败: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 