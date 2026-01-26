#!/bin/bash 

cpu_usage=$(( RANDOM % 100 ))
cpu_limit=80
date_now=$(date)
if [ "$cpu_usage" -ge "$cpu_limit" ]; then
	echo "[$date_now] 🚨 ALERT: CPU is High ($cpu_usage%). Restarting Server..."
else 
	echo "[$date_now] ✅ OK: System is stable ($cpu_usage%)."
fi

