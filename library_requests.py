# ライブラリをインポートして利用可能にする
import requests

# get()関数でWebページを取得できる
r = requests.get('https://gihyo.jp/dp')
print(r)

# get()関数の戻り値はResponceオブジェクト
# type(r)

# .status_code属性でHTTPステータスコードを取得できる
# print(r.status_code)

# headers属性でHTTPヘッダーの辞書を取得できる
# print(r.headers['content-type'])

# encoding属性でHTTPヘッダーから得られたエンコーディングを取得する
# print(r.encoding)

# text属性でstr型にデコードしたレスポンスボディを取得できる
# print(r.text)

# content属性でbytes型のレスポンスボディを取得できる
# print(r.content)