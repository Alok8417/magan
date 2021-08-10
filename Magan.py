termux-calendar add \

    --title 'My meeting' \

    --id 'Google:Work Calendar' \

    --start "$unix_time_start" \

    --stop "$unix_time_stop" \

    --location "$latitude,$longitude" \

    --description 'A long horrible meeting' \

    --all-day 'false'
