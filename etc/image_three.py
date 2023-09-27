import json

# JSON 파일 경로
json_file_path = 'image_three.json'

# 쓸 파일 경로
output_file_path = 'image_three_parsing.json'

# JSON 파일 열기
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 파싱 및 출력 파일 생성
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for item in data:
        save_date = item["save_date"][:10] + "T" + item["save_date"][11:]
        parsed_item = [
            {"index": {"_index": "image_three", "_id": item["identity"]}},
            {"seq": item["seq"],"save_date": save_date,"imagepath": item["imagepath"],"title": item["title"],"content": item["content"],"origin_name": item["origin_name"],"hash_name": item["hash_name"],"thumbnail": item["thumbnail"]}

        ]

        for item in parsed_item:
            output_file.write(json.dumps(item, ensure_ascii=False) + '\n')


print("정상완료")