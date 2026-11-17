#!/bin/bash

ARCHIVE_DIR = "archive"
LOG_FILE = "organizer.log"
DATA_SOURCE = "grades.csv"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "$ARCHIVE_DIR directory created successfully."
fi

if [ ! -f "$DATA_SOURCE" ]; then
    echo "Error: $DATA_SOURCE file can not be found."
    exit 1
fi

Timestamp = $(date +"%Y-%m-%d_%H-%M-%S")
Updated_file = "grades_${Timestamp}.csv"

mv "$DATA_SOURCE" "$ARCHIVE_DIR/$Updated_file"
echo "File $DATA_SOURCE has been moved to $ARCHIVE_DIR/$Updated_file successfully."

touch "$DATA_SOURCE"
echo "New file $DATA_SOURCE has been created successfully."

echo "Log entry: $Timestamp | Original file: $DATA_SOURCE | Archived: $ARCHIVE_DIR/$Updated_file" >> "$LOG_FILE"
echo "ARCHIVED $DATA_SOURCE as $ARCHIVE_DIR/$Updated_file and created a new empty $DATA_SOURCE."
