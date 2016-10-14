#This is for dummy_content django project
curl -XPOST -v -H "Content-Type: multipart/form-data" "http://127.0.0.1:8001/task/"  -F "image=@/home/randolph/Pictures/lbc.jpg" -F "doc=@/home/randolph/Music/BIRTHDAY_MUSIC/test_upload.mp3" -F "task_desc=test" -F "task_name=t1"
