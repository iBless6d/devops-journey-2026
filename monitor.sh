#!/bin/bash
cpu_limit=80
restarted_count=0

echo "---🔥 DevOps Server Monitor v2.0 🔥 ---"
read -p "👤 Enter Admin Name: " admin_name

echo " Welcome $admin_name! Starting diagnostics..."
sleep 1

for server in "App-Server" "DB-Database" "Cache-Redis"; do
	echo " ______________________________"
	echo "🔍 Checking: $server"
	read -p "👉 Enter CPU Usage (0-100): " usage
	
	if [ "$usage" -ge "$cpu_limit" ]; then
		echo "❌ DANGER! CPU is too high ($usage%)."
        	echo "🔄 Restarting $server..." 
		sleep 1
		restarted_count=$(( restarted_count + 1 ))
	else
		echo "✅ $server is stable ($usage%)."
	fi
done

echo "========================================="
echo "📊 REPORT SUMMARY FOR: $admin_name"
echo "🚫 Total Servers Restarted: $restarted_count"

if [ "$restarted_count" -eq 0 ];then
	echo "🎉 Great job! The system is 100% healthy."
else
	echo "⚠️ Warning: The infrastructure is unstable."
fi
