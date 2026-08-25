import os
import random
from datetime import datetime, timedelta

contents = [
    {"title": "日本で運転免許を取得するまでの完全ガイド"},
    {"title": "外国人が日本で車を買うための必要書類と手続き"},
    {"title": "自社ローンとは？審査に通りやすい中古車販売店の見分け方"},
    {"title": "日本の交通ルール：外国人が間違いやすいポイント5選"},
    {"title": "自動車保険（任意保険）は絶対必要？基礎知識を解説"},
    {"title": "中古車選びのコツ：走行距離と年式どちらを重視すべき？"},
    {"title": "外国籍でも組める自動車ローンの選び方と注意点"},
    {"title": "車庫証明（保管場所標章）の取り方と必要なもの"},
    {"title": "軽自動車と普通車、初めてのマイカーにはどっちがおすすめ？"},
    {"title": "車検（自動車検査登録制度）の費用と流れを徹底解説"},
    {"title": "学科試験に一発合格するための勉強法とコツ"},
    {"title": "初心者マークのルールと違反時のペナルティ"},
    {"title": "維持費はいくら？日本での車生活マニュアル"}
]

out_dir = "../../scratch_backup/JP_License_GO/blog/articles"
blog_index = "../../scratch_backup/JP_License_GO/blog/blog.html"

# Fix dates
months = [
    (2025, 8), (2025, 9), (2025, 10), (2025, 11), (2025, 12),
    (2026, 1), (2026, 2), (2026, 3), (2026, 4), (2026, 5),
    (2026, 6), (2026, 7), (2026, 8)
]
dates = []
for year, month in months:
    day = random.randint(1, 28)
    if year == 2026 and month == 8:
        day = random.randint(1, 15) # Keep well below Aug 25
    dates.append(datetime(year, month, day))
dates.sort(reverse=True)

index_items = []

for i, (date, article_data) in enumerate(zip(dates, contents)):
    date_str = date.strftime('%Y年%m月%d日')
    update_meta = ""
    if i < 3:
        update_date = date + timedelta(days=random.randint(2, 6))
        # Ensure update date is also strictly past
        if update_date > datetime(2026, 8, 24):
            update_date = datetime(2026, 8, 24)
        update_meta = f" | 🔄 最終更新日: {update_date.strftime('%Y年%m月%d日')}"
        
    filename = f"article_{i+1}.html"
    
    # Read existing file, replace the meta line
    filepath = os.path.join(out_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the meta block (very fragile but we know the exact format)
    import re
    new_meta = f"<span>📅 公開日: {date_str} {update_meta}</span>"
    content = re.sub(r'<span>📅 公開日:.*?</span>', new_meta, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Append to index
    index_items.append(f'<li style="padding: 15px 0; border-bottom: 1px dashed #ccc; display: flex; align-items: center;"><span class="date" style="color: #777; font-size: 0.9rem; min-width: 120px; display: inline-block;">{date_str}</span> <a href="articles/{filename}" style="color: #0056b3; text-decoration: none; font-size: 1.1rem; font-weight: bold;">{article_data["title"]}</a></li>')

# Re-write blog.html
index_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>お役立ちコラム - JapanMenkyoGo</title>
    <style>
        body {{ font-family: 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ font-size: 2rem; color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 10px; }}
        ul.blog-list {{ list-style-type: none; padding: 0; }}
        a:hover {{ text-decoration: underline !important; }}
        .back-link {{ margin-top: 30px; display: inline-block; color: #0056b3; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>📚 お役立ちコラム</h1>
    <p>日本での免許取得から、マイカー購入、カーライフの充実まで、外国人の方にも役立つ情報をお届けします。</p>
    
    <ul class="blog-list">
        {chr(10).join(index_items)}
    </ul>
    
    <a href="../index.html" class="back-link">← アプリ公式サイトへ戻る</a>
</body>
</html>
"""

with open(blog_index, 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Dates fixed!")
