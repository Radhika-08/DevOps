#!/bin/bash

mkdir -p backups

docker inspect day05-web > backups/container_backup.json

echo "Backup Created Successfully"
