import http.server, os

class Handler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        # أي طلب لملف العرض يُرسل كتنزيل إجباري باسم واضح
        if self.path.split('?')[0] in ('/download', '/Goiter_Presentation.pptx'):
            self.path = '/Goiter_Presentation.pptx'
            fpath = os.path.join(os.getcwd(), 'Goiter_Presentation.pptx')
            if os.path.exists(fpath):
                f = open(fpath, 'rb')
                self.send_response(200)
                self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.presentationml.presentation')
                self.send_header('Content-Disposition', 'attachment; filename="Goiter_Presentation.pptx"')
                self.send_header('Content-Length', str(os.path.getsize(fpath)))
                self.end_headers()
                return f
        return super().send_head()

if __name__ == '__main__':
    http.server.ThreadingHTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
