#!/bin/bash

# Example workflow for translating the GitBook

echo "🇺🇦 Ukrainian GitBook Translation Workflow"
echo "=========================================="

# Step 1: Backup original files
echo "1️⃣ Creating backups..."
find . -name "*.md" -exec cp {} backups/ \;

# Step 2: Translate specific chapters first (for testing)
echo "2️⃣ Translating introduction..."
python3 scripts/translate_gitbook.py --only "README.md"

# Step 3: Translate main content
echo "3️⃣ Translating main content..."
python3 scripts/translate_gitbook.py --skip "node_modules" ".git" "_book"

# Step 4: Review and build
echo "4️⃣ Building GitBook..."
gitbook build

# Step 5: Commit changes
echo "5️⃣ Ready to commit!"
echo "Review the changes and run: git add . && git commit -m 'Add Ukrainian translation'"
