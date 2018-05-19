import random

from flask import Flask, render_template

app = Flask(__name__)

# list of cat images
base_url = "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced"
image_name_prefix = "anigif_enhanced-buzz"

images = [
    f"{base_url}/webdr01/15/9/{image_name_prefix}-31540-1381844535-8.gif",
    f"{base_url}/webdr05/15/9/{image_name_prefix}-26388-1381844103-11.gif",
    f"{base_url}/webdr05/15/9/{image_name_prefix}-26390-1381844163-18.gif",
    f"{base_url}/webdr06/15/10/{image_name_prefix}-1376-1381846217-0.gif",
    f"{base_url}/webdr03/15/9/{image_name_prefix}-3391-1381844336-26.gif",
    f"{base_url}/webdr06/15/10/{image_name_prefix}-29111-1381845968-0.gif",
    f"{base_url}/webdr03/15/9/{image_name_prefix}-3409-1381844582-13.gif",
    f"{base_url}/webdr02/15/9/{image_name_prefix}-19667-1381844937-10.gif",
    f"{base_url}/webdr06/15/9/{image_name_prefix}-18774-1381844645-6.gif",
    f"{base_url}/webdr06/15/9/{image_name_prefix}-25158-1381844793-0.gif",
    f"{base_url}/webdr02/15/9/{image_name_prefix}-19708-1381845008-7.gif",
    f"{base_url}/webdr05/15/9/{image_name_prefix}-26358-1381845043-13.gif",
    f"{base_url}/webdr05/15/9/{image_name_prefix}-26383-1381845104-25.gif",
    f"{base_url}/webdr02/15/9/{image_name_prefix}-19645-1381845207-5.gif",
    f"{base_url}/webdr03/15/10/{image_name_prefix}-11864-1381846346-0.gif",
    f"{base_url}/webdr05/15/9/{image_name_prefix}-19070-1381845280-0.gif",
    f"{base_url}/webdr01/15/9/{image_name_prefix}-27162-1381845360-0.gif",
    f"{base_url}/webdr06/15/9/{image_name_prefix}-25329-1381845415-0.gif",
    f"{base_url}/webdr01/15/9/{image_name_prefix}-27248-1381845460-0.gif",
    f"{base_url}/webdr06/15/9/{image_name_prefix}-23859-1381845509-0.gif",
    f"{base_url}/webdr02/15/10/{image_name_prefix}-19659-1381845602-0.gif",
    f"{base_url}/webdr02/15/10/{image_name_prefix}-19703-1381845685-16.gif",
    f"{base_url}/webdr06/15/10/{image_name_prefix}-25498-1381845743-9.gif",
    f"{base_url}/webdr01/15/10/{image_name_prefix}-27831-1381845794-0.gif",
    f"{base_url}/webdr01/15/10/{image_name_prefix}-27162-1381845926-2.gif",
    f"{base_url}/webdr01/15/10/{image_name_prefix}-26581-1381846023-15.gif",
    f"{base_url}/webdr06/15/10/{image_name_prefix}-23501-1381846064-1.gif",
    f"{base_url}/webdr01/15/10/{image_name_prefix}-26511-1381846135-9.gif",
    f"{base_url}/webdr03/15/10/{image_name_prefix}-11980-1381846269-1.gif",
    f"{base_url}/webdr01/15/10/{image_name_prefix}-27208-1381845845-0.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
