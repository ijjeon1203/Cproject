#!/bin/bash

# 폴더 목록이 있는 파일
INPUT_FILE="../list/folderList.md"

# 파일이 존재하는지 확인
if [ ! -f "$INPUT_FILE" ]; then
    echo "file '$INPUT_FILE' does not exist"
    exit 1
fi

# 파일에서 한 줄씩 읽어서 폴더 생성
while IFS= read -r folder; do
    # 빈 줄이거나 공백만 있는 경우 건너뜀
    if [[ -z "$folder" || "$folder" =~ ^[[:space:]]*$ ]]; then
        continue
    fi

    # 폴더가 존재하지 않으면 생성
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        echo "create Folder : $folder"
    else
        echo "$folder is already exist"
    fi
done < "$INPUT_FILE"

echo "finish!"
