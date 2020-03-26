#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import requests
from requests_toolbelt import MultipartEncoder


server_url = u"http://aitest.i.sinotrans.com/OcrPlugins/core/ocr"

def ocr_img(upload_file):
    # try:
    #     if upload_file.find('.jpg') != -1:
    #         res_txt = upload_file.replace('.jpg', '.txt')
    #     elif upload_file.find('.png') != -1:
    #         res_txt = upload_file.replace('.png', '.txt')
    #     elif upload_file.find('.jpeg') != -1:
    #         res_txt = upload_file.replace('.jpeg', '.txt')
    #     else:
    #         print('no supost image fomat: ',upload_file)
    #
    #     if os.path.exists(res_txt) == True:
    #         print('txt exists')
    #         return
    # except:
    #     print('except')
    #     return

    file_name = os.path.basename(upload_file)
    m = MultipartEncoder(
        fields={
            'docType': 'TX_OCR_FOR_CJ',
            'ifNeedOcr': '1',
            'ocrType': '3',
            'appId': 'JHIkTU35',
            'appKey': 'HOA6Jl8c',
            'outputType': 'tencentResult',
            'appSecret': 'd3dc2e51865b8290df8ace8b403c936a',
            'files': (file_name, open(upload_file, 'rb'), 'image/%s' % os.path.splitext(upload_file)[-1][1:])
        }
    )

    print("ready process: ", upload_file)

    try:
        r = requests.post(
            server_url,
            data=m,
            headers={'Content-Type': m.content_type}
        )

        if r.status_code == 200:
            response_string = r.text
            print(response_string)

            # with open(res_txt, "a+",encoding='gb18030') as fr:
            #     fr.write(response_string)
            #     fr.close()

        del r
    except:
        # raise
        print("some error!")


if __name__ == "__main__":
    image_path = "D:/workdata/licence/0cdcd7be-4dfc-4b1f-89dc-fc99d0e4cd6a.jpg"
    ocr_img(image_path)