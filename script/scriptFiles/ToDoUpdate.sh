#!/bin/bash

# 최종 결과 파일
OUTPUT_FILE="Todo.md"

# 기존 파일 백업 (선택 사항)
mv $OUTPUT_FILE "${OUTPUT_FILE}.bak"

# 헤더 추가
echo "# 종합 TODO 리스트" > $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# 각 폴더의 TODO 파일 합치기
for folder in A B C; do
    if [ -f "$folder/todo.md" ]; then
        echo "## $folder" >> $OUTPUT_FILE
        cat "$folder/todo.md" >> $OUTPUT_FILE
        echo "" >> $OUTPUT_FILE
    fi
done

echo "✅ 모든 TODO 내용을 ${OUTPUT_FILE}에 정리 완료!"

추가
- 입력,선택해서 합치기 
- # 기준으로 나누기 



