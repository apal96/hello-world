def commit():
    # TIMESTAMP=$(date +%c)
    print("Hello World")
    git pull
    git add .
    git commit -m "Auto update $TIMESTAMP"
    git push origin master

while true :
    commit()
    sleep 60
        