#!/bin/bash
app_name="Instagram_DB"
backup_date="2026-01-17"
server_ip="192.168.1.50"

total_files=500
deleted_files=120
final_count=$((total_files - deleted_files))

echo "------------------------------------"
echo "🚀 Starting backup for: $app_name"
echo "📅 Date: $backup_date"
echo "🌐 Server: $server_ip"
echo "------------------------------------"

echo "♻️  Cleaning old files..."
echo "✅ Done! We kept $final_count files safe."
echo "------------------------------------"
