python manage.py collectstatic
sudo systemctl status gunicorn
sudo systemctl status nginx
sudo systemctl restart gunicorn2
sudo systemctl restart nginx
source venv/bin/activate
sudo journalctl -u gunicorn
sudo journalctl -u nginx

