#Dont change anything without informing us
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Prince94163/AutoFilter1 /AutoFilter1
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AutoFilter1
fi
cd /AutoFilter1
pip3 install -U -r requirements.txt
pip3 install spotdl
pip3 install yt-dlp
pip3 install speedtest
pip3 install youtube-dl

echo "Starting Bot...."
python3 bot.py
