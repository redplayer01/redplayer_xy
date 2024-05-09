#!/bin/bash

# 设置变量
batch_size=20
commit_message="Batch commit"

# 检查是否有参数传递
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# 切换到当前目录
cd "$(dirname "$0")" || exit

# 提交文件
commit_files() {
    git commit -m "$commit_message"
    git push
}

# 遍历目录下的文件
file_count=0
for file in "$1"/*; do
    if [ -f "$file" ]; then
        echo "Adding $file to commit..."
        git add $file
        ((file_count++))
        if [ $file_count -eq $batch_size ]; then
            commit_files
            file_count=0
        fi
    fi
done

# 提交最后一批文件
if [ $file_count -gt 0 ]; then
    commit_files
fi

echo "Batch commit complete."
